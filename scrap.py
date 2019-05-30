from bs4 import BeautifulSoup
import requests

url = 'http://bigpara.hurriyet.com.tr/borsa/canli-borsa/'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

table = soup.select('.tableBox')

row = table[0]

efes = row.select('.live-stock-item').data_symbol

for i in efes:
    print(i)