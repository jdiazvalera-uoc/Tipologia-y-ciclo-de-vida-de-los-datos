from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def navegar_a_pagina(driver, url):
    """
    Navegamos a la ulr deseada, se abre la pagina en nuestro buscador y aceptamos las cookies
    si es necesario.

    Entrdas: 
        - driver: WebDriver de Selenium que utilizamos para controlar el navegador.
        - url: Direccion web.
    """
    # Accedemos al URL
    driver.get(url)
    try:
        # Esperamos a que aparezca el mensaje de las Cookies
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[id^='sp_message_iframe_']"))
        )
        boton_cookies = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept & continue')]"))
        )
        # Y las aceptamos
        boton_cookies.click()
        print("Cookies aceptadas.")
        driver.switch_to.default_content()
    except TimeoutException:
        print("Botón de cookies no aceptado o aceptado manualmente.")


def buscar_siguiente_tabla(driver):
    """
    Buscar del botón "A la página siguiente".

    Entrdas: 
        - driver: WebDriver de Selenium que utilizamos para controlar el navegador.
    Salidas:
        - siguiente: Devuelve el atributo 'href' del boton, Si no se encuentra, devuelve None.
    """
    try:
        # Busca el botón de siguiente página y obtiene su enlace (href)
        siguiente = driver.find_element(By.CSS_SELECTOR, "li.tm-pagination__list-item--icon-next-page a.tm-pagination__link").get_attribute("href")
        return siguiente
    except Exception:
        print(f" Error obteniendo el enlace 'Siguiente'. Finalizando...")
        return None 
    
  
def filtro_UEFA (driver):
    """
    Aplicamos el filtro para mostrar únicamente jugadores de la UEFA.
    En el filtro de Continen seleccionamos la opcion 6 que es UEFA.
    Despues pulsamos el boton 'Mostrar' para que se actualice
    
    Entradas:
        - driver: WebDriver de Selenium que utilizamos para controlar el navegador.
    Salidas:

        - Devuelve True si se aplicó correctamente el filtro, o False en caso de error.
    """
    try:
        # Esperamos a que aparezca el selector de continente 
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "kontinent_id"))
        )
        filtro = driver.find_element(By.NAME, "kontinent_id")
        # Scroleamos para tener el selector en la pantalla
        driver.execute_script("arguments[0].scrollIntoView(true);", filtro)
        time.sleep(1)
        
        # Seleccionar la opción UEFA (valor "6") 
        driver.execute_script("arguments[0].value = '6';", filtro)
        driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", filtro)
        time.sleep(2) 
        
        # Espera a que el botón 'Show' esté presente e interactuable
        boton_show = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and contains(@value, 'Show')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", boton_show)
        time.sleep(1)
        
        # Ocultar el campo de búsqueda que interfiere (si existe)
        try:
            driver.execute_script("document.querySelector('input.tm-header__input--search-field').style.display='none';")
        except Exception as e:
            print("No se pudo ocultar el campo de búsqueda: ", e)
        
        # Usar JavaScript para hacer clic en el botón 'Show'
        driver.execute_script("arguments[0].click();", boton_show)
        time.sleep(3)  
        
        # Esperar a que se cargue la tabla de jugadores
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table.items"))
        )
        return True
    except Exception as e:
        print(f"Error al aplicar el filtro UEFA: {e}")
        return False
    
def cambiar_a_vista_ampliada(driver):
    """
    Cambia la vista de la página a 'Detailed', pulsando el boton 'Deatailed' que nos abrira
    la pestaña.

    Entradas:
        - driver: WebDriver de Selenium que utilizamos para controlar el navegador.
    Salidas:
        - Devuelve True si se accedio correctamente a la pestaña, o False en caso de error.
    """
    try:
        # Espera a que el elemento Detailed sea clickeable
        detailed_view = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Detailed"]/ancestor::a'))
        )
        # Desplazar el elemento a la vista
        driver.execute_script("arguments[0].scrollIntoView(true);", detailed_view)
        time.sleep(1)
        try:
            driver.execute_script("document.querySelector('div.domain-note').style.display='none';")
        except Exception as ex:
            print("No se pudo ocultar el elemento interferente:", ex)
        
        # Forzar el clic mediante JavaScript
        driver.execute_script("arguments[0].click();", detailed_view)
        time.sleep(3)
        return True
    except TimeoutException:
        print("error")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False