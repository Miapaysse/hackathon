# Acerca de GuardianClima ITBA.

def mostrar_info():
    print("\n=== Acerca de GuardianClima ITBA🌤️ ===\n")
    print("GuardianClima ITBA es una aplicación desarrollada en un contexto educativo.")
    print("Permite consultar el clima actual de cualquier ciudad, guardar registros, ")
    print("visualizar estadísticas globales de uso, y obtener recomendaciones de vestimenta mediante IA.")
    
    print("\nFuncionalidades principales: login simulado, validación de contraseñas, clima en tiempo real (OpenWeatherMap), IA para vestimenta (Google Gemini).")
    
    print("\n- Menú de Acceso (Pre-Login): Al iniciar la aplicación, el usuario ingresa al Menú de Acceso, donde tiene tres opciones:")
    print("  * 1. Iniciar sesión: Permite al usuario autenticarse con su nombre y contraseña previamente registrados.")
    print("  * 2. Registrar nuevo usuario: Permite crear un nuevo usuario, validando que la contraseña sigua criterios de seguridad.")
    print("  * 3. Salir: Finaliza la ejecución del programa.")
    
    print("\n‼️Advertencia de seguridad!!: Este sistema es un simulador educativo. ")
    print(" Los usuarios y contraseñas son almacenados en un archivo CSV por motivos pedagógicos, por lo tanto, NO ofrece seguridad para aplicaciones reales.")
    print(" En contextos profesionales se deberían implementar códigos de cifrado y técnicas de hashing con mayor complejidad para proteger las credenciales de los usuarios.") 
    print(" NO utilice ninguna contraseña personal en está aplicación.\n")
    
    print("- Menú Principal (Post-Login): Luego de iniciar sesión exitosamente, el usuario accede al menú principal, donde dispone de las siguientes opciones:")
    print("  * 1. Consultar clima actual: El usuario ingresa una ciudad y obtiene el clima actual consultando a la API de OpenWeatherMap. Los resultados se guardan automáticamente en el historial global.")
    print("  * 2. Ver historial personal: Permite al usuario consultar su historial de búsquedas anteriores, filtrado por ciudad.")
    print("  * 3. Estadísticas globales de uso: Muestra estadísticas calculadas a partir del historial de consultas de todos los usuarios: ciudad más consultada, cantidad total de consultas y temperatura promedio. ")
    print("  * 4. Consejo de Vestimenta (IA): Utiliza la API de Gemini para generar sugerencias de vestimenta personalizadas según la consulta que desee el usuario.")
    print("  * 5. Acerca de GuardiánClima ITBA: Presenta descripción general de la aplicacion.")
    print("  * 6. Cerrar sesión: Finalizando la sesión actual y vuelve al Menú de Acceso.")
   
    print("\n ⚙️Funcionamiento interno.")
    print("- Creación de usuarios y validación de contraseñas: El registro se realiza mediante el ingreso de un nombre de usuario único y contraseña. Las contraseñas son validadas de manera estricta antes de ser aceptadas.")
    print("Los criterios son: Minimo 12 caracteres, al menos: una mayúscula, una minúscula, un número, un caracter especial. En caso de no cumplir se muestra el listado de requisitos y sugerencias.")
    print("Si la contraseña es válida, el usuario queda automaticamente registrado y logueado.")
    
    print("- Obtención de datos climáticos y guardado en el historial: La consulta se realiza mediante la API de OpenWeatherMap cuyos parametros son:")
    print("ciudad (ingresada por el usuario), unidades metricas, idioma español.")
    print("Los datos obtenidos incluyen: temperatura, sensacion térmica, humedad, condiciones climáticas y velocidad del viento. Cada consulta es registrada automaticamente en el archivo CSV junto con usuario, ciudad, fecha y hora, y los datos anteriormente mencionados.")
    
    print("- 📊Estadísticas globales de uso: El archivo CSV se procesa para calcular:")
    print("Total de consultas registradas, Ciudad más consultada y temperatura promedio.")
    print("El archivo queda preparado para ser exportado y con herramientas externas poder preparar diferentes tipos de gráficos.")
    
    print("- Consulta de vestimenta mediante Inteligencia Artificial: El módulo de IA permite que el usuario obtenga un consejo de vestimenta personalizado.")
    print("El usuario puede utilizar la última consulta, seleccionar alguna especifica de su historial o realizar una consulta en el momento.")
    print("Los datos de la consulta se envían en un prompt a Gemini que genera una recomendacion de vestimenta para el usuario.")
    
    print("\n!! Todas las interacciones con las API se realizan con APIKEY seguras cargadas en un archivo .env")
    
    print("\nAspectos técnicos destacados:")
    print("☼ Programación modular utilizando funciones para cada funciónalidad del programa.")
    print("☼ Manejo de archivos CSV para el almacenamiento de datos.")
    print("☼ Integracion de APIs externas: OpenWeatherMap (datos climáticos) y Google Gemini (IA generativa).")
    print("☼ Manejo de errores frente a problemas de conexion, datos invalidos o archivos inexistentes.")
    print("☼ Validación de contraseñas seguras con diferentes criterios.")
    
    print("\nDesarrollado por: Allona, Ema; Blanco, Malena; Chaves Alvarez, Victoria; Hitters, Phimtanaya (Zoe) y Payssé, Mia ")
    print("Grupo: Las Chicas Superprogramadoras. ")
    
    print("Tecnología Admisión ITBA - 1C 2025")



