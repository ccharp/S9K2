# coding: utf-8
# In[0]: Load data from SQLite

import sqlite3
import pandas as pd
import datetime
import numpy as np
import os


def to_datetime(ts):
    pd.to_datetime(ts, unit='s')

def load_minutely_candles(sqlite_db_path):
    # Grab the data from the DB. Paths with ~ will break this.
    conn = sqlite3.connect(os.path.abspath(sqlite_db_path))
    query = 'SELECT * from candles_USD_BTC ORDER BY start'
    sql_result = pd.read_sql_query(query, conn, index_col='start', parse_dates={'start': {'unit': 's'}})
    sql_result.index.names = ['timestamp']
    return sql_result.dropna().drop('id', axis=1)

agg_dict = {'high' : max, 'low' : min,
           'open' : lambda c: c.iloc[0], 'close' : lambda c: c.iloc[-1],
           'volume' : sum, 'trades' : sum}

def agg_to_hourly(candles):
    return candles.resample('1H' ).aggregate(agg_dict)


def agg_to_daily(candles):
    return candles.resample('1D' ).aggregate(agg_dict)

# Imports data from specific coinbase CSV found here: https://www.kaggle.com/mczielinski/bitcoin-historical-data/data
# Data before 2015-6-1 is sparse. Date chosen semi-arbitrarily...
# MAKE BACKUP OF gdax_0.1.db BEFORE USING!
def import_historical_data(csv="/Users/ccharp/btc-csv/sorted.csv"):
    names=['timestamp','open','high','low','close','volume','volume_usd','vwp']
    to_datetime = lambda ts: pd.to_datetime(ts, unit='s')
    csv_data = pd.read_csv(csv, sep=',', names=names, parse_dates=[0], index_col=0, date_parser=to_datetime, skiprows=[0])

    # Big assumption here. Don't have #trade data, adding here mostly as placeholder and to satisfy db not-null constraint.
    csv_data['trades'] = csv_data.volume_usd // csv_data.high
    csv_data.drop('volume_usd', 1, inplace=True)

    gekko_data = load_minutely_candles('../history/gdax_0.1.db')
    last_minute = gekko_data.index[0] - pd.Timedelta(minutes=1)
    truncated = csv_data[pd.datetime(2015,6,1):last_minute]

    # Another assumption here: best to keep first of duplicate? Or average (using groupby)?
    truncated = truncated[~truncated.index.duplicated(keep='first')]

    # Convert back to what the db expects
    truncated.index = truncated.index.astype(np.int64) // 10**9
    truncated.index.names = ['start']

    print('Writing new db...')
    cwd = os.getcwd()
    history_path = os.path.abspath(os.path.join(cwd, '..', 'history'))
    db_path = os.path.join(history_path, 'gdax_0.1.db')
    conn = sqlite3.connect(os.path.abspath(db_path))
    truncated.to_sql('candles_USD_BTC', conn, index=True, if_exists='append')
