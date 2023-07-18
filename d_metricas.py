import streamlit as st
import random
import time

st.title("Hello world")
st.subheader('and Mars')
st.text('Im going to teach you how to use this')
st.markdown("___")

metric_container = st.empty()  # Contenedor vacío para la métrica

va = 0
d = 0
v2_str = str(d) + 'ms⁻¹'

while True:
    v = random.randint(0,500)
    v = round(v)
    v_str = str(v) + 'ms⁻¹'
    d = v- va 
    v2_str = str(d) + 'ms⁻¹'
    metric_container.metric(label="Wind Speed", value=v_str, delta=v2_str)
    va = v
    time.sleep(10)
    metric_container.empty()  # Borrar el valor anterior antes de mostrar el nuevo
