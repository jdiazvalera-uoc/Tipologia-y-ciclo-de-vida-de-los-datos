import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

from modulos.configuracion import iniciar_driver
from modulos.extraer import extraer_jugadores
from modulos.navegacion import navegar_a_pagina,buscar_siguiente_tabla, filtro_UEFA, cambiar_a_vista_ampliada

# Definimos la página a la que vamos a acceder y desde donde empezaremos el Scraping
URL = "https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop"
def main():
    driver =  None
    try:
        # Se confirua y se inicializa el driver
        driver = iniciar_driver()
        # Mediante el driver accedemos a la URL definida
        navegar_a_pagina(driver, URL)
        jugadores_mas_valorados = []
        # Escogemos la opción UEFA (6) dentro del filtro Continen y pulsamos el boton show
        if filtro_UEFA(driver):
            print("Filtro UEFA aplicado correctamente.")
        else:
            print("No se pudo aplicar el filtro UEFA.")
            driver.quit()
            return
        # Accedemos a la pestaña Detailed
        if cambiar_a_vista_ampliada(driver):
            print("Se ha accedido a la pestaña detailed correctamente.")
        else:
            print("No se pudo acceder a detailed.")
            driver.quit()
            return
        while True:
            # Simulamos comportamiento humano esperando un poco y extraemos los datos de la tabla
            time.sleep(random.uniform(3, 6))
            jugadores = extraer_jugadores(driver)
            jugadores_mas_valorados.extend(jugadores)
            time.sleep(3)
            # Una vex extraido todo pulsamos el boton de siguiente página para ir a la siguiente tabla
            siguiente_tabla = buscar_siguiente_tabla(driver)
            # Cuando no haya más tablas cerramos el navegador
            if siguiente_tabla:
                print(f"Navegando a la siguiente página: {siguiente_tabla}")
                driver.get(siguiente_tabla)
                
            else:
                print("No hay más tablas. Finalizando scraping.")
                break 
        # Y con todos los datos extraidos generamos un archivo CSV y finaliza el Web Scraping
        crear_csv(jugadores_mas_valorados, "transfermarkt_top_players")
        print("Scraping completado, datos guardados en 'transfermarkt_top_players.csv'.")
    except Exception as e:
        print(f'Error: {e}')
    finally:
        if driver:
            driver.quit()
            del driver 
            print('Navegador cerrado')
    
    
def crear_csv(datos, archivo):
    """
    Generamos un archivo CSV para guardar los datos extraídos.

    Entradas:
        - datos: Lista de jugadores extraídos del scraping.
        - archivo: Nombre del archivo CSV.
    Salidas:
        Genera el archivo csv.
    """
    df = pd.DataFrame(datos)
    df.to_csv(f"{archivo}.csv", index=False)
    print(f"dataset creado {archivo}.csv")

if __name__ == "__main__":
    main()