#Importo las librerías que voy a necesitar 
import requests 
import json
import datetime
import csv
from collections import Counter 
import statistics

HISTORIAL_FILE = "historial_global.csv" #Llamo al archivo donde voy a guardar el historial de consultas
API_KEY = 'faf588bee287e1e62aa3c55abd236220'  #Clave de API de OpenWeatherMap. Tengo que moverla de aca.!!!



#Función para consultar clima actual y guardar datos en el historial. Manejando los errores posibles. 
#Primero creo una función para obtener los datos del clima actual de la ciudad que se vaya a consultar, a través de la API de OpenWeatherMap.
def clima_actual(ciudad, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather" #Link base de la API de OpenWeatherMap
    #Añado los parámetros para llamar a la API, que estan en la página de la API.
    parametros = {
        "q": ciudad, #Ciudad a consultar
        "appid": API_KEY, #Clave de la API
        "units": "metric", #Unidades en sistema métrico (Celsius)
        "lang": "es" #Idioma español 
    }
    print (f"Consultando el clima para {ciudad} a traves de OpenWeatherMap...")
    #Mensaje de espera para que el usuario sepa que se está procesando su solicitud.
    
    try:
        #Realizo la solicitud con los parámetros definidos.
        respuesta = requests.get(url, params=parametros, timeout=10)
        respuesta.raise_for_status() #Verifico si la respuesta fue exitosa o no (código 200)
        #Si la respuesta es exitosa, convierto la respuesta a JSON.
        #Si hay un error HTTP o de conexión, lanza una excepción.

        datos_clima = respuesta.json() #Convierto la respuesta de la API a JSON para que resulte más sencillo trabajar.
        return datos_clima #Devuelvo los datos del clima en formato JSON para poder usarlo en otras partes del código.
    except requests.exceptions.HTTPError as errh: #Preparo mensajes de error ante cualquier fallo de la API.
        if respuesta.status_code == 401:
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
    

def clima(usuario): #Creo la función clima que se ejecuta como opción del menú principal.
    ciudad = input("Ingrese el nombre de la ciudad a consutar: ")
    datos_clima_actual = clima_actual(ciudad, API_KEY) #Ejecuto la función para obtener los datos del clima actual de la ciudad ingresada.
    if datos_clima_actual:
        try:
            #Buscamos los datos que vamos a mostrarle al usuario en el archivo JSON que devuelve la API.
            temperatura = datos_clima_actual["main"]["temp"] #Datos de temperatura
            sensacion = datos_clima_actual["main"]["feels_like"] #Datos de sensación térmica
            humedad = datos_clima_actual["main"]["humidity"] #Datos de humedad en el ambiente
            descripcion = datos_clima_actual["weather"][0]["description"] #Descripción del clima, por ejemplo: "cielo despejado", "nublado", etc
            viento = datos_clima_actual["wind"]["speed"] #Datos de velocidad del viento 
            viento_kmh = viento * 3.6 #Convierto la velocidad a km/h multiplicandola por 3.6, la paso de m/s que es la unidad que devuelve la API a km/h.

            #Le muestro la información al usuario.

            print(f"\n Clima en {ciudad.capitalize()}:") #Capitalizo el nombre de la ciudad para que se vea mejor.
            print(f"- Temperatura: {temperatura} °C") #Añado las unidades para que se entiendan los datos, no es lo mismo 20 F que 20 °C
            print(f"- Sensación térmica: {sensacion} °C") 
            print(f"- Humedad: {humedad}%")
            print(f"- Condición: {descripcion.capitalize()}") #Capitalizo la descripción para que se vea mejor.
            print(f"- Viento: {viento_kmh} km/h") 

            fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #Fecha y hora actual en formato YYYY-MM-DD y HH:MM:SS
            #Pido el nombre de usuario para guardar en el historial.

            with open(HISTORIAL_FILE, "a", newline="") as archivo: #Guardo los datos consultados en el archivo historial global 
                writer = csv.writer(archivo)
                writer.writerow([usuario, ciudad, fecha_hora, temperatura, descripcion, humedad, viento_kmh])
            print("Consulta guardada en el historial global.")
        except KeyError:
            print("No se pudo procesar correctamente la información del clima.")



