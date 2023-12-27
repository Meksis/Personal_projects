from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas as pd

import time

from datetime import datetime
from dateutil import relativedelta

import plotly.express as px


XPATH = By.XPATH

url = 'https://www.tinkoff.ru/invest/bonds/?start=0&end=12&country=Russian&orderType=Desc&sortType=ByYieldToClient'
# url = 'https://www.tinkoff.ru/invest/bonds/?start=0&end=2400&country=Russian&orderType=Desc&sortType=ByYieldToClient'

class Obligations_parser:
    def __init__(self, driver : webdriver.Firefox, url : str, existing_df : pd.DataFrame = pd.DataFrame()):
        self.driver = driver
        self.driver.maximize_window()
        self.prev_window_switch = 0
        self.previous_url = url

        self.driver.get(url)
        self.obligations_data = existing_df.copy()

    def next_layer(self, add_value : int = 12):
        start = self.previous_url[self.previous_url.index('start') : self.previous_url.index('&end')]
        start = int(start[start.index('=') + 1 :]) + add_value

        end = self.previous_url[ self.previous_url.index('end') : self.previous_url.index('&country')]
        end = int(end[end.index('=') + 1 :]) + add_value


        self.previous_url = f"{self.previous_url[ : self.previous_url.index('start') + 6]}{start}&end={end}&{self.previous_url[self.previous_url.index('country') :]}"

        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(self.previous_url)

        self.elements_iterator()

            
    def grab_paper_info(self, paper_url : str = ''):
        if paper_url:
            self.driver.execute_script("window.open('');")
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.get(paper_url)
        
        else:
            self.driver.get(paper_url)

        paper_data = {}

        try:
            paper_data.update({'Название' : [self.driver.find_element(XPATH, '//span[@class = "SecurityHeader__showName_iw6qC"]').text]})
            
            paper_data.update({'Код' : [self.driver.find_element(XPATH, '//span[@class = "SecurityHeader__ticker_j7fZW"]').text]})

            cost = self.driver.find_element(XPATH, '//div[@class = "SecurityInvitingScreen__price_FSP8P"]').text.replace('\n', '').replace(',', '.').replace(' ', '')[ : -1]
            paper_data.update({'Цена' : [float(cost) if cost else -1]})
            
            # paper_data.update({'Рейтинг' : [self.driver.find_element(XPATH, '//div[@class = "SecurityHeader__panel_itBzT SecurityHeader__desktop_dL7RD"]/div[@class = "SecurityHeader__panelText_KDJdO"]').text]})
            

            paper_rating = self.driver.find_elements(XPATH, '//div[@class = "SecurityHeader__panel_itBzT SecurityHeader__desktop_dL7RD"]')
            paper_rating = paper_rating[0].text if len(paper_rating) == 1 else paper_rating[1].text
            paper_rating = paper_rating.split('\n')[1]

            paper_data.update({'Рейтинг' : [paper_rating]})

            paper_datas = self.driver.find_elements(XPATH, '//td[@class = "Table-module__cell_RJ0qz"]')


            for counter in range(1, len(paper_datas) + 1, 2):
                # print(paper_datas[counter - 1].text)
                match paper_datas[counter - 1].text:
                    case 'Дата колл-опциона':
                        print('Облигация с колл-опционом')
                        break

                    case 'Дата погашения облигации':
                        expire_date = datetime.strptime(paper_datas[counter].text, '%d.%m.%Y')
                        monthes_delta = relativedelta.relativedelta(expire_date, datetime.now())
                        monthes_delta = monthes_delta.years * 12 + monthes_delta.months

                        paper_data.update({'Срок(месяца)' : [monthes_delta]})


                    case "Величина купона":
                        paper_coupon = float(paper_datas[counter].text.replace('\n', '').replace(',', '.').replace(' ', '')[ : -2])
                        paper_coupon -= paper_coupon * 0.13     # Вычитаем налог 13% на купоны

                        paper_data.update({'Величина купона(-13%)' : [round(paper_coupon, 2)]})
                    
                    case "Номинал":
                        paper_data.update({'Номинал' : [float(paper_datas[counter].text.replace('\n', '').replace(',', '.').replace(' ', '')[ : -1])]})
                    
                    case "Количество выплат в год":
                        if 'Величина купона(-13%)' not in paper_data:
                            paper_data.update({'Величина купона(-13%)' : [0]})
                            
                        paper_data.update({'Выплат в год' : [int(paper_datas[counter].text)]})
                        paper_data.update({'Доходность(год)' : [round(paper_data['Выплат в год'][0] * paper_data['Величина купона(-13%)'][0], 2)]})
                        # paper_data.update({'Доходность(все время)' : [paper_data['Срок(месяца)'][0] // 2 * paper_data['Доходность(год)'][0]]})
                        # paper_data.update({'Доходность(все время)' : [paper_data['Срок(месяца)'][0] // paper_data['Выплат в год'][0] * paper_data['Величина купона(-13%)'][0]]})

                        paper_data.update({'Доходность(все время)' : [round(paper_data['Срок(месяца)'][0] // paper_data['Выплат в год'][0] * paper_data['Величина купона(-13%)'][0], 2)]})
                        paper_data.update({'Доходность(% в год)' : [round(paper_data['Доходность(год)'][0] / paper_data['Цена'][0] * 100, 2)]})

                    
                    case 'Амортизация':
                        paper_data.update({'Амортизация' : [True] if paper_datas[counter] == 'Да' else [False]})
                    

            print(paper_data)

            paper_data.update({'Ссылка' : [paper_url]})

            

            # print(pd.DataFrame(paper_data))
            # print(pd.DataFrame.from_dict(paper_data), )

            

            self.obligations_data = pd.concat([self.obligations_data, pd.DataFrame(paper_data)])

            
            self.driver.close()

        except Exception:
            print('Тулево словили ошибулю')
            self.driver.close()
            time.sleep(10)
            self.grab_paper_info()


    def elements_iterator(self):

        # link_buttons_class = 'Link-module__link_yQVl1 Link-module__link_theme_default_mkRhf'

        # Использую тр и тд, поскольку на сайте в строках тр 5 ссылок с нужным адресом, потому просто по классу ссылки не выйдет найти одно совпадение - придется потом чистить список. Приходится потихоьнку находить элементы.
        # tr_link_buttons_class = 'Table-module__row_Qlwsh Table-module__row_clickable_FeO1O'
        tr_link_buttons_class = 'TableRowCell-module__row_clickable_noFXY'
        # td_link_buttons_class = 'Table-module__cell_RJ0qz'

        # papers_rows = self.driver.find_elements(XPATH, f'//tr[@class = "{tr_link_buttons_class}"]')
        papers_rows = self.driver.find_elements(By.CLASS_NAME, tr_link_buttons_class)
        
        for paper in papers_rows:
            self.driver.switch_to.window(self.driver.window_handles[-1])

            try:
                paper_link = paper.find_element(XPATH, 'td').find_element(XPATH, 'a').get_attribute('href')
            
            except:
                time.sleep(3)
                paper_link = paper.find_element(XPATH, 'td').find_element(XPATH, 'a').get_attribute('href')
            
            
            self.grab_paper_info(paper_link)
            print(len(self.obligations_data), '\n')

        
        self.driver.switch_to.window(self.driver.window_handles[0])

        if len(self.driver.find_elements(By.CLASS_NAME, 'Pagination-module__item_arrow_mCpmW')) == 2:
            self.next_layer()
        
        else:
            print(f'Вышли из функции, поскольку Больше страниц нет')
            return(self.obligations_data)
        
class DataProcessing():
    def change_url(self, url, start_val, end_val):
        return(f"{url[ : url.index('start') + 6]}{start_val}&end={end_val}&{url[url.index('country') :]}")
    
    
    def df_cutter(self, df, resize_to_n_rows : int):
        return(pd.DataFrame(df.iloc[ : resize_to_n_rows]))
    
    def plot_papers(self, df: pd.DataFrame):
        # if 'Доходность(все время)' in df.columns:
        #     target_column_name = 'Доходность(все время)'

        # elif 'Доходность(год)' in df.columns:
        #     target_column_name = 'Доходность(год)'

        # else:
        #     target_column_name = None

        target_column_name = 'Доходность(% в год)'

        # Используйте Plotly Express для создания интерактивного графика
        fig = px.scatter(df, y=target_column_name, x='Цена', color='Код', size_max=10, hover_data=['Код', "Название", "Цена", "Доходность(% в год)", "Срок(месяца)"])

        # Настройки осей и заголовка
        fig.update_xaxes(title_text='Цена')
        fig.update_yaxes(title_text=target_column_name)
        fig.update_layout(title='Зависимость цены от доходности для бумаг')

        # Отображаем график
        fig.show()
