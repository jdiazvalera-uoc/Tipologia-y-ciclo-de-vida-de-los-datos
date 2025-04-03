# README

Repositorio que contiene todos los archivos para la práctica 1 de la asignatura Tipología y Ciclo de Vida de los Datos del Máster Universitario de Ciencia de Datos de la UOC.

## Alumnos:
- Josep Maria Díaz Valera  
- Enrique Arenaza Aguirre

## Descripción:
Este script de Python realiza Web Scraping sobre el sitio web Transfermarkt para recopilar información sobre los jugadores con mayor valor de mercado del continente europeo (UEFA). Utiliza Selenium y undetected_chromedriver para automatizar la navegación y evitar bloqueos. El objetivo final es generar un dataset en formato CSV que permita realizar análisis futbolísticos orientados al scouting, predicción de talento y toma de decisiones basada en estadísticas.
## Estructura del proyecto

PR1/
├── source/
│   ├── main.py          
│   └── modulos/              
│       ├── configuracion.py
│       ├── navegacion.py
│       └── extraer.py
├── dataset/
│   └── transfermarkt_top_players.csv
├── doi.txt            
├── requirements.txt        
└── README.md        
## Dependencies:
- Python 3.x  
- pandas  
- selenium  
- undetected_chromedriver  
- beautifulsoup4  

## Instalación:
Instala los paquetes necesarios ejecutando:
$ pip install -r requirements.txt

## Estructura del código:

1. `configuracion.py`: Inicializa el navegador con configuraciones avanzadas para evitar detección, incluyendo rotación de user agents, navegación en modo incógnito, etc.
2. `navegacion.py`: Se encarga de abrir la web de Transfermarkt, aceptar cookies, aplicar filtros (UEFA), cambiar a vista detallada y detectar la navegación entre páginas.
3. `extraer.py`: Contiene la lógica para hacer scroll, parsear la tabla de jugadores con BeautifulSoup y recolectar los datos más relevantes (edad, nacionalidad, club, goles, asistencias, tarjetas, sustituciones, etc.).
4. `main.py`: Ejecuta todas las funciones anteriores en el orden necesario, gestiona el flujo del scraping y guarda el resultado final en un CSV llamado `transfermarkt_top_players.csv`.

## Uso:
Ejecuta el script principal desde la terminal:
$ python main.py

Esto lanzará el scraping sobre las primeras 20 páginas del ranking de jugadores más valiosos de Europa y generará el dataset con los resultados obtenidos.

## Notas:
- El scraping se realiza respetando el archivo `robots.txt` de Transfermarkt.
- Se han incorporado buenas prácticas como pausas aleatorias entre acciones y ocultamiento de elementos que interfieren con la navegación.
- El proyecto incluye modularidad total: cada bloque de código (configuración, navegación, extracción) se encuentra separado y reutilizable.
- Para el correcto funcionamiento del script se debe de tener la última versiona ctuaizada del navegador
Chrome.
