# In[0]: Set up environment.
import os
import candles
import matplotlib.pyplot as plt
from plydata import query
from plotnine import ggplot, geom_line, geom_point, aes, theme, element_text, ggtitle
from datetime import datetime, timedelta


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

ago_24hrs = datetime.now() - timedelta(hours=24)
minutely_last24hrs = minutely_candles[minutely_candles.timestamp >= ago_24hrs]
bollinger_buy = minutely_last24hrs[minutely_last24hrs['cross_bollinger_bottom'] == True]
bollinger_sell = minutely_last24hrs[minutely_last24hrs['cross_bollinger_top'] == True]
(ggplot(data=None) +
     geom_line(aes('timestamp', 'close'), data=minutely_last24hrs, color='black') +
     geom_line(aes('timestamp', 'rolling_mean'), data=minutely_last24hrs, color='grey') +
     geom_line(aes('timestamp', 'bollinger_top'), data=minutely_last24hrs, color='blue') +
     geom_line(aes('timestamp', 'bollinger_bottom'), data=minutely_last24hrs, color='blue') +
     geom_point(aes('timestamp', 'close'), data=bollinger_buy, color='green') +
     geom_point(aes('timestamp', 'close'), data=bollinger_sell, color='red') +
     theme(axis_text_x=element_text(rotation=45)) +
     ggtitle('Closing Price \\w Bollinger Bands\nUSD to BTC (minutely)')
)

# In[0]: Plot minutely number of trades over time.

(ggplot(minutely_last24hrs) +
     geom_line(aes('timestamp', 'trades'), color='black') +
     theme(axis_text_x=element_text(rotation=45)) +
     ggtitle('CNumber of Trades\nUSD to BTC (minutely)')
)

# In[0]: Plot hourly closing price with Bollinger bands over time

bollinger_buy = hourly_candles[hourly_candles['cross_bollinger_bottom'] == True]
bollinger_sell = hourly_candles[hourly_candles['cross_bollinger_top'] == True]
(ggplot(data=None) +
     geom_line(aes('timestamp', 'close'), data=hourly_candles, color='black') +
     geom_line(aes('timestamp', 'rolling_mean'), data=hourly_candles, color='grey') +
     geom_line(aes('timestamp', 'bollinger_top'), data=hourly_candles, color='blue') +
     geom_line(aes('timestamp', 'bollinger_bottom'), data=hourly_candles, color='blue') +
     geom_point(aes('timestamp', 'close'), data=bollinger_buy, color='green') +
     geom_point(aes('timestamp', 'close'), data=bollinger_sell, color='red') +
     theme(axis_text_x=element_text(rotation=45)) +
     ggtitle('Closing Price \\w Bollinger Bands\nUSD to BTC (minutely)')
)

# In[0]: Plot hourly  number of trades over time.

(ggplot(hourly_candles) +
     geom_line(aes('timestamp', 'trades'), color='black') +
     theme(axis_text_x=element_text(rotation=45)) +
     ggtitle('Number of Trades\nUSD to BTC (minutely)')
)

# In[0]: Plot daily closing price with Bollinger bands over time

bollinger_buy = daily_candles[daily_candles['cross_bollinger_bottom'] == True]
bollinger_sell = daily_candles[daily_candles['cross_bollinger_top'] == True]
(ggplot(data=None) +
     geom_line(aes('timestamp', 'close'), data=daily_candles, color='black') +
     geom_line(aes('timestamp', 'rolling_mean'), data=daily_candles, color='grey') +
     geom_line(aes('timestamp', 'bollinger_top'), data=daily_candles, color='blue') +
     geom_line(aes('timestamp', 'bollinger_bottom'), data=daily_candles, color='blue') +
     geom_point(aes('timestamp', 'close'), data=bollinger_buy, color='green') +
     geom_point(aes('timestamp', 'close'), data=bollinger_sell, color='red') +
     theme(axis_text_x=element_text(rotation=45)) +
     ggtitle('Closing Price \\w Bollinger Bands\nUSD to BTC (minutely)')
)

# In[0]: Plot daily number of trades over time.

(ggplot(daily_candles) +
     geom_line(aes('timestamp', 'trades'), color='black') +
     theme(axis_text_x=element_text(rotation=45)) +
     ggtitle('Number of Trades\nUSD to BTC (minutely)')
)
