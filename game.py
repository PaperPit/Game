import requests
from bs4 import BeautifulSoup
from pprint import pprint # Импортируем функцию pprint()

token = '857185a1857185a1857185a1278650cfba88571857185a1e2654cc27ca693a670fb5e4e' # Указываем свой сервисный токен
url = 'https://api.vk.com/method/users.get?user_id=1&v=5.95&fields=sex,bdate&access_token=' # Указываем адрес страницы к которой делаем запрос
ids = ",".join(map(str, range(1, 501))) # Формируем строку, содержащую информацию о поле id первых трёх пользователей
params = {'user_ids': ids, 'v': 5.95, 'fields': 'sex,bdate', 'access_token': token, 'lang': 'ru'} 
user =  requests.get(url, params=params).json()
print(user['response'][100]["sex"]) # Выводим дату рождения первого пользователя на экран
men = 0
women = 0
other = 0

for i in range(500):
    pol = user['response'][i]["sex"]
    if pol == 1:
        women += 1
    elif pol == 2:
        men += 1
    else:
        other += 1

print(women/(men+women))

#token = 857185a1857185a1857185a1278650cfba88571857185a1e2654cc27ca693a670fb5e4e
