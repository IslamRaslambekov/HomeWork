import requests
from pprint import pprint


def find_vacancies(parameters):
    URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(URL).json()
    usd_rate = response['Valute']['USD']['Value']
    euro_rate = response['Valute']['EUR']['Value']

    URL_HH = 'https://api.hh.ru/vacancies'

    min_salary = list()
    max_salary = list()

    response = requests.get(URL_HH, params=parameters).json()
    pages = response['pages']
    vacancies_count = response['found']

    for page in range(pages + 1):

        params = {'text': parameters.get('text'),
                  'only_with_salary': parameters.get('only_with_salary'),
                  'per_page': parameters.get('per_page'),
                  'page': page}

        response = requests.get(URL_HH, params=params).json()

        for item in response['items']:
            salfrom = item['salary']['from']
            salto = item['salary']['to']
            salcurr = item['salary']['currency']

            if salcurr == 'RUR':
                if salfrom is not None:
                    min_salary.append(salfrom)
                if salto is not None:
                    max_salary.append(salto)

            elif salcurr == 'USD':
                if salfrom is not None:
                    min_salary.append(int(salfrom * usd_rate))
                if salto is not None:
                    max_salary.append(int(salto * usd_rate))

            elif salcurr == 'EUR':
                if salfrom is not None:
                    min_salary.append(int(salfrom * euro_rate))
                if salto is not None:
                    max_salary.append(int(salto * euro_rate))

    data = {
        'average_salary': f'{sum(min_salary) // len(min_salary)} - {sum(max_salary) // len(max_salary)}',
        'vacancies_count': vacancies_count
    }

    return data
