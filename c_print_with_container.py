# usamos un contenedor para evitar una cadena de mensajes hacia abajo

import streamlit as st
import time
st.title("Hello world")
st.subheader('and Mars')
st.text('Im going to tech you how to use this')
st.markdown("___")

message_container = st.empty()

while True:
    message_container.write('hi')
    time.sleep(2)
    message_container.write('bye')
    time.sleep(2)
    message_container.empty()
