import streamlit as st
import json
import openai
import pyperclip as pc
import time

with open("configs.json", "r") as config_file:
    api_key = json.loads(config_file.read())["api_key"]

openai.api_key = api_key

text_input = st.text_input('input text')

if st.button('remove'):
    text_input.
    text_input = ''