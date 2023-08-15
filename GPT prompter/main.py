import streamlit as st
import json
import openai


def session_update_by_request_data():
    # global input_emptier, req_but_emptier
    st.session_state.input_prompt = str(input_prompt)
    

def create_requesting_place(input_prompt_text : str = ''):
    global input_emptier, req_but_emptier, input_prompt, request_button



    input_emptier = st.empty()
    with input_emptier:
        input_prompt = st.text_input("Основной запрос", input_prompt_text)


    req_but_emptier = st.empty()
    with req_but_emptier:
        request_button = st.button("Оформляем")

def del_inputs():
    global input_emptier, req_but_emptier, input_prompt, request_button
    
    input_emptier.empty()
    req_but_emptier.empty()
    
    del input_prompt, request_button


with open("configs.json", "r") as config_file:
    api_key = json.loads(config_file.read())["api_key"]

openai.api_key = api_key


system_prompt = st.sidebar.file_uploader("Файл со стартовым промптом", ["txt"])
system_prompt_text = ""

if system_prompt:
    st.code(system_prompt.getvalue().decode())
    system_prompt_text = system_prompt.getvalue().decode()
    
    


if 'input_prompt' not in st.session_state:
    st.session_state.input_prompt = ''

create_requesting_place(st.session_state.input_prompt)


if request_button:
    input_prompt_text = str(input_prompt)

    # session_update_by_request_data()
    # del_inputs()

    with st.spinner("Ждем ответ"):
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content" : system_prompt_text}, {"role": "user", "content" : input_prompt_text}])
    
    # create_requesting_place(st.session_state.input_prompt)

    if "choices" in response:
        response = response.choices[0].message.content
        
        st.code(response)

        # if st.button("Копировать"):
        #     pc.copy(response)
            # st.toast("Успешно скопировано", '💾')

    else:
        st.code("Нет ответа")
        # st.toast("Нет ответа")
    
