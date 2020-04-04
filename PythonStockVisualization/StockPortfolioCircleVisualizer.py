# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 12:32:30 2020

@author: Brech
"""

import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader as web

tickers = ['AAPL', 'TSLA', 'FB', 'NVDA', 'AMZN', 'GOOG']
amounts = [7 ,5, 12, 16, 2, 4]
prices = []
total = []

for ticker in tickers:
    df = web.DataReader(ticker, 'yahoo', dt.datetime(2019,1,1), dt.datetime.now())
    price = df[-1:]['Close'][0]
    prices.append(price)
    index = ticker.index(ticker)
    total.append(price * amounts)
    
fig, ax = plt.subplots(figsize = (16, 8))

ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
                        
ax.tick_params(axis='x', color='white')
ax.tick_params(axis='y', color='white')

ax.set_title('Stock Portfolio', color='#EF6C35', fontsize=23)

patches, texts, autotexts = ax.pie(total, labels=tickers, autopct='%1.1f%%', pctdistance=0.8)
[text.set_color('white') for text in texts]

circle = plt.Circle((0,0),0.55,color='black')
plt.gca().add_artist(circle)

ax.text(-2, 1, 'Portfolio overview',fontsize=13, color='#FFE536', verticalalignment='center', horizontalalignment='center')
ax.text(-2, 0.85,f'total USD amount: {sum(total):.2f} $', fontsize=12, color='white verticalalignment='center', horizontalalignment='center')
counter = 0.15
for ticker in tickers:
    ax.text(-2, 0.85 - counter, f'{ticker}: {total[tickers.index(ticker)].2f} $', fontsize=12, color='white', verticalalignment='center', horizontalalignment='center')
    counter += 0.15


plt.show()