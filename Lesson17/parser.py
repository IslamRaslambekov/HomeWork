import requests
from bs4 import BeautifulSoup
from Lesson17.db import run_db


def run():
    HOST = 'https://www.kant.ru'
    URL = 'https://www.kant.ru/catalog/bikes/#/filter:page=1&'

    html = requests.get(URL).text

    soup = BeautifulSoup(html, 'html.parser')
    containers = soup.find_all('div', class_='kant__catalog__item__content')
    bikes = list()
    for container in containers:
        link = HOST + container.find('a').get('href')
        model = container.find('div', {'class': 'kant__catalog__item-title'}).getText()[12:].replace('            ',
                                                                                                     '').replace(',',
                                                                                                                 '.')
        price = container.find('span', {'class': 'kant__price'}).getText(strip=True)
        if container.find('span', {'class': 'kant__catalog__price--old kant__price'}) is not None:
            old_price = container.find('span', {'class': 'kant__catalog__price--old kant__price'}).getText(strip=True)
        else:
            old_price = None

        bikes.append({
            'link': link,
            'model': model,
            'price': price,
            'old_price': old_price
        })

    for bike in bikes:
        run_db(str(bike['link']), str(bike['model']), bike['price'], bike['old_price'])
