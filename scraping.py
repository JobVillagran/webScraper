import requests
from bs4 import BeautifulSoup

# URL del sitio web a hacer scraping
url = "https://www.bbc.com/news"

# Realizar la solicitud HTTP al sitio web
response = requests.get(url)

# Crear el objeto BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Buscar el elemento <h3> con la clase "gs-c-promo-heading__title"
title_element = soup.find("h3", class_="gs-c-promo-heading__title")

# Verificar si se encontró el elemento
if title_element is not None:
    # Extraer el texto del elemento
    title = title_element.text.strip()
    print("Título de la noticia:", title)
else:
    print("No se encontró el título de la noticia")
