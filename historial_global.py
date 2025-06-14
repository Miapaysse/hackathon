#Importo las librerías que voy a necesitar 
import requests 
import json
import datetime
import csv
from collections import Counter 
import statistics


HISTORIAL_FILE = "historial_global.csv" #Llamo al archivo donde voy a guardar el historial de consultas
API_KEY = 'faf588bee287e1e62aa3c55abd236220'  #Clave de API de OpenWeatherMap. Tengo que moverla de aca.!!!


def historial_usuario(usuario):
    ciudad_historial = input("Ingrese la ciudad para la cual desea ver su historial: ")
    try:
        with open(HISTORIAL_FILE, "r") as archivo: #Abro el archivo historial global para leerlo.
            lector = csv.reader(archivo)
            encontrado = False #Variable para verificar si se encuentra registro de la ciudad pedida. La inicializo en False para que cambie si es que se encuentra algo.
            print(f"\nHistorial de consultas para {ciudad_historial.capitalize()}:")
            for fila in lector:
                if fila[1].lower() == ciudad_historial.lower() and fila[0].lower() == usuario.lower() : #Comparo la ciudad ingresada con las ciudades del historial, ignorando mayúsculas y minúsculas, lo mismo con el usuario.
                    encontrado = True
                    print(f"Fecha y hora: {fila[2]}, Temperatura: {fila[3]} °C, Condición del clima: {fila[4]}, Humedad: {fila[5]}%, Viento: {fila[6]} m/s")
            if not encontrado:
                print(f"No se encontraron registros para la ciudad '{ciudad_historial}' en tu historial.")
    except FileNotFoundError:
        print("No se encontró el archivo de historial. Asegúrate de haber realizado consultas previamente.")


def estadisticas_globales():
    try:
        with open(HISTORIAL_FILE, newline = "") as archive: #Abro el archivo historial global para leerlo y poder procesarlo.
            lector = csv.reader(archive)
            next(lector) #Salto la primera fila si es que tiene encabezado, si no, la quito. 
            
            #Inicializo las variables que voy a usar para almacenar los datos de las estadísticas.
            total_consultas = 0 
            ciudades =[] #Lista para almacenar las ciudades consultadas.
            temperaturas =[] #Lista para almacenar las temperaturas consultadas. 


            for fila in lector:
                if len(fila) < 7:
                    continue  # por si hay filas incompletas

                #Desempaqueto los datos de cada fila del historial para procesarlos.
                usuario, ciudad, fecha, temperatura, condicion, humedad, viento = fila
                ciudades.append(ciudad)
                temperaturas.append(float(temperatura))
                total_consultas += 1

            if total_consultas == 0:
                print("Aún no hay registros en el historial.")
                return

            ciudad_mas_consultada = Counter(ciudades).most_common(1)[0][0]
            promedio_temperatura = statistics.mean(temperaturas)

            print("\nEstadísticas Globales:")
            print(f"* Total de consultas: {total_consultas}")
            print(f"* Ciudad más consultada: {ciudad_mas_consultada}")
            print(f"* Temperatura promedio: {promedio_temperatura:.2f} °C")

    except Exception as e:
        print(f"Error al procesar estadísticas: {e}")