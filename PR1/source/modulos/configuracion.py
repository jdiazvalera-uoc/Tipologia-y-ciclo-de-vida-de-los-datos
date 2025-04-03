from selenium import webdriver
import undetected_chromedriver as uc
import random
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Para evitar que nos detectes usaremos una lista con diferentes agentes
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
]
def iniciar_driver():
    """
    Inicializa y configura el driver de Selenium con opciones personalizadas, que utilizaremos
    posteriormente para controlar el navegador.
    Salidas:
        - driver: WebDriver de Selenium que utilizamos para controlar el navegador.
    """
    # Creamos las opciones de Chrome y desactivamos la deteccion automatica, activamos el
    # modo incognito, desactivamos la GPU y el sandobox y le decimos que utilice la lista de agentes
    # previamente definidos.
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--incognito")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument(f"user-agent={random.choice(USER_AGENTS)}")
    # Inicializamos el driver de Chrome con las opciones configuradas
    driver = uc.Chrome(options=options)
    driver.maximize_window()
    return driver