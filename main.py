import bs4
import requests   #pip install requests bs4 lxml pandas xlsxwriter ->установка pandas
from bs4 import BeautifulSoup

import pandas as pd


headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 '
                  'YaBrowser/22.1.3.942 Yowser/2.5 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9 '
}


main_url = 'https://cyberscore.live/en/'

def get_soup(url):
    res = requests.get(url, headers)
    return bs4.BeautifulSoup(res.text, 'html.parser')

categories_page = get_soup(main_url+'matches/?type=past&tournament_id=43121&page=1')
categories = categories_page.findAll('a', class_= 'item matches-item info-blocks-item-height group/matches-item info-blocks-item-height--with-tournament online')

for cat in categories:
    subcategories_page = get_soup(main_url+cat['href'])
    subcategories = subcategories_page.findAll('a', class_= 'item matches-item info-blocks-item-height group/matches-item info-blocks-item-height--with-tournament online')
    for subcat in subcategories:
        matches_page =get_soup(main_url+subcat['href'])
        matches = matches_page.findAll('div',class_='      ')


data = [['TEAM', 'MATCHES', 'WINS', 'LOSSES', 'WINRATE', 'LOGO']]


#заголовок таблицы - считать

#словарь для хранения считанных данных dataframe
#df = {}

#считываем данные таблиц с сайта https://cyberscore.live/en/matches/?tournament_id=43121&type=past
#tables = pd.read_html('https://cyberscore.live/en/matches/?tournament_id=43121&type=past')





#print(len(tables))








