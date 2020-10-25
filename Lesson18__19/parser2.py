import requests
from bs4 import BeautifulSoup
# from Lesson17.db import run_db


def run():
    HOST = 'https://www.velosite.ru'
    URL = 'https://www.velosite.ru/catalog/search/?root_category=1&sort=popularity&sort_type=desc&view=blocks&in_stock=1' \
          '&brand%5B%5D=273&brand%5B%5D=305&brand%5B%5D=415&gender=&stature= '
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/84.0.4147.135 Safari/537.36 '
    }
    html = requests.get(URL).text

    soup = BeautifulSoup(html, 'html.parser')
    containers = soup.find_all('div', class_='card--inner-hover')
    bikes = list()

    for container in containers:
        link = HOST + container.find('div', class_='card__bottom_price--right global-grid-50 grid-parent').find(
            'a').get('href')
        model = container.find('div', class_='card--inner').find('a', class_='noborder card__info').getText()[
                11:].replace(',', '.')
        price = container.find('div', class_='card__bottom_price').find('span', class_='accent-red').getText().replace(
            '\xa0', ' ')
        old_price = None

        bikes.append({
            'link': link,
            'model': model,
            'price': price,
            'old_price': old_price
        })
    return bikes
    # for bike in bikes:
    #     run_db(str(bike['link']), str(bike['model']), bike['price'], bike['old_price'])