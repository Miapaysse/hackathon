# Consejo de vestimenta de IA

#Importo las librerías que voy a necesitar 

import os
import csv
from dotenv import load_dotenv
import google.generativeai as genai

# Importo la función clima para utilizarla en el código
from clima import clima

HISTORIAL_FILE = "historial_global.csv" # Llamo al archivo del historial de consultas
CAMPOS =  ["usuario", "ciudad", "fecha", "temperatura", "condicion", "humedad", "viento"]    # Campos de los diccionarios guardados en el historial

load_dotenv()
api_key_gemini = os.getenv("GEMINI_API_KEY") # Clave de API de IA  


def obtener_consejo_ia_gemini(api_key_gemini, ciudad, temperatura, condicion_clima, viento, humedad):
    if not api_key_gemini:
        print("Error: No se encontró la clave de API de Gemini en el archivo .env.")
        return
    
    genai.configure(api_key=api_key_gemini)
    model = genai.GenerativeModel("models/gemini-1.5-flash")

    prompt = (
        f"Estoy en {ciudad}. La temperatura es de {temperatura}°C, el clima es {condicion_clima}, con un viento de {viento} km/h "
        f"y una humedad del {humedad}%. ¿Cómo debería vestirme hoy? Respondé de forma breve y práctica."
    )

    try:
        print("\nGenerando consejo con IA...")
        respuesta = model.generate_content(prompt)
        print("Consejo de vestimenta personalizado:")
        print(respuesta.text)
    except Exception as e:
         print(f"Error inesperado al procesar el consejo IA: {e}")



def obtener_ultima_consulta(usuario):
    try: # Busco en el historial la última consulta 
        with open(HISTORIAL_FILE, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            consultas = [fila for fila in lector if fila and fila["usuario"].lower() == usuario.lower()]
            if consultas:
                return consultas[-1]
            else:
                print("No hay consultas previas tuyas en el historial.")    # Si no hay consultas previas realizadas envia un mensaje de error
                return None 
    except FileNotFoundError:
        print("No se encontró el archivo historial_global.csv")
        return None
        


def extraer_datos_de_consulta(consulta):
     # Obtengo de la consulta los datos que necesito
    ciudad = consulta["ciudad"]
    temperatura = consulta["temperatura"]
    condicion = consulta["condicion"]
    humedad = consulta["humedad"]
    viento = consulta["viento"]

    return ciudad, temperatura, condicion, humedad, viento



def procesar_consulta_y_obtener_consejo(consulta):
    ciudad, temperatura, condicion, humedad, viento = extraer_datos_de_consulta(consulta)        # Obtengo de la consulta los datos necesarios 
    obtener_consejo_ia_gemini(api_key_gemini, ciudad, temperatura, condicion, viento, humedad)    # Llamo a la función para obtener el consejo con la úlitima consulta 
            


def consejo(usuario):
    print("\n === CONSEJO DE VESTIMENTA CON IA ===\n")
    print("A partir de qué información quiere recibir el consejo de vestimenta:")
    print("Opción 1: Última consulta realizada")
    print("Opción 2: Consulta especifica del historial")
    print("Opción 3: Realizar una nueva consulta")
    
    while True:
        try:
            opcion = int(input("Elige una opción (1-3): ").strip())
            if opcion not in [1, 2, 3]:
                print("Por favor, ingrese un número válido (1, 2 o 3).")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido (1, 2 o 3).")
    
    match opcion:
        case 1:
            ultima_consulta = obtener_ultima_consulta(usuario)
            if not ultima_consulta:
                return
            procesar_consulta_y_obtener_consejo(ultima_consulta)

        case 2:   # Busco consulta en el historial del usuario
            try:
                with open(HISTORIAL_FILE, newline='', encoding='utf-8') as archivo:
                    lector = csv.DictReader(archivo)
                    consultas = [fila for fila in lector if fila and (fila["usuario"].lower() == usuario.lower()) ]
                    print(f"\nEste es tu historial de consultas:")
                    
                    if not consultas:
                        print("No hay historial tuyo registrado.")    # Si no hay consultas en el historial del usuario devuelve un mensaje
                        return
                        
                    contador = 0    # Inicializo un contador de consultas para numerarlas SI HAY UNA 
        
                    for fila in consultas:
                        contador+=1 
                        print(f"\nConsulta {contador}: Usuario: {fila["usuario"]}, Ciudad:{fila["ciudad"]}, Fecha y hora: {fila["fecha"]}, Temperatura: {float(fila["temperatura"]):.2f} °C, Condición del clima: {fila["condicion"]}, Humedad: {fila["humedad"]}%, Viento: {float(fila["viento"]):.2f} km/h")
                    
                    while True:
                        try:
                            consulta_seleccionada = int(input("\nIndique a partir de cuál número de consulta desea recibir el consejo: ").strip())
                            if 1 <= consulta_seleccionada <= len(consultas):
                                break
                            else:
                                print("Número fuera de rango. Ingrese un número válido.")
                        except ValueError:
                                print("Por favor, ingrese un número válido.")
                    
                    consulta = consultas[consulta_seleccionada - 1]
                    procesar_consulta_y_obtener_consejo(consulta)

            except FileNotFoundError:
                print("No se encontró el archivo de historial. Asegúrate de haber realizado consultas previamente.")

    
        case 3:        
            clima(usuario)    # Llamo a la funcion clima para poder generar una nueva consulta
            ultima_consulta = obtener_ultima_consulta(usuario)    # Busco en el historial la última consulta hecha por el ususario.
            if not ultima_consulta:
                print("No hay consultas registradas aún.")
                return
            procesar_consulta_y_obtener_consejo(ultima_consulta)
