# imprime mensaje hi y bye

import streamlit as st
import time
st.title("Hello world")
st.subheader('and Mars')
st.text('Im going to tech you how to use this')
st.markdown("___")

while True:
    st.write('hi')
    time.sleep(2)
    st.write('bye')
    time.sleep(2)
