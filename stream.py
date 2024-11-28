import streamlit as st
from assist import ask_gpt

st.title("Асистент Василя Сухомлинського")
st.write("Цей AI допоможе вам дізнатися більше про педагогічні ідеї Сухомлинського.")

user_input = st.text_input("Введіть ваш запит:")
if user_input:
    response = ask_gpt(user_input)
    st.write("Відповідь асистента:")
    st.write(response)
