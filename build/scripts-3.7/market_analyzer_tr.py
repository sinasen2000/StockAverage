import pandas as pd
import matplotlib.pyplot as plt
import copy

data = pd.read_json(open('stock_data_tr.json', 'r'))

data.set_index('company_name', inplace=True)

# printing all companies
print(data)

# printing the data of the companies with a positive increase in their stock price
print(data[data['percentage_change'] >= 0])

# printing the data of the companies with stock price bigger than 15, i.e big companies
print(data[data['stock_price'] >= 15])

# printing the data in descending stock price
data.sort_values('stock_price', ascending=False, inplace=True)

plt.style.use('seaborn-darkgrid')

data2 = copy.deepcopy(data.head(25))

fig, ax = plt.subplots(figsize=(10, 10))

ax.bar(data2.index, data2['stock_price'], color='#FF0000')

ax.set_ylabel = 'Stock Prices'

plt.yticks(fontsize='x-large')
plt.xticks(rotation=60, ha='right', fontsize='x-large', rotation_mode='anchor')
plt.legend(['Stock Price'], fontsize='xx-large')
plt.title('The Stock Prices of Top 25 Turkish Companies', fontsize='xx-large')

plt.show()

data.sort_values('percentage_change', ascending=False, inplace=True)

data3 = copy.deepcopy(data.head(10))
fig, ax = plt.subplots(figsize=(10, 10))
ax.bar(data3.index, data3['stock_price'], color='#FF0000')
ax.bar(data3.index, data3['percentage_change'], bottom=data3['stock_price'], color='#1E9BDD')
plt.legend(['Stock Price', 'Percentage Change'], fontsize='xx-large')
plt.title('10 Companies with the most positive percentage change', fontsize='xx-large')

plt.show()


