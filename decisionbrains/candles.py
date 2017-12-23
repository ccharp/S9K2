# coding: utf-8
# In[0]: Load data from SQLite

import sqlite3
import pandas as pd
from plydata import mutate, select, arrange, group_by, summarize, call
from plydata.options import options
import datetime
import os


def load_minutely_candles(sqlite_db_path):
    # Grab the data from the DB. Paths with ~ will break this.
    conn = sqlite3.connect(os.path.abspath(sqlite_db_path))
    query = 'select * from candles_USD_BTC'
    sql_result = pd.read_sql_query(query, conn)

    to_datetime = lambda ts: datetime.datetime.fromtimestamp(ts)
    return (sql_result.dropna() >>
        mutate(timestamp = 'start.apply(to_datetime)') >>
        select('id', 'start', drop=True) >>
        arrange('timestamp')
    )


def agg_to_hourly(candles):
    truncate_to_hour = lambda ts: ts.replace(minute=0, second=0, microsecond=0)
    with options(modify_input_data=True):
        return (candles.copy() >>
                mutate(timestamp='timestamp.apply(truncate_to_hour)') >>
                group_by('timestamp') >>
                summarize(high = 'max(high)', low = 'min(low)',
                          open = 'first(open)', close = 'last(close)',
                          volume = 'sum(volume)', trades = 'sum(trades)')
        )


def agg_to_daily(candles):
    truncate_to_day = lambda ts: ts.replace(hour=0, minute=0, second=0, microsecond=0)
    with options(modify_input_data=True):
        return (candles.copy() >>
                mutate(timestamp='timestamp.apply(truncate_to_day)') >>
                group_by('timestamp') >>
                summarize(high = 'max(high)', low = 'min(low)',
                          open = 'first(open)', close = 'last(close)',
                          volume = 'sum(volume)', trades = 'sum(trades)')
        )


def add_bollinger_bands(candles, window_size=1):
    rolling_mean = candles.close.rolling(window_size).mean()
    rolling_volatility = candles.close.rolling(window_size).std()
    return(candles >>
           mutate(rolling_mean = 'rolling_mean',
                  rolling_volatility = 'rolling_volatility',
                  bollinger_top = 'rolling_mean + 2*rolling_volatility',
                  bollinger_bottom = 'rolling_mean - 2*rolling_volatility') >>
           mutate(above_bollinger_top = 'close >= bollinger_top',
                  below_bollinger_bottom = 'close <= bollinger_bottom') >>
           mutate(cross_bollinger_top = 'above_bollinger_top.shift() * ~above_bollinger_top',
                  cross_bollinger_bottom = 'below_bollinger_bottom.shift() * ~below_bollinger_bottom',) >>
           call('.dropna')
    )
