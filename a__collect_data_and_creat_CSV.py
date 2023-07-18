import serial
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import time

flag = 0

# Función para actualizar la gráfica en tiempo real
def update_plot():
    ax.clear()
    ax.axis([0, 20, 10, 110])
    ax.plot(datos_hum, label='Hum abs', linestyle='-', color='r', linewidth=3)
    ax.plot(datos_temp, label='Temp °C', linestyle='none', marker='.', markersize=3, color='b', linewidth=0.1)
    ax.legend(loc='upper left')  # Fijar la posición de la leyenda en la esquina superior izquierda
    plt.draw()

# Configuración de la comunicación serial
ser = serial.Serial('COM7', 9600, timeout=1)
j = 1
workbook = openpyxl.Workbook()
# Lista para almacenar los datos de la señal
datos_hum = []
datos_temp = []

# Configuración de la gráfica
plt.ion()  # Modo interactivo para graficar en tiempo real
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1) #parcelas, depende si se quiere dividir la pantalla para varias graficas

# Crear archivo CSV o cargar datos existentes
csv_file = "datos.csv"
csv_headers = ['Temperatura', 'Humedad']
csv_data = []

try:
    # Leer datos existentes del archivo CSV
    df = pd.read_csv(csv_file)
    csv_data = df.values.tolist()
except FileNotFoundError:
    pass

while True:
    # Leer un valor del puerto serial
    dato = ser.readline().decode('ascii').strip()
    if flag == 1:
        datos = dato.split('|')
        if len(datos) == 2:
            try:
                h = float(datos[0])
                t = float(datos[1])

                datos_hum.append(h)
                datos_temp.append(t)
                num_puntos = 20
                if len(datos_hum) >= num_puntos:

                    # Agregar los nuevos datos a csv_data
                    for i in range(len(datos_temp)):
                        csv_data.append([datos_temp[i], datos_hum[i]])

                    # Guardar los datos en el archivo CSV
                    df = pd.DataFrame(csv_data, columns=csv_headers)
                    df.to_csv(csv_file, index=False)

                    # Reiniciar las listas de datos
                    datos_hum = []
                    datos_temp = []

                update_plot()

            except ValueError:
                print("Error: No se pudieron convertir los datos a números.")
        else:
            print("Error: Datos incompletos.")
            flag = 0
    flag = 1

    plt.pause(0.001)  # Pausar para permitir la actualización de la gráfica
