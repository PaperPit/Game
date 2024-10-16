import requests
from bs4 import BeautifulSoup

# Определяем адрес страницы
url = 'https://nplus1.ru/news/2021/10/11/econobel2021'

# Выполняем GET-запрос
response = requests.get(url)

# Создаём объект BeautifulSoup
page = BeautifulSoup(response.text, 'html.parser')

# Находим все meta теги с атрибутом name
meta_description = page.find('meta', attrs={'itemprop': 'datePublished'})
meta_og_title = page.find('meta', attrs={'property': 'og:site_name'})

# Выводим значения атрибутов content для найденных meta-тегов
if meta_description:
    print("Meta Description:", meta_description['content'])

if meta_og_title:
    print("OG Title:", meta_og_title['content'])
