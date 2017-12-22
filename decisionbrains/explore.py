# In[0]: Set up environment.
import os
import candles
import matplotlib.pyplot as plt

figure_size = (10, 6) # Width, height of plots

cwd = os.getcwd()
history_path = os.path.abspath(os.path.join(cwd, '..', 'history'))
db_path = os.path.join(history_path, 'gdax_0.1.db')

# In[0]: Load minutely candles.

minutely_candles = candles.load_minutely_candles(db_path)
minutely_candles = candles.add_bollinger_bands(minutely_candles, 120)
print(minutely_candles.head())

# In[0]: Turn minutely candles into hourly candles.

hourly_candles = candles.agg_to_hourly(minutely_candles)
hourly_candles = candles.add_bollinger_bands(hourly_candles, 48)
print(hourly_candles.head())

# In[0]: Turn hourly candles into daily candles.

daily_candles = candles.agg_to_daily(hourly_candles)
daily_candles = candles.add_bollinger_bands(daily_candles, 3)
print(daily_candles.head())

# In[0]: Plot minutely closing price with Bollinger bands over time

fig=plt.figure(figsize=figure_size, dpi=80, facecolor='w', edgecolor='k')
fig.suptitle(' Closing Price \\w Bollinger Bands\nUSD to BTC (minutely)', fontsize=20)
plt.xlabel('Time', fontsize=18)
plt.ylabel('Closing Price', fontsize=16)
minutely_data = minutely_candles[minutely_candles['timestamp'] > '2017-12-19']
plt.plot(minutely_data['timestamp'], minutely_data['close'], 'black', label='Closing Price')
plt.plot(minutely_data['timestamp'], minutely_data['rolling_mean'], 'gray', label='Rolling Mean')
plt.plot(minutely_data['timestamp'], minutely_data['bollinger_top'], 'blue', label='Bollinger Bands')
plt.plot(minutely_data['timestamp'], minutely_data['bollinger_bottom'], 'blue', label='')
bollinger_buy = minutely_data[minutely_data['cross_bollinger_bottom'] == True]
plt.plot(bollinger_buy['timestamp'], bollinger_buy['close'], 'ro', label='Advise Buy')
bollinger_sell = minutely_data[minutely_data['cross_bollinger_top'] == True]
plt.plot(bollinger_sell['timestamp'], bollinger_sell['close'], 'go', label='Advise Sell')
plt.legend()
plt.show()

# In[0]: Plot minutely number of trades over time.

fig=plt.figure(figsize=figure_size, dpi= 80, facecolor='w', edgecolor='k')
plt.suptitle('Number of Trades\nUSD to BTC (minutely)', fontsize=20)
plt.xlabel('Time', fontsize=18)
plt.ylabel('Number of Trades', fontsize=16)
plt.plot(minutely_data['timestamp'], minutely_data['trades'], 'black', label='Total Number Trades')
plt.plot(minutely_data['timestamp'], minutely_data['trades'].rolling(60).mean(), 'red', label='Rolling Mean')
plt.legend()
plt.show()

# In[0]: Plot hourly closing price with Bollinger bands over time

fig=plt.figure(figsize=figure_size, dpi=80, facecolor='w', edgecolor='k')
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

# In[0]: Plot hourly number of trades over time.

fig=plt.figure(figsize=figure_size, dpi= 80, facecolor='w', edgecolor='k')
plt.suptitle('Number of Trades\nUSD to BTC (hourly)', fontsize=20)
plt.xlabel('Time', fontsize=18)
plt.ylabel('Number of Trades', fontsize=16)
plt.plot(hourly_candles['timestamp'], hourly_candles['trades'], 'black', label='Total Number Trades')
plt.plot(hourly_candles['timestamp'], hourly_candles['trades'].rolling(24).mean(), 'blue', label='Rolling Mean')
plt.legend()
plt.show()

# In[0]: Plot daily closing price with Bollinger bands over time

fig=plt.figure(figsize=figure_size, dpi=80, facecolor='w', edgecolor='k')
fig.suptitle(' Closing Price \\w Bollinger Bands\nUSD to BTC (daily)', fontsize=20)
plt.xlabel('Time', fontsize=18)
plt.ylabel('Closing Price', fontsize=16)
plt.plot(daily_candles['timestamp'], daily_candles['close'], 'black', label='Closing Price')
plt.plot(daily_candles['timestamp'], daily_candles['rolling_mean'], 'gray', label='Rolling Mean')
plt.plot(daily_candles['timestamp'], daily_candles['bollinger_top'], 'blue', label='Bollinger Bands')
plt.plot(daily_candles['timestamp'], daily_candles['bollinger_bottom'], 'blue', label='')
bollinger_buy = daily_candles[daily_candles['cross_bollinger_bottom'] == True]
plt.plot(bollinger_buy['timestamp'], bollinger_buy['close'], 'ro', label='Advise Buy')
bollinger_sell = daily_candles[daily_candles['cross_bollinger_top'] == True]
plt.plot(bollinger_sell['timestamp'], bollinger_sell['close'], 'go', label='Advise Sell')
plt.legend()
plt.show()

# In[0]: Plot daily number of trades over time.

fig = plt.figure(figsize=figure_size, dpi=80, facecolor='w', edgecolor='k')
plt.suptitle('Number of Trades\nUSD to BTC (daily)', fontsize=20)
plt.xlabel('Time', fontsize=18)
plt.ylabel('Number of Trades', fontsize=16)
plt.plot(daily_candles['timestamp'], daily_candles['trades'], 'black', label='Total Number Trades')
plt.plot(daily_candles['timestamp'], daily_candles['trades'].rolling(3).mean(), 'blue', label='Rolling Mean')
plt.legend()
plt.show()