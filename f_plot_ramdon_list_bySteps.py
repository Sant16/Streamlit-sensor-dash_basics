import streamlit as st
import random
import plotly.graph_objects as go
import time

# Configurar página y título del dashboard
st.set_page_config(page_title="Visualización en tiempo real", layout="wide")
st.title("Visualización en tiempo real de datos aleatorios")

# Crear figura de Plotly
fig = go.Figure()

# Configurar el eje y la leyenda
fig.update_layout(yaxis=dict(range=[0, 100]), legend=dict(x=0, y=1))
fig.update_layout(xaxis=dict(range=[0, 25]), legend=dict(x=0, y=1))

# Crear el contenedor para la gráfica
chart_container = st.empty()

x = []
y = []

while True:
    time.sleep(5)
    # Generar un nuevo dato aleatorio
    x.append(len(x))
    y.append(random.randint(0, 100))

    # Actualizar los datos en la gráfica
    fig.add_trace(go.Scatter(x=x, y=y, name='Random Data', mode='lines', line=dict(color='green', width=2)))

    # Mostrar la figura en Streamlit
    chart_container.plotly_chart(fig, use_container_width=True)

    # Limpiar los datos anteriores
    fig.data = fig.data[:-1]
    if len(x) > 10:
        # Limpiar la figura
        fig.data = []
        x = []
        y = []
