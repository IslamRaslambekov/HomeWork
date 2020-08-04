import requests
from pprint import pprint


URL = 'https://api.hh.ru/vacancies'
params = {'text': 'Python-разработчик AND Москва',
          'only_with_salary': True,
          'page': 1}

result = requests.get(URL, params=params).json()
min_salary = list()
max_salary = list()

for i in result['items']:
    # pprint(i)
    # print(result['found'])
    if (i['salary']['from'] is not None) and (i['salary']['to'] is not None):
        min_salary.append(i['salary']['from'])
        max_salary.append(i['salary']['to'])

print(f'Средняя з/п Python-разработчика в Москве \
от {sum(min_salary) // len(min_salary)} \
до {sum(max_salary) // len(max_salary)} RUR')
