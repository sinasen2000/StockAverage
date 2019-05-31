from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

url = 'http://bigpara.hurriyet.com.tr/borsa/canli-borsa/'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
table = soup.select('.live-stock-item')

sum_stocks = 0
sum_prcntg = 0
stocks = []

# algorithm that scraps the data and passes the values into a dictionary
# it was pretty hard to understand how to use css in order to scrap the data.
for row in table:
    di = dict()
    di['company_name'] = row['data-symbol']
    # changing 2,5 to 2.5 for type casting
    di['stock_price'] = row.select_one('.node-c').get_text().replace(',', '.')
    di['percentage_change'] = row.select_one('.node-e').get_text().replace(',', '.')
    stocks.append(di)

    #tried to use statistics.mean but casting the string to float each time is costly.
    sum_stocks += float(di['stock_price'])
    sum_prcntg += float(di['percentage_change'])

avg_stock_price = sum_stocks/len(table)
avg_prcntg_change = sum_prcntg/len(table)
print(f"Current aveage stock price: {avg_stock_price}\nCurrent aveage percentage change: {avg_prcntg_change}")


for stock in stocks[0:50]:
    print(stock)

with open('stock_data_tr.json', 'w') as f:
    json.dump(stocks, f)

with open('stock_data_tr.json', 'r') as f:
    stocks = json.load(f)




