import requests
import time
from pprint import pprint as pp

# ------------------------------------*
#    Название бота   lesson_15_bot    |
# ------------------------------------*

TOKEN = '1386457041:AAEGR3j0_zf-cNjdt6_5QtSrhdb4ZIwUYJA'
# PROXIES = {
#     'http': 'http://161.202.226.194',
#     'https': 'https://161.202.226.194',
# }
# Пробовал разные прокси, выдает ошибку. Без прокси все работает нормально.

URL = f'https://api.telegram.org/bot{TOKEN}'

url_gU = f'{URL}/getUpdates'
url_sM = f'{URL}/sendMessage'
counter = 0

while True:
    time.sleep(1)
    response = requests.get(url_gU)
    messages = response.json()['result']
    pp(messages)

    for message in messages:
        chat_id = message['message']['chat']['id']
        message_text = message['message']['text']
        if counter < 1:
            response = requests.post(url_sM, params={'chat_id': chat_id, 'text': 'Доброго времени суток!'})
            counter += 1

