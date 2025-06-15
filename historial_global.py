# Importo las librerías que voy a necesitar 

import csv
from collections import Counter 
import statistics
import os

HISTORIAL_FILE = "historial_global.csv"         # Llamo al archivo donde voy a guardar el historial de consultas
CAMPOS =  ["usuario", "ciudad", "fecha", "temperatura", "condicion", "humedad", "viento"]    # Campos de los diccionarios guardados en el historial

# Opcion 2: Ver historial personal. Manejando los errores posibles.

# Primero creo una función para cargar los registros desde el archivo CSV
def cargar_historial():
    if not os.path.isfile(HISTORIAL_FILE):
        return []        # Si el archivo no existe, devuelve una lista vacía.
   
    registros = []
    try:   # Utilizamos el try para poder accionar en caso de posible error
        with open(HISTORIAL_FILE, mode='r', newline='', encoding='utf-8') as archivo:      # Abrimos el archivo como lector
            lector = csv.DictReader(archivo)
            for fila in lector:
                if all(campo in fila and fila[campo].strip() for campo in CAMPOS):        # Validación básica de estructura. Permitiendo omitir registros con datos vacíos
                    registros.append(fila)
                else:
                    print(f"Registro con campos faltantes omitido: {fila}")
        return registros
    except Exception as e:
        print(f"Error al intentar leer el historial: {e}")
        return []
    



# Función para mostrar el historial de un usuario para una ciudad específica
def historial_usuario(usuario):
    ciudad_historial = input("Ingrese la ciudad para la cual desea ver su historial: ").strip()
    registros = cargar_historial()
    
    if not registros:
        print("No hay registros disponibles para consultar.")
        return
    encontrados = [fila for fila in registros
                      if fila["usuario"].strip().lower() == usuario.lower() and
                         fila["ciudad"].strip().lower() == ciudad_historial.lower()]
    if encontrados:
        print(f"\nHistorial de consultas para {ciudad_historial.capitalize()} del usuario {usuario}")
        for fila in encontrados:
            print(f"- Fecha: {fila['fecha']}, Temperatura: {float(fila['temperatura']):.2f} °C, Condición: {fila['condicion'].capitalize()}, Humedad: {fila['humedad']}%, Viento: {float(fila['viento']):.2f} km/h")
    else:
        print(f"No se encontraron registros para {ciudad_historial} en tu historial.")



# Opción 3: Estadísticas globales de uso

def estadisticas_globales():
    registros = cargar_historial()

    if not registros:
        print("No hay registros disponibles para calcular las estadísticas globales.")
        return

     # Inicializo las variables que voy a usar para almacenar los datos de las estadísticas.
    total_consultas = 0 
    ciudades = []             # Lista para almacenar las ciudades consultadas.
    temperaturas = []         # Lista para almacenar las temperaturas consultadas. 

    for fila in registros:
        try: 
            ciudad = fila['ciudad'].strip()
            temperatura = float(fila['temperatura'])
            ciudades.append(ciudad)
            temperaturas.append(temperatura)
            total_consultas += 1
        except (KeyError, ValueError):
            print(f"Registro inválido omitido: {fila}")
            continue

    if total_consultas == 0:
        print("Aún no hay registros en el historial.")
        return

    ciudad_mas_consultada = Counter(ciudades).most_common(1)[0][0]
    promedio_temperatura = statistics.mean(temperaturas)

    print("\nEstadísticas Globales:")
    print(f"* Total de consultas: {total_consultas}")
    print(f"* Ciudad más consultada: {ciudad_mas_consultada}")
    print(f"* Temperatura promedio: {promedio_temperatura:.2f} °C")
           


