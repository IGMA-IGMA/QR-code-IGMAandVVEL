import requests
from bs4 import BeautifulSoup

def parser(id_number):
    link = f'https://soc-ege.sdamgia.ru/problem?id={id_number}'
    soup = BeautifulSoup(requests.get(link).text, 'html.parser')

    limited_tags = soup.find_all('span', limit=None)
    ret = []
    for tag in limited_tags:
        if 'Ответ' in str(tag):
            ret += [str(tag)[35:-7]]
    return ret[1]

print(parser(int(input())))