import requests
from pprint import pprint

URL = 'https://api.hh.ru/vacancies'
params = {'text': 'Python AND Москва',
          'only_with_salary': True,
          'per_page': 100,
          'page': 1}

response = requests.get(URL, params=params).json()
min_salary = list()
max_salary = list()

print(f"\nНайдено вакансий по запросу Python в Москве - {response['found']}\n")
RUR_count = 0
USD_count = 0
EUR_count = 0
for i in response['items']:
    if (i['salary']['from'] is not None) and (i['salary']['to'] is not None):

        if i['salary']['currency'] == 'RUR':
            min_salary.append(i['salary']['from'])
            max_salary.append(i['salary']['to'])
            RUR_count += 1

        elif i['salary']['currency'] == 'USD':
            min_salary.append((i['salary']['from']) * 73.59)
            max_salary.append((i['salary']['to']) * 73.59)
            USD_count += 1

        elif i['salary']['currency'] == 'EUR':
            min_salary.append((i['salary']['from']) * 87.05)
            max_salary.append((i['salary']['to']) * 87.05)
            EUR_count += 1

print(f'Количесвто вакансий с указанной з/п: \
\nв рублях - {RUR_count} \
\nв долларах - {USD_count} \
\nв евро - {EUR_count}\n')

print(f'Средняя з/п Python-разработчика в Москве \
от {sum(min_salary) // len(min_salary)} \
до {sum(max_salary) // len(max_salary)} RUR')
