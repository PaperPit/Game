import requests
from bs4 import BeautifulSoup

# Определяем адрес страницы
url = 'https://ru.wikipedia.org/wiki/Pink_Floyd'
def wiki_header(url):
    # Выполняем GET-запрос
    response = requests.get(url)
    # Создаём объект BeautifulSoup
    page = BeautifulSoup(response.text, 'html.parser')
    vacancy_header = page.find('span',class_='mw-page-title-main')
    return vacancy_header.string


print(wiki_header(url))


