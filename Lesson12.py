import requests
from pprint import pprint

URL = 'https://api.hh.ru/vacancies'
params = {'text': 'Python AND Москва',
          'only_with_salary': True,
          'page': 1}

result = requests.get(URL, params=params).json()
min_salary = list()
max_salary = list()

print(f"Найдено вакансий по запросу Python в Москве - {result['found']}")
counter = 0
for i in result['items']:
    if i['salary']['currency'] == 'RUR':
        if (i['salary']['from'] is not None) and (i['salary']['to'] is not None):
            min_salary.append(i['salary']['from'])
            max_salary.append(i['salary']['to'])
            counter += 1

print(f'Количесвто вакансий с указанной з/п - {counter}\n')

print(f'Средняя з/п Python-разработчика в Москве \
от {sum(min_salary) // len(min_salary)} \
до {sum(max_salary) // len(max_salary)} RUR')
