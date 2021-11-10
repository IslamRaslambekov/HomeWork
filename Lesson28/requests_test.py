import requests
import os

SERVER = 'http://127.0.0.1:8000/'
PAGE_1 = 'api/1.0.0/doctor/'
PAGE_2 = 'api/1.0.0/title/'

response = requests.get(os.path.join(SERVER, PAGE_1))
print(response.text)

response = requests.get(os.path.join(SERVER, PAGE_2))
print(response.text)
