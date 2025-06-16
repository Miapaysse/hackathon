# Importo las funciones que voy a usar de otros archivos
from clima import clima 
from historial_global import historial_usuario, estadisticas_globales
from consejo_ia import consejo
from acerca_de import mostrar_info
from auth import iniciar_sesion, registrar_usuario


def menu_acceso(): # Vista Menú Principal Pre-Login
    while True:
        print("=== GUARDIÁNCLIMA ITBA ===")
        print("Menú:")
        print("1. Iniciar Sesión")                  # Opciones del menú de acceso
        print("2. Registrar Nuevo Usuario")
        print("3. Salir")

        opcion = input("Ingrese una opción (1-3): ").strip()     # El usuario elige qué acción desea realizar. No lo defino como formato int para que en caso de que el usuario ingrese otro caracter no se pare el programa.

        if opcion == "1":
            usuario_logueado = iniciar_sesion()     # En el caso de que desee iniciar sesión, se llama a la función correspondiente
            if usuario_logueado is not None:
                print(f"\n¡Bienvenido/a {usuario_logueado} al Menú Principal!")
                menu_principal(usuario_logueado)  # Si el inicio de sesión es existoso, se lo lleva al usuario al Menú Principal
        elif opcion == "2":
            usuario_logueado = registrar_usuario()      # En el caso de que desee registrarse, se llama a la función correspondiente
            if usuario_logueado is not None:
                print(f"\n¡Bienvenido/a {usuario_logueado} al Menú Principal!") 
                menu_principal(usuario_logueado)  # Auto-login tras registro exitoso
        elif opcion == "3":
            print("Gracias por usar GuardiánClima ITBA. ¡Hasta pronto!")         # En el caso de que desee salir, se cierra el programa
            exit()
        else:
            print("Opción inválida. Por favor, elegí 1, 2 o 3.")  




#Armo una función típica de menú igual que la de acceso y defino funcines para cada opción.

def menu_principal(usuario):
     # Bucle para mostrar el menú principal repetidamente hasta que el usuario decida salir y se rompa el bucle. 
     while True: 
        print("\n=== GuardiánClima ITBA ===")
        print("\n=== Menú Principal ===") 
        print("1. Consultar clima actual.")
        print("2. Ver historial personal.")
        print("3. Estadísticas globales de uso.")
        print("4. Consejo de vestimenta (IA).")
        print("5. Acerca de GuardiánClima ITBA.")
        print("6. Cerrar Sesión")

        opcion = input("Selecciona una opción (1-6): ").strip()  # Le pido al usuario que elija una opción del menú que lleva a que se ejecute la función correspondiente.

        if opcion == "1":
            clima(usuario)
        elif opcion == "2":
            historial_usuario(usuario)
        elif opcion == "3":
            estadisticas_globales()
        elif opcion == "4":
            consejo(usuario)
        elif opcion == "5":
            mostrar_info()
        elif opcion == "6":
            print("Gracias por usar GuardiánClima ITBA. ¡Hasta pronto!")
            menu_acceso()
            break
        else:
            print("Opción inválida. Intenta de nuevo.")




