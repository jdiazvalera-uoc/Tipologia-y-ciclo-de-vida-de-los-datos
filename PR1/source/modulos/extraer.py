from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import random
import time


def hacer_scroll(driver):
    """
    Realiza un desplazamiento automático (scroll) por la página.

    Entrdas: 
        - driver: WebDriver de Selenium que utilizamos para controlar el navegador.
    """
    # Guardamos la altura total del documento para conocer hasta dóndedebemos de scrollear
    altura_total = driver.execute_script("return document.body.scrollHeight")
    # Iteramos y scrolleamos mediante el Javascript
    for scroll in range(0, altura_total, 700):
        driver.execute_script(f"window.scrollTo(0, {scroll});")
        time.sleep(random.uniform(2, 4))

def extraer_jugadores(driver):
    """
    Extrae la información de los jugadores de la tabla de estadísticas de la página web. Para ello, 
    espera hasta que la tabla de jugadores esté presente en la página.Luego scrolleamos y usando
    BeautifulSoup para analiza el contenido de la página y extrae los datos de cada jugador.

    Entradas:
        - driver: Instancia del navegador controlado por Selenium.

    Salidas:
        - jugadores: Una lista de diccionarios con la información de cada jugador.
    """
    # Espera hasta que el elemento de la tabla con la clase "items" este listo
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table.items"))
    )
    # Realiza el scroll para que se cargue todo el contenido de la página
    hacer_scroll(driver)
    time.sleep(random.uniform(3, 5)) 
    # Creamos un objeto con toda l informacion del codigo fuente
    soup = BeautifulSoup(driver.page_source, "html.parser")
    # Buscamos las filas con informacion de los jugadores
    players = soup.find_all('tr', {'class': ['odd', 'even']})
    # Extraemos los datos necesarios
    PlayersList = [player.find_all('td', {'class': 'hauptlink'})[0].text.strip() for player in players]
    AgeList = [player.find_all('td', {'class': 'zentriert'})[1].text.strip() for player in players]

    NationalityList = [
        player.find_all("td", {"class": "zentriert"})[2].find("img")["title"].strip()
        if player.find_all("td", {"class": "zentriert"})[2].find("img") else "N/A"
        for player in players
    ]

    ClubList = [
        player.find_all("td", {"class": "zentriert"})[3].find("a")["title"].strip()
        if player.find_all("td", {"class": "zentriert"})[3].find("a") else "N/A"
        for player in players
    ]

    PlayerValueList = [player.find('td', {'class': 'rechts hauptlink'}).text.strip() for player in players]

    LineupList = [
        player.find_all("td", {"class": "zentriert"})[4].text.strip()
        if player.find_all("td", {"class": "zentriert"})[4] else "N/A"
        for player in players
    ]

    GoalsList = [
        player.find_all("td", {"class": "zentriert"})[5].text.strip()
        if player.find_all("td", {"class": "zentriert"})[5] else "N/A"
        for player in players
    ]
    AutoGoalsList = [
        player.find_all("td", {"class": "zentriert"})[6].text.strip()
        if player.find_all("td", {"class": "zentriert"})[6] else "N/A"
        for player in players
    ]

    AssistsList = [
        player.find_all("td", {"class": "zentriert"})[7].text.strip()
        if player.find_all("td", {"class": "zentriert"})[7] else "N/A"
        for player in players
    ]

    YellowcardsList = [
        player.find_all("td", {"class": "zentriert"})[8].text.strip()
        if player.find_all("td", {"class": "zentriert"})[8] else "N/A"
        for player in players
    ]  

    DoubleYellowcardsList = [
        player.find_all("td", {"class": "zentriert"})[9].text.strip()
        if player.find_all("td", {"class": "zentriert"})[9] else "N/A"
        for player in players
    ]
    
    RedcardsList = [
        player.find_all("td", {"class": "zentriert"})[10].text.strip()
        if player.find_all("td", {"class": "zentriert"})[10] else "N/A"
        for player in players
    ]    

    SubInList = [
        player.find_all("td", {"class": "zentriert"})[11].text.strip()
        if player.find_all("td", {"class": "zentriert"})[11] else "N/A"
        for player in players
    ]
    
    SubOutList = [
        player.find_all("td", {"class": "zentriert"})[12].text.strip()
        if player.find_all("td", {"class": "zentriert"})[12] else "N/A"
        for player in players
    ]                 
    # Construir lista de diccionarios con todos los datos recolectados
    jugadores = []
    for i in range(len(PlayersList)):
        jugadores.append({
            "Nombre": PlayersList[i] if i < len(PlayersList) else "N/A",
            "Edad": AgeList[i] if i < len(AgeList) else "N/A",
            "Nacionalidad": NationalityList[i] if i < len(NationalityList) else "N/A",
            "Club": ClubList[i] if i < len(ClubList) else "N/A",
            "Valor de Mercado": PlayerValueList[i] if i < len(PlayerValueList) else "N/A",
            "Titular": LineupList[i] if i < len(LineupList) else "N/A",
            "Goles": GoalsList[i] if i < len(GoalsList) else "N/A",
            "Autogoles": AutoGoalsList[i] if i < len(AutoGoalsList) else "N/A",
            "Asistencias": AssistsList[i] if i < len(AssistsList) else "N/A",
            "Amarillas": YellowcardsList[i] if i < len(YellowcardsList) else "N/A",
            "Doble Amarilla": DoubleYellowcardsList[i] if i < len(DoubleYellowcardsList) else "N/A",
            "Rojas": RedcardsList[i] if i < len(RedcardsList) else "N/A",
            "Sustituciones In": SubInList[i] if i < len(SubInList) else "N/A",
            "Sustituciones Out": SubOutList[i] if i < len(SubOutList) else "N/A",
        })

    return jugadores