# 🌦️ GuardiánClima ITBA

Es un proyecto de aplicación de consola desarrollado en el marco educativo del Hackatón de Tecnología ITBA 2025.
El programa permite consultar el clima actual de cualquier ciudad, guardar registros, visualizar estadísticas globales de uso, y obtener recomendaciones de vestimenta mediante IA
### Equipo de desarrollo

Allona, Ema;
Blanco, Malena;
Chaves Alvarez, Victoria Mia;
Hitters, Phimthananya (Zoe);
Payssé, Mia.

---

## Descripción general

GuardiánClima ITBA es un sistema educativo que permite:

- Consultar el clima actual de cualquier ciudad utilizando datos en tiempo real.
- Registrar y consultar historiales personales de búsquedas.
- Calcular estadísticas globales de uso.
- Obtener recomendaciones personalizadas de vestimenta mediante IA.
- Gestionar usuarios con validación avanzada de contraseñas.

> ⚠️‼️Advertencia de seguridad⚠️ Este proyecto fue diseñado como ejercicio pedagógico. No implementar en producción sin ajustes de seguridad.
Los usuarios y contraseñas son almacenados en un archivo CSV por motivos pedagógicos, por lo tanto, NO ofrece seguridad para aplicaciones reales.
En contextos profesionales se deberían implementar códigos de cifrado y técnicas de hashing con mayor complejidad para proteger las credenciales de los usuarios. 
NO utilice ninguna contraseña personal en está aplicación.

---

## Estructura del proyecto

GuardiánClima_ITBA/
│
├── main.py
├── menus.py        # Donde se encuentran el menú de acceso y el principal.
├── auth.py         # Donde se encuentra el proceso de registro de usuario, inicio de sesión y validación de contraseñas.
├── clima.py        # Donde se encuentran las funciones para obtener el clima.
├── historial_global.py  # Donde se encuentran las funciones para guardar el historial, verlo y obtener las estadísticas globales.
├── consejo_ia.py   # Donde se encuentra la función para obtener el consejo de IA.
├── acerca_de.py    # Donde se encuentra la información del programa.
├── .env
├── requirements.txt  # Paquetes a instalar.
├── usuarios_simulados.csv
└── historial_global.csv

- **usuarios_simulados.csv**: Almacena usuarios y contraseñas (simulado).
- **historial_global.csv**: Guarda todas las consultas realizadas.

---

## Cómo obtener las API Keys

### OpenWeatherMap:

1. Registrate en https://openweathermap.org/
2. Ingresá a tu cuenta → API Keys
3. Copiá la API Key.

#### 🔑 Google Gemini (Google AI Studio):

1. Registrate en https://aistudio.google.com/app/apikey
2. Generá una API Key de Gemini.
3. Copiá la clave.

> **Nota:** El modelo utilizado es `gemini-1.5-flash`.

---

## Configuración de APIs y variables de entorno

Para proteger las claves, las API Keys se almacenan en un archivo oculto `.env`.

### 1. Crear el archivo `.env` en la raíz del proyecto

En el mismo directorio donde están tus archivos `.py`, creá un archivo llamado:

.env

Sin espacios ni agregados, así tal cual como se encuentra.

### 2. Agregar tus API Keys dentro del archivo `.env`:

OWM_API_KEY=tu_clave_de_openweathermap
GEMINI_API_KEY=tu_clave_de_google_gemini

Agrega tus claves sin comillas ni espacios extra y con el formato `VARIABLE=valor`.

---

## Instalación y ejecución

1. Clonar el repositorio o descargar el código.

2. Instalar dependencias necesarias:

```bash
pip install -r requirements.txt

Dentro de la carpeta del programa, ejecutar la aplicación principal:
python main.py
``` 

> ⚠️‼️Advertencia de seguridad⚠️
No implementar en producción sin ajustes de seguridad.
Los usuarios y contraseñas son almacenados en texto plano sin cifrado, por lo tanto, NO ofrece seguridad para aplicaciones reales.
En contextos profesionales se deberían implementar códigos de cifrado y técnicas de hashing con mayor complejidad para proteger las credenciales de los usuarios. 
NO utilice ninguna contraseña personal real en está aplicación.

---

## Tecnologías utilizadas

Python 3.x
APIs externas:
OpenWeatherMap (clima)
Google Gemini (IA generativa)
Manejo de archivos CSV
Programación modular y validación de contraseñas segura (simulada)

## Estadísticas y gráficos

El archivo historial_global.csv registra automáticamente todas las consultas realizadas.
Este archivo puede abrirse en Excel, Google Sheets u otras herramientas para generar:
- Gráficos de barras: cantidad de consultas por ciudad.
- Gráficos de líneas: evolución de la temperatura en cada ciudad.
- Gráficos de torta: distribución de condiciones climáticas registradas.


# Equipo de desarrollo

Allona, Ema;
Blanco, Malena;
Chaves Alvarez, Victoria Mia;
Hitters, Phimthananya (Zoe);
Payssé, Mia.

Tecnología Admisión ITBA - 1C 2025

