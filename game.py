import requests
from bs4 import BeautifulSoup

# Определяем адрес страницы
url = 'https://www.zdorovo365.ru/vakansii.html'

# Выполняем GET-запрос
response = requests.get(url)

# Создаём объект BeautifulSoup
page = BeautifulSoup(response.text, 'html.parser')

vacancy_header = page.find('h3', string ="Наши вакансии")
vacancy_position = page.find_all('span', class_='t')

print(vacancy_header.string)
# Выводим текст каждого элемента
for i, position in enumerate(vacancy_position, 1):
    print(f"Должность {i}: {position.text}")

