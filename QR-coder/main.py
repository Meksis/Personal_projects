import pyqrcode, os, shutil
import streamlit as st


def hex2dec(hex : str) -> int:
    alphabet = '0123456789abcdef'
    number = 0
    
    for counter, sym in enumerate(hex[::-1]):
        number += alphabet.index(sym) * 16 ** counter
    
    return(number)


def color_remaker(string : str) -> list[str]:
    return ([i[0] for i in [[f'{string[1 : ][counter-1]}{string[1 : ][counter]}' if counter % 2 else 0] for counter in range(len(string[ 1 : ]))] if i[0] ])


text_to_encode = st.text_input('Ваш текст для кодирования')

qr_code_color = st.sidebar.color_picker('Цвет для QR-кода', value = "#ffffff")
qr_code_bgcolor = st.sidebar.color_picker('Цвет для фона QR-кода', value = "#000000")

transparance_picker = st.sidebar.number_input('Степень непрозрачности', min_value=0, max_value = 255, value = 255)
scale_picker = st.select_slider('Размер кода', value = 5, options = range(1, 50))
quiet_zone_picker = st.sidebar.number_input('Толщина рамки кода', min_value=0, value = 4,)


qr_code_color_decoded = color_remaker(qr_code_color)
qr_code_bgcolor_decoded = color_remaker(qr_code_bgcolor)

# st.code(hex_splitted)


if st.button('Сваргнаить код'):
    qr_code = pyqrcode.create(text_to_encode)
    qr_code.png('swallow.png', scale=scale_picker, quiet_zone=quiet_zone_picker,
                    module_color=(hex2dec(qr_code_color_decoded[0]), hex2dec(qr_code_color_decoded[1]), hex2dec(qr_code_color_decoded[2])),
                    background=(hex2dec(qr_code_bgcolor_decoded[0]), hex2dec(qr_code_bgcolor_decoded[1]), hex2dec(qr_code_bgcolor_decoded[2]), transparance_picker)) 

    st.image('swallow.png')