## grafica los ultimos 300 datos de un archivo CSV

import streamlit as st
import plotly.graph_objects as go
import time
import pandas as pd

# Cargar datos desde el archivo CSV con encabezados
csv_file = "datos.csv"
csv_headers = ['Temperatura', 'Humedad']
df = pd.read_csv(csv_file, header=None, names=csv_headers)

last5 = df['Humedad'].tail(10).tolist()

# Configurar página y título del dashboard
st.set_page_config(page_title="Visualización en tiempo real", layout="wide")
st.title("Visualización en tiempo real de datos aleatorios")

# Crear figura de Plotly
fig = go.Figure()

# Configurar el eje y la leyenda
fig.update_layout(yaxis=dict(range=[0, 100]), legend=dict(x=0, y=1))
fig.update_layout(xaxis=dict(range=[0, 300]), legend=dict(x=0, y=1))

# Crear el contenedor para la gráfica
chart_container = st.empty()

x = []
y = []

while True:
    # Cargar datos desde el archivo CSV con encabezados
    csv_file = "datos.csv"
    csv_headers = ['Temperatura', 'Humedad']
    df = pd.read_csv(csv_file, header=None, names=csv_headers)
    last5 = df['Humedad'].tail(300).tolist()
    
    for _ in range(300):
        x.append(len(x) )
        y.append(last5[-1])

        # Actualizar los datos en la gráfica
        fig.add_trace(go.Scatter(x=x, y=y, name='Random Data', mode='lines', line=dict(color='green', width=2)))

        # Mostrar la figura en Streamlit
        chart_container.plotly_chart(fig, use_container_width=True)

        # Limpiar los datos anteriores
        fig.data = fig.data[:-1]
        time.sleep(0.01)
        if len(y) >= 299:
            # Limpiar la figura
            fig.data = []
            x = []
            y = []
