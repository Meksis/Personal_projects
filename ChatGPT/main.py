import openai, json
import streamlit as st
from random import randint



spinner_texts = ['Подождите немного, чат-бот крутит ботаническое катание на клавишах.',
 'Наши черепахи-программисты ведут крупный турнир в штанге. Подождите, пока они поднимут все коды в районе.',
 'Чат-бот летает на свободной печатной каретке, но сделал армию бумажных самолетиков. Мы их разбираем - прямо сейчас!',
 'К сожалению, чат-бот попал в игровой лабиринт. Подождите, пока он найдет выход и вернется к вам.',
 'Мы в процессе усовершенствования облика чат-бота. Подождите, пока мы ему приклеим улыбку.',
 'Ваш запрос отправлен в интернет-пространство на поиски самых эпических ответов. Потерпите немного.',
 'Друзья роботы не сидят сложа руки! Чат-бот сейчас поехал на свидание с учебником по искусственному интеллекту.',
 'Понадобилось несколько команд чтобы переубедить светофор зажечь зеленый свет. Подождите чуть-чуть, мы уже близки!',
 'Чат-бот проявил себя как юморист, и ушел становиться профессиональным клоуном. Мы пытаемся уговорить его вернуться.',
 'В нашем цифровом саду чат-бот сейчас ухаживает за растениями алгоритмов. Зайдите позже, чтобы насладиться цветущими идеями.',
 'Чат-бот отправился на эмоционально-синтаксический анализ, чтобы проверить, какие слова и фразы вызывают больше радости. Загляните через пару минут!',
 'На данный момент чат-бот делает перерыв, пьет чашечку текстового кофе и набирается вдохновения. Он вернется к вам с энергичными ответами!',
 'Мы еще раз находимся в Флэшмобе Фальшмарша и кажется, чат-бот станцевал слишком быстро. Мы загружаем новый танцевальный алгоритм, подождите немного.',
 'Наши кибер-художники заняты созданием шедевров на пикселях. Подождите, чтобы увидеть мистическую картину ответов.',
 'У нашего чат-бота случился галопировающий пав?ло?. Мы его ремонтируем, подождите, пока он восстанет на ноги.',
 'В лаборатории киберсознания по случаю праздника раздаются электронные подарки. Чат-бот проверяет каждый, чтобы убедиться, что они безопасны для вас.',
 'Наши цифровые дельфины вышли на свадебный парад. Чат-бот носит фалеристическую форму и машет плавником, но вернется совсем скоро!',
 'Чат-бот настроил музыку и начал знакомство с битами. Он ищет свой идеальный ритм, вернется к вам, когда будет готов для вдохновенных ответов.',
 'Чат-бот отправился на межгалактическую экскурсию в поисках новых знаний. Пока он путешествует в фотонной среде, мы будем ожидать его возвращение.']

with open('configs.json', 'r', encoding='utf-8') as file : 
    file = json.loads(file.read())
    openai.api_key = file['api_key'] 
    txt_for_setup = file['setup_text']

def make_response(prompt : str, system_prompt : str = '') -> list[str, list]:
    messages = [
            {
                "role" : "system",
                'content' : system_prompt
            },

            * st.session_state.history,

            {
                "role" : "user",
                'content' : prompt
            },
        ]
    
    
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )

    response = response.choices[0].message.content if 'choices' in response else False

    if response:
        # st.session_state.history.append({'role' : 'user', 'content' : prompt})
        # st.session_state.history.append({'role' : 'assistant', 'content' : response})

        return(response)

    else:
        return(response)

def change_startup_text():
    with open('configs.json', 'r', encoding='utf-8') as file:
        file_ = json.loads(file.read())
        file_.update({'setup_text' : prompt_changer})
    
    with open('configs.json', 'w', encoding='utf-8') as file:
        json.dump(file_, file, ensure_ascii=True, indent=4)

prompt_changer = st.sidebar.text_area('Изменить начальные установки', value = txt_for_setup, key = 'startup_text_radeactor_area')
prompt_fixator = st.sidebar.button('Подвердить изменение промпта')

prompt_input = st.chat_input('Ваш запрос здесь')




if prompt_fixator:
    change_startup_text()


if prompt_input:
    with st.chat_message('user'):
        # st.code(prompt_input)

        if 'history' not in st.session_state:
            st.session_state.history = [{'role' : 'user', 'content' : prompt_input}]
        
        else:
            st.session_state.history.append({'role' : 'user', 'content' : prompt_input})
            
    for message in st.session_state.history:
        with st.chat_message(message['role']):
            # st.code(message['content'])
            st.write(message['content'])

    with st.spinner(spinner_texts[randint(0, len(spinner_texts) - 1)]):
        response = make_response(prompt_input, prompt_changer)

        st.session_state.history.append({'role' : 'assistant', 'content' : response})

    with st.chat_message('assistant'):
        # st.code(response)
        st.write(response)
        # st.text_area('да', response, disabled = True, label_visibility='hidden')



