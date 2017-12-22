# coding: utf-8
# In[0]: Load data from SQLite

import sqlite3
import pandas as pd
import numpy as np
import datetime
import os

def load_minutely_candles(sqlite_db_path):
    # Grab the data from the DB. Paths with ~ will break this.
    conn = sqlite3.connect(os.path.abspath(sqlite_db_path))
    query = 'select * from candles_USD_BTC'
    minutely_candles = pd.read_sql_query(query, conn)

    minutely_candles.dropna()

    minutely_candles['timestamp'] = minutely_candles['start'].apply(lambda ts: datetime.datetime.fromtimestamp(ts))
    #minutely_candles['timestamp_str'] = minutely_candles['timestamp'].apply(lambda dt: dt.strftime('%Y-%m-%d %H:%M:%S'))
    minutely_candles = minutely_candles.drop(['id', 'start'], axis=1)
    minutely_candles.sort_values('timestamp', inplace=True)
    return minutely_candles

def agg_to_hourly(candles):
    hourly_candles = candles.copy()
    # Truncate timestamp to hour
    hourly_candles['timestamp'] = hourly_candles['timestamp'].transform(lambda ts: ts.replace(minute=0, second=0, microsecond=0))
    hourly_candles = hourly_candles.groupby('timestamp', as_index=False).agg({'high': max,
                                                                              'low': min,
                                                                              'open': lambda x: x.iloc[0],
                                                                              'close': lambda x: x.iloc[-1],
                                                                              'volume': sum,
                                                                              'trades': sum})
    return hourly_candles

def agg_to_daily(candles):
    daily_candles = candles.copy()
    # Truncate timestamp to hour
    daily_candles['timestamp'] = daily_candles['timestamp'].transform(lambda ts: ts.replace(hour=0, minute=0, second=0, microsecond=0))
    daily_candles = daily_candles.groupby('timestamp', as_index=False).agg({'high': max,
                                                                            'low': min,
                                                                            'open': lambda x: x.iloc[0],
                                                                            'close': lambda x: x.iloc[-1],
                                                                            'volume': sum,
                                                                            'trades': sum})
    return daily_candles

def add_bollinger_bands(candles, window_size=1):
    # Add rolling mean and rolling volatility
    rolling_mean = candles['close'].rolling(window_size).mean()
    rolling_volatility = candles['close'].rolling(window_size).std()
    candles['rolling_mean'] = rolling_mean
    candles['rolling_volatility'] = rolling_volatility

    # Add top & bottom Bollinger bands
    candles['bollinger_top'] = rolling_mean + 2*rolling_volatility
    candles['bollinger_bottom'] = rolling_mean - 2*rolling_volatility

    # Mark places where closing price trend crosses the top Bollinger band
    # from above to below. That is, previous hour above top band, current
    # price below top band.
    above_bollinger_top = candles['close'] >= candles['bollinger_top']
    below_bollinger_top = candles['close'] < candles['bollinger_top']
    candles['cross_bollinger_top'] = above_bollinger_top.shift() * below_bollinger_top

    # Mark places where closing price trend crosses the bottom Bollinger band
    # from above to below. That is, previous hour below bottom band, current
    # price above bottom band.
    above_bollinger_bottom = candles['close'] >= candles['bollinger_bottom']
    below_bollinger_bottom = candles['close'] < candles['bollinger_bottom']
    candles['cross_bollinger_bottom'] = below_bollinger_bottom.shift() * above_bollinger_bottom

    # Drop NAs caused by calculation of rolling statistics
    candles.dropna(inplace=True)

    return candles
