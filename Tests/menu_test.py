#Importo las librerías que voy a necesitar 
import requests 
import json
import datetime
import csv
from collections import Counter 
import statistics

HISTORIAL_FILE = "historial_global.csv" #Llamo al archivo donde voy a guardar el historial de consultas
API_KEY = 'faf588bee287e1e62aa3c55abd236220'  #Clave de API de OpenWeatherMap. Tengo que moverla de aca.!!!

from clima import clima, historial_usuario, estadisticas_globales
from consejo_ia import consejo
from acerca_de import mostrar_info

#Armo una función típica de menú igual que la de acceso y defino funcines para cada opción.

def menu_principal():
     #Bucle para mostrar el menú principal repetidamente hasta que el usuario decida salir y se rompa el bucle. 
     while True: 
        print("\n=== Menú Principal - GuardiánClima ITBA ===")
        print("1. Consultar clima actual.")
        print("2. Ver historial personal.")
        print("3. Estadísticas globales de uso.")
        print("4. Consejo de vestimenta (IA).")
        print("5. Acerca de GuardiánClima ITBA.")
        print("6. Salir")

        opcion = input("Selecciona una opción: ") #Le pido al usuario que elija una opción del menú que lleva a que se ejecute la fucnióncorrespondiente.

        if opcion == "1":
            clima()
        elif opcion == "2":
            historial_usuario()
        elif opcion == "3":
            estadisticas_globales()
        elif opcion == "4":
            consejo()
        elif opcion == "5":
            mostrar_info()
        elif opcion == "6":
            print("¡Nos vemos!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")




menu_principal()