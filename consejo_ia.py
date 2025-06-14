# test_consejo_ia.py
import google.generativeai as genai
#Importo las librerías que voy a necesitar 
import requests 
import json
import csv
from collections import Counter 

from clima import clima

HISTORIAL_FILE = "historial_global.csv" #Llamo al archivo donde voy a guardar el historial de consultas

api_key_gemini = "AIzaSyB1EBXeDpuhSZ5a4oX1THmVW3aJmNdZGAM"  

def obtener_consejo_ia_gemini(api_key_gemini, ciudad, temperatura, condicion_clima,
viento, humedad):

    genai.configure(api_key=api_key_gemini)

    model = genai.GenerativeModel("models/gemini-1.5-flash")

    prompt = (
        f"Estoy en {ciudad}. Hace {temperatura}°C, está {condicion_clima}, con un viento de {viento} km/h "
        f"y una humedad del {humedad}%. ¿Qué ropa debería usar hoy? Respondé de forma breve y práctica."
    )

    try:
        print("\nGenerando consejo con IA...")
        respuesta = model.generate_content(prompt)
        print("Consejo de vestimenta personalizado:")
        print(respuesta.text)
    except Exception as e:
        print("Error generando el consejo:", e)

def consejo(usuario):
    print("A partir de qué información quiere recibir un consejo:")
    print("Opción 1: Última consulta realizada")
    print("Opción 2: Consulta especifica del historial")
    print("Opción 3: Realizar una nueva consulta")
    opcion = int(input("Elige una opcion: "))
    match opcion:
        case 1:

            try:
                #BUSCO EN EL HISTORIAL LA ÚLTIMA CONSULTA 
                with open(HISTORIAL_FILE, newline='', encoding='utf-8') as archivo:
                    lector = csv.reader(archivo)
                    consultas = [fila for fila in lector if fila and fila[0].lower() == usuario.lower()]
                
                #SI NO HAY CONSULTAS PREVIAS MENSAJE DE ERROR
                if not consultas:
                    print("No hay consultas previas tuyas en el historial.")
                    return

                ultima = consultas[-1]  # la última consulta 

                #SACO DE LA CONSULTA LOS DATOS QUE NECESITO 
                ciudad = ultima[1]
                temperatura = ultima[3]
                condicion = ultima[4]
                humedad = ultima[5]
                viento = ultima[6]

                #FUNCION DE OBTENER CONSEJO 
                obtener_consejo_ia_gemini(
                    api_key_gemini=api_key_gemini,
                    ciudad = ciudad,
                    temperatura=temperatura,
                    condicion_clima=condicion,
                    viento=viento,
                    humedad=humedad
                )

            except FileNotFoundError:
                print("No se encontró el archivo historial_global.csv")
            except Exception as e:
                print(f"Error inesperado al procesar el consejo IA: {e}")
        

        case 2:       

        #BUSCO EL HISTORIAL DEL USUARIO
        #SI HAY UNA 
        #SACO DE LA CONSULTA LOS DATOS QUE NECESITO 
        #FUNCION DE OBTENER CONSEJO 

            try:
                with open(HISTORIAL_FILE, newline='', encoding='utf-8') as archivo:
                    lector = csv.reader(archivo)
                    consultas = [fila for fila in lector if fila and (fila[0].lower() == usuario.lower()) ]
                    print(f"\nEste es tu historial de consultas:")
                    contador = 0
                    for fila in consultas:
                        contador+=1
                        print(f"\nConsulta {contador}: Usuario: {fila[0]}, Ciudad:{fila[1]}, Fecha y hora: {fila[2]}, Temperatura: {fila[3]} °C, Condición del clima: {fila[4]}, Humedad: {fila[5]}%, Viento: {fila[6]} m/s")
                    consulta_seleccionada = int(input("\nIndique a partir de cuál desea recibir el consejo: "))
                    consulta = consultas[consulta_seleccionada-1]
                    
                    #SACO DE LA CONSULTA LOS DATOS QUE NECESITO 
                    ciudad = consulta[1]
                    temperatura = consulta[3]
                    condicion = consulta[4]
                    humedad = consulta[5]
                    viento = consulta[6]
                    
                    obtener_consejo_ia_gemini(
                    api_key_gemini=api_key_gemini,
                    ciudad = ciudad,
                    temperatura=temperatura,
                    condicion_clima=condicion,
                    viento=viento,
                    humedad=humedad
                )
            
            except FileNotFoundError:
                print("No se encontró el archivo de historial. Asegúrate de haber realizado consultas previamente.")
       
       
        case 3:        
        #LLAMO A LA FUNCIÓN PARA GENERAR UNA NUEVA CONSULTA
        #BUSCO EN EL HISTORIAL LA ÚLTIMA CONSULTA 
        #SACO DE LA CONSULTA LOS DATOS QUE NECESITO 
        #FUNCION DE OBTENER CONSEJO 
            clima(usuario)
            try:
                #BUSCO EN EL HISTORIAL LA ÚLTIMA CONSULTA 
                with open(HISTORIAL_FILE, newline='', encoding='utf-8') as archivo:
                    lector = csv.reader(archivo)
                    consultas = [fila for fila in lector if fila and fila[0].lower() == usuario.lower()]
                
                #SI NO HAY CONSULTAS PREVIAS MENSAJE DE ERROR
                if not consultas:
                    print("No hay consultas previas tuyas en el historial.")
                    return

                ultima = consultas[-1]  # la última consulta 

                #SACO DE LA CONSULTA LOS DATOS QUE NECESITO 
                ciudad = ultima[1]
                temperatura = ultima[3]
                condicion = ultima[4]
                humedad = ultima[5]
                viento = ultima[6]

                #FUNCION DE OBTENER CONSEJO 
                obtener_consejo_ia_gemini(
                    api_key_gemini=api_key_gemini,
                    ciudad = ciudad,
                    temperatura=temperatura,
                    condicion_clima=condicion,
                    viento=viento,
                    humedad=humedad
                )

            except FileNotFoundError:
                print("No se encontró el archivo historial_global.csv")
            except Exception as e:
                print(f"Error inesperado al procesar el consejo IA: {e}")            


    