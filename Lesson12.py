import requests
from pprint import pprint

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

response = requests.get(URL).json()  # Берутся данные о курсах валют с ЦБ РФ https://www.cbr-xml-daily.ru/

usd_rate = response['Valute']['USD']['Value']
euro_rate = response['Valute']['EUR']['Value']

URL = 'https://api.hh.ru/vacancies'  # Перезапись URL

min_salary = list()
max_salary = list()

# Делается запрос чтобы узнать количество страниц
response = requests.get(URL, params={'text': 'Python AND Москва', 'only_with_salary': True, 'per_page': 100}).json()
pages = response['pages']

print(f"\nНайдено вакансий по запросу Python в Москве - {response['found']}\n")

for page in range(1, pages):  # Данные с последней страницы не будут браться
    params = {'text': 'Python AND Москва',
              'only_with_salary': True,
              'per_page': 100,
              'page': page}  # Страница будет меняться от 1 до 7 (не включая 7 страницу)

    response = requests.get(URL, params=params).json()  # На каждую страницу идет запрос

    for item in response['items']:
        salfrom = item['salary']['from']  # Зарплата от... (пример: от 100 000)
        salto = item['salary']['to']  # Зарплата до... (пример: до 150 000)
        salcurr = item['salary']['currency']  # Валюта (RUR, USD, EUR)

        if salcurr == 'RUR':
            if salfrom is not None:
                min_salary.append(salfrom)
            if salto is not None:
                max_salary.append(salto)

        elif salcurr == 'USD':
            if salfrom is not None:
                min_salary.append(int(salfrom * usd_rate))   # Перевод доллара в рубль
            if salto is not None:
                max_salary.append(int(salto * usd_rate))

        elif salcurr == 'EUR':
            if salfrom is not None:
                min_salary.append(int(salfrom * euro_rate))   # Перевод евро в рубль
            if salto is not None:
                max_salary.append(int(salto * euro_rate))


print(f'Средняя з/п разработчиков по запросу Python в Москве \
от {sum(min_salary) // len(min_salary)} \
до {sum(max_salary) // len(max_salary)} RUR')
