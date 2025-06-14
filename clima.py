# Importo las librerías que voy a necesitar 

import requests 
import json
from datetime import datetime
import csv
from dotenv import load_dotenv
import os

HISTORIAL_FILE = "historial_global.csv"     # Llamo al archivo donde voy a guardar el historial de consultas
CAMPOS = ["usuario", "ciudad", "fecha", "temperatura", "condicion", "humedad", "viento"]    # Campos de los diccionarios guardados en el historial

load_dotenv()    # Cargo la API KEY desde el archivo .env donde esta segura.
API_KEY = os.getenv("OWM_API_KEY") # Clave de API de OpenWeatherMap.



# Opción 1: Función para consultar clima actual y guardar datos en el historial. Manejando los errores posibles.

    # Primero creo una función para obtener los datos del clima actual de la ciudad que se vaya a consultar, a través de la API de OpenWeatherMap.

def clima_actual(ciudad, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather" #Link base de la API de OpenWeatherMap
    
    parametros = {     # Añado los parámetros para llamar a la API, que están en la página de la API.
        "q": ciudad, #Ciudad a consultar
        "appid": api_key, #Clave de la API
        "units": "metric", #Unidades en sistema métrico (Celsius)
        "lang": "es" #Idioma español 
    }
    print (f"Consultando el clima para {ciudad} a traves de OpenWeatherMap...")    # Mensaje de espera para que el usuario sepa que se está procesando su solicitud.
    
    try:
        respuesta = requests.get(url, params=parametros, timeout=10)    # Realizo la solicitud con los parámetros definidos.
        respuesta.raise_for_status()                                    # Verifico si la respuesta fue exitosa o no (código 200)
        datos_clima = respuesta.json()                                  # Si la respuesta fue exitosa, convierto la respuesta de la API a JSON para que resulte más sencillo trabajar.
        return datos_clima                                              # Devuelvo los datos del clima en formato JSON para poder usarlo en otras partes del código.
    except requests.exceptions.HTTPError as errh:  # Si hay un error HTTP o de conexión, lanza una excepción.
        if respuesta.status_code == 401:           #  Preparo mensajes de error ante cualquier fallo de la API.
              print (f"Error de autenticación OWM: API KEY inválida.")
        elif respuesta.status_code == 404:
             print(f"Eror OWM: Ciudad '{ciudad}' no encontrada.")
        else:
             print(f"Error HTTP OWM: {errh}")
        return None
    except requests.exceptions.ConnectionError:
        print("Error de conexión OWM: No se pudo conectar al servidor.")
        return None
    except json.JSONDecodeError:
        print("Error OWM: La respuesta de la API no es JSON válido.")
        return None

    # Función para agregar un registro en el historial

def registrar_datos_historial(registro):
    archivo_existe = os.path.isfile(HISTORIAL_FILE)
    with open(HISTORIAL_FILE, "a", newline='', encoding='utf-8') as archivo:    # Guardo los datos consultados en el archivo historial global   
        writer = csv.DictWriter(archivo, fieldnames=CAMPOS)
        if not archivo_existe:
        writer.writeheader()  # Escribe encabezado solo si el archivo es nuevo
        writer.writerow(registro)

    # Creo la función clima que se ejecuta como opción del menú principal.

def clima(usuario): 
    ciudad = input("Ingrese el nombre de la ciudad a consultar: ").strip()
    datos_clima_actual = clima_actual(ciudad, API_KEY)     # Ejecuto la función para obtener los datos del clima actual de la ciudad ingresada.
    
    if datos_clima_actual:
        try: # Buscamos los datos que vamos a mostrarle al usuario en el archivo JSON.
            temperatura = datos_clima_actual["main"]["temp"]                 # Datos de temperatura
            sensacion = datos_clima_actual["main"]["feels_like"]             # Datos de sensación térmica
            humedad_porcentaje = datos_clima_actual["main"]["humidity"]      # Datos de humedad en el ambiente
            descripcion = datos_clima_actual["weather"][0]["description"]    # Descripción del clima, por ejemplo: "cielo despejado", "nublado", etc
            viento = datos_clima_actual["wind"]["speed"]                     # Datos de velocidad del viento 
            viento_kmh = viento * 3.6                                        # Convierto la velocidad a km/h multiplicandola por 3.6, la paso de m/s que es la unidad que devuelve la API a km/h.

                    # Le muestro la información al usuario.

            print(f"\n Clima en {ciudad.capitalize()}:") #Capitalizo el nombre de la ciudad para que se vea mejor.
            print(f"- Temperatura: {temperatura:.2f} °C") #Añado las unidades para que se entiendan los datos, no es lo mismo 20 F que 20 °C
            print(f"- Sensación térmica: {sensacion} °C") 
            print(f"- Humedad: {humedad_porcentaje}%")
            print(f"- Condición: {descripcion.capitalize()}") #Capitalizo la descripción para que se vea mejor.
            print(f"- Viento: {viento_kmh:.2f} km/h") 

            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #Fecha y hora actual en formato YYYY-MM-DD y HH:MM:SS

            registro = {        #Creo un diccionario para guardar los registros
                "usuario": usuario,
                "ciudad": ciudad,
                "fecha": fecha_hora,
                "temperatura": temperatura,
                "condicion": descripción,
                "humedad": humedad_porcentaje,
                "viento": viento_kmh
            }

            registrar_datos_historial(registro)
            print("Consulta guardada en el historial global.")
        except KeyError:
            print(f"No se pudo procesar correctamente la información del clima para {ciudad}.")
