# Menú de Acceso (Pre-Login)

# Bibliotecas importadas:
import csv
import re
import os
print("Directorio actual:", os.getcwd())        # Para que los nombres de usuario y contraseñas queden registrados en el archivo csv, el archibo debe estar abierto en la consola

# Funcion que permite agregar nuevo usuario al CSV

def guardar_usuario(username, password):
    with open("usuarios_simulados.csv", "a", newline='', encoding='utf-8') as archivo:      # Abre el archivo y registra en forma de tupla tanto nombre de usuario como contraseña
        escritor = csv.writer(archivo)
        escritor.writerow([username, password])

# Validación de contraseñas y sugerencias para que cumplan con los requisitos de seguridad

def validar_contraseña(password):
    errores = []                                                                # Almacena los errores en una lista      
    if len(password) < 12:
        errores.append("La contraseña debe tener al menos doce caractéres")                     # Criterio de seguridad: un largo mínimo
    if not re.search(r"[A-Z]", password):
        errores.append("La contraseña debe incluir al menos una letra mayúscula")               # Criterio de seguridad: diversidad de caracteres
    if not re.search(r"[a-z]", password):
        errores.append("La contraseña debe incluir al menos una letra minúscula")
    if not re.search(r"\d", password):
        errores.append("La contraseña debe incluir al menos un número")
    if not re.search(r"[!@#%^&*_+.;,:/]", password):
        errores.append("La contraseña debe incluir al menos un símbolo especial !@%^&*_+.;,:/") # Muestra lo que el sistema considera un "simbolo especial" para mayor claridad

    if errores:
        requisitos = (
            "Requisitos mínimos de seguridad: " +
            "\n * ".join(errores)                                   # Pone dentro de la variable la lista de errores identificados
        )
        sugerencia = "\nTe sugerimos que crees una contraseña única. La utilizació de palabras aleatorias tambien fortalece tu contraseña."
        return False, requisitos + sugerencia                       # Imprime los requisitos (lista de errores) y una sugerencia para que la contraseña sea más fuerte
    else:
        return True, "Contraseña válida."

# Carga los usuarios desde usuarios_simulados.csv en un diccionario

def cargar_usuarios():
    usuarios = {}
    try:                                                                                # Utilizamos el try para poder accionar en caso de posible error
        with open("usuarios_simulados.csv", newline='', encoding='utf-8') as archivo:   # Abrimos el archivo como lector
            lector = csv.reader(archivo)
            for fila in lector:
                if len(fila) == 2:
                    usuario, contraseña = fila                          # Llama usuario y contraseña a cada elemento correspondiente de la tupla 
                    usuarios[usuario] = contraseña                      # A cada usuario le asigna su correspondiente contraseña
    except FileNotFoundError:                            # Si el archivo no existe, devolvemos un diccionario vacío
        pass
    return usuarios

#Permite registrar un nuevo usuario, validando nombre y contraseña

def registrar_usuario():
    usuarios = cargar_usuarios()
    
    print("\n=== REGISTRO DE NUEVO USUARIO ===")
    
    while True:
        username = input("Elija un nombre de usuario: ").strip()            # Le pide a quien intenta registrarse que elija su nombre de usuario
        if username in usuarios:
            print("Este nombre de usuario ya existe. Pruebe con otro.")     # Si ese nombre de usuario ya fue utilizado anteriormente y ya esta registrado, notifica a la persona y le permite ingresar otro nombre de usuario
        elif username == "":
            print("El nombre de usuario no puede estar vacío.")             # En caso de que la persona no complete nada, aclara que no puede dejar vacio el campo de nombre de usuario
        else:
            break

    while True:
        password = input("Ingrese una contraseña segura: ").strip()
        valido, mensaje = validar_contraseña(password)                  # Llama a la función validar contraseña para fijarse que cumpla con los requisitos minimos de seguridad
        print(mensaje)
        if valido:
            guardar_usuario(username, password)                         # Si la contraseña cumple con los requisitos, se llama a la función guardar_usuario y se registran ese nombre de usuario y contraseña en el archivo csv
            print(f"\n¡Registro exitoso! Bienvenido/a, {username}.")
            return username                                             # Auto-login
        else:
            intentar_otra = input("\n¿Quieres intentar con otra contraseña? (si/no): ").strip().lower()     # Si la contraseña no cumple, se le ofrece al usuario intentar con una nueva contraseña luego de notificarle los requisitos de la mimsa
            if intentar_otra == 'no':
                print("Registro cancelado.")
                return None
            

# Inicio de sesión
def iniciar_sesion():
    usuarios = cargar_usuarios()        # Llama a la función cargar_usuarios dentro de la variable usuarios
    
    while True:
        print("\n=== INICIO DE SESIÓN ===")
        username = input("Nombre de usuario: ").strip() # Ingresa nombre de usuario
        password = input("Contraseña: ").strip()    # Ingresa contraseña

        if username not in usuarios:
            print(f"\nEl usuario '{username}' no existe.") 
            opcion = input("¿Deseás registrarte con este nombre? (si/no): ").strip().lower()    # Si el nombre de usuario con el que intenta iniciar sesión no existe, se le ofrece registrarse volviendo al menu de acceso
            if opcion == 'si':
                return None                                                             # Volver al menu de acceso, que ofrecerá registro
            else:
                continuar = input("¿Querés intentar iniciar sesión con otro usuario? (si/no): ").strip().lower() # En el caso que se desee iniciar sesión con otro usuario, se lo lleva de nuevo a iniciar sesión, sino lo devuelve al menú de acceso
                if continuar == 'no':
                    print("Volviendo al menú de acceso...")
                    return None
        else:
            if usuarios[username] == password:
                print(f"\n¡Bienvenido, {username}! Inicio de sesión exitoso.")      # Si ambos usuario y contraseña son correctos se lo lleva al menú principal
                #MENU PRINCIPAL
                return username
            else:
                print("\nContraseña incorrecta.")
                reintentar = input("¿Querés volver a intentarlo? (si/no): ").strip().lower()    # En caso de contraseña incorrecta, se le permite al usuario volver a intentar o volver al menú de acceso
                if reintentar == 'no':
                    print("Volviendo al menú de acceso...")
                    return None


# Menú pre-Login con opciones

def mostrar_menu_acceso(): # Vista Menú Principal Pre-Login
    while True:
        print("=== GUARDIÁNCLIMA ITBA ===")
        print("Menú:")
        print("1. Iniciar Sesión")                  # Opciones del menú de acceso
        print("2. Registrar Nuevo Usuario")
        print("3. Salir")

        opcion = input("Ingrese una opción (1-3):").strip()     # El usuario elige qué acción desea realizar

        if opcion == "1":
            usuario_logueado = iniciar_sesion()     # En el caso de que desee iniciar sesión, se llama a la función correspondiente
            if usuario_logueado:
                menu_principal(usuario_logueado)  # Si el inicio de sesión es existoso, se lo lleva al usuario al Menú Principal
        elif opcion == "2":
            usuario_logueado = registrar_usuario()       # En el caso de que desee registrarse, se llama a la función correspondiente
            if usuario_logueado:
                menu_principal(usuario_logueado)  # Auto-login tras registro exitoso
        elif opcion == "3":
            print("Gracias por usar GuardiánClima ITBA. ¡Hasta pronto!")         # En el caso de que desee salir, se cierra el programa
            break
        else:
            print("Opción inválida. Por favor, elegí 1, 2 o 3.")        # En el caso de que se ingrese una opción inválida, se le aclara al usuario y se le solicita ingresar alguna de las opciones válidas

def menu_principal(usuario):                                    # Aca va en realidad la función que haya creado Vicki para el Menú Principal
    print(f"\n¡Bienvenido/a {usuario} al Menú Principal!")

if __name__ == "__main__":      # Esto lo puse para correr el programa, quizas haya que sacarlo después
    mostrar_menu_acceso()