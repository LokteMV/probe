import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ru/krasnodar/cars/mitsubishi/all/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def parse():
    html = get_html(URL)


parse()
