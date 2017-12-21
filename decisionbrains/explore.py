
# coding: utf-8

# In[0]: Load data from SQLite

import sqlite3
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import os

cwd = os.getcwd()
history_path = os.path.abspath(os.path.join(cwd, '..', 'history'))
# Grab the data from the DB. Paths with ~ will break this.
dbAbsolutePath = os.path.join(history_path, 'gdax_0.1.db')
conn = sqlite3.connect(dbAbsolutePath)
query = 'select * from candles_USD_BTC'
minutely_candles = pd.read_sql_query(query, conn)

minutely_candles.dropna()
print(minutely_candles.head())

# In[0]: Add some features
minutely_candles['timestamp'] = minutely_candles['start'].apply(lambda ts: datetime.datetime.fromtimestamp(ts))
#minutely_candles['timestamp_str'] = minutely_candles['timestamp'].apply(lambda dt: dt.strftime('%Y-%m-%d %H:%M:%S'))
minutely_candles['totalMillions'] = (minutely_candles['vwp'] * minutely_candles['trades']) / 1000000
minutely_candles = minutely_candles.drop(['id', 'start'], axis=1)
minutely_candles.sort_values('timestamp', inplace=True)
print(minutely_candles.head())


# In[0]: Noisy as fro, yo, need to aggregate
plt.plot(minutely_candles['timestamp'], minutely_candles['vwp'])
plt.show()

plt.plot(minutely_candles['timestamp'], minutely_candles['trades'])
plt.show()

# In[0]: Aggregate to hourly level
hourly_candles = minutely_candles.copy()
# Truncate timestamp to hour
hourly_candles['timestamp'] = hourly_candles['timestamp'].transform(lambda ts: ts.replace(microsecond=0,second=0,minute=0))
#minutely_candles['timestamp_str'] = hourly_candles['timestamp'].apply(lambda dt: dt.strftime('%Y-%m-%d %H:%M:%S'))
# TODO: Open/Close aggregation
hourly_candles = hourly_candles.groupby('timestamp', as_index=False).agg({'high': max,
                                                                          'low': min,
                                                                          'open': lambda x: x.iloc[0],
                                                                          'close': lambda x: x.iloc[-1],
                                                                          'volume': sum,
                                                                          'trades': sum})

# In[0]: Add features to hourly granularity data

# Add rolling mean and rolling volatility
rolling_mean = hourly_candles['close'].rolling(24).mean()
rolling_volatility = hourly_candles['close'].rolling(24).std()
hourly_candles['rolling_mean'] = rolling_mean
hourly_candles['rolling_volatility'] = rolling_volatility

# Add top & bottom Bollinger bands
hourly_candles['bollinger_top'] = rolling_mean + 2*rolling_volatility
hourly_candles['bollinger_bottom'] = rolling_mean - 2*rolling_volatility

# Mark places where closing price trend crosses the top Bollinger band
# from above to below. That is, previous hour above top band, current
# price below top band.
above_bollinger_top = hourly_candles['close'] >= hourly_candles['bollinger_top']
below_bollinger_top = hourly_candles['close'] < hourly_candles['bollinger_top']
hourly_candles['cross_bollinger_top'] = above_bollinger_top.shift() * below_bollinger_top

# Mark places where closing price trend crosses the bottom Bollinger band
# from above to below. That is, previous hour below bottom band, current
# price above bottom band.
above_bollinger_bottom = hourly_candles['close'] >= hourly_candles['bollinger_bottom']
below_bollinger_bottom = hourly_candles['close'] < hourly_candles['bollinger_bottom']
hourly_candles['cross_bollinger_bottom'] = below_bollinger_bottom.shift() * above_bollinger_bottom

# Drop NAs caused by calculation of rolling statistics
hourly_candles.dropna(inplace=True)

print(hourly_candles.head())

# In[0]: Plot closing price with Bollinger bands over time

fig=plt.figure(figsize=(12, 6), dpi= 80, facecolor='w', edgecolor='k')
plt.suptitle('USD to BTC (hourly)', fontsize=5)
fig.suptitle(' Closing Price \\w Bollinger Bands\nUSD to BTC (hourly)', fontsize=20)
plt.xlabel('Time', fontsize=18)
plt.ylabel('Closing Price', fontsize=16)
plt.plot(hourly_candles['timestamp'], hourly_candles['close'], 'black', label='Closing Price')
plt.plot(hourly_candles['timestamp'], hourly_candles['rolling_mean'], 'gray', label='Rolling Mean')
plt.plot(hourly_candles['timestamp'], hourly_candles['bollinger_top'], 'blue', label='Bollinger Bands')
plt.plot(hourly_candles['timestamp'], hourly_candles['bollinger_bottom'], 'blue', label='')
bollinger_buy = hourly_candles[hourly_candles['cross_bollinger_bottom'] == True]
plt.plot(bollinger_buy['timestamp'], bollinger_buy['close'], 'ro', label='Advise Buy')
bollinger_sell = hourly_candles[hourly_candles['cross_bollinger_top'] == True]
plt.plot(bollinger_sell['timestamp'], bollinger_sell['close'], 'go', label='Advise Sell')
plt.legend()
plt.show()

# In[0]: Plot number of trades over time.

fig=plt.figure(figsize=(12, 6), dpi= 80, facecolor='w', edgecolor='k')
plt.suptitle('Number of Trades\nUSD to BTC (hourly)', fontsize=20)
plt.xlabel('Time', fontsize=18)
plt.ylabel('Number of Trades', fontsize=16)
plt.plot(hourly_candles['timestamp'], hourly_candles['trades'], 'black', label='Total Number Trades')
plt.plot(hourly_candles['timestamp'], hourly_candles['trades'].rolling(24).mean(), 'blue', label='Rolling Mean')
plt.legend()
plt.show()

# In[0]: Aggregate to daily level
daily_candles = hourly_candles.copy()
# Truncate timestamp to hour
daily_candles['timestamp'] = daily_candles['timestamp'].transform(lambda ts: ts.replace(hour=0))
#minutely_candles['timestamp_str'] = hourly_candles['timestamp'].apply(lambda dt: dt.strftime('%Y-%m-%d %H:%M:%S'))
# TODO: Open/Close aggregation
hourly_candles = hourly_candles.groupby('timestamp', as_index=False).agg({'high': max,
                                                                          'low': min,
                                                                          'open': lambda x: x.iloc[0],
                                                                          'close': lambda x: x.iloc[-1],
                                                                          'volume': sum,
                                                                          'trades': sum})

# In[0]: Add features to hourly granularity data

# Add rolling mean and rolling volatility
rolling_mean = hourly_candles['close'].rolling(48).mean()
rolling_volatility = hourly_candles['close'].rolling(48).std()
hourly_candles['rolling_mean'] = rolling_mean
hourly_candles['rolling_volatility'] = rolling_volatility

# Add top & bottom Bollinger bands
hourly_candles['bollinger_top'] = rolling_mean + 2*rolling_volatility
hourly_candles['bollinger_bottom'] = rolling_mean - 2*rolling_volatility

# Mark places where closing price trend crosses the top Bollinger band
# from above to below. That is, previous hour above top band, current
# price below top band.
above_bollinger_top = hourly_candles['close'] >= hourly_candles['bollinger_top']
below_bollinger_top = hourly_candles['close'] < hourly_candles['bollinger_top']
hourly_candles['cross_bollinger_top'] = above_bollinger_top.shift() * below_bollinger_top

# Mark places where closing price trend crosses the bottom Bollinger band
# from above to below. That is, previous hour below bottom band, current
# price above bottom band.
above_bollinger_bottom = hourly_candles['close'] >= hourly_candles['bollinger_bottom']
below_bollinger_bottom = hourly_candles['close'] < hourly_candles['bollinger_bottom']
hourly_candles['cross_bollinger_bottom'] = below_bollinger_bottom.shift() * above_bollinger_bottom

# Drop NAs caused by calculation of rolling statistics
hourly_candles.dropna(inplace=True)

print(hourly_candles.head())
