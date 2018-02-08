import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import candles
import talib_wrapper as taw
import utility as u

def test_ma(df, lead, lag, pc_thresh = 0.025):
    ma_df = df.copy()
    ma_df['lead'] = ma_df['close'].rolling(lead).mean()
    ma_df['lag'] = ma_df['close'].rolling(lag).mean()
    ma_df.dropna(inplace = True)
    ma_df['lead-lag'] = ma_df['lead'] - ma_df['lag']
    ma_df['pc_diff'] = ma_df['lead-lag'] / ma_df['close']
    ma_df['regime'] = np.where(ma_df['pc_diff'] > pc_thresh, 1, 0)
    ma_df['regime'] = np.where(ma_df['pc_diff'] < -pc_thresh, -1, ma_df['regime'])
    ma_df['Market'] = np.log(ma_df['close'] / ma_df['close'].shift(1))
    ma_df['Strategy'] = ma_df['regime'].shift(1) * ma_df['Market']
    ma_df[['Market','Strategy']] = ma_df[['Market','Strategy']].cumsum().apply(np.exp)
    return ma_df

__state = u.DECISION_HODL

# Returns single number from most recent data
def calc_weighted_avg(df, value_name, weight_name):
    weight = df[weight_name]
    value  = df[value_name]
    return (weight * value).sum() / weight.sum()

# Designed to operate minutely
def decide():
    cwd = os.getcwd()
    history_path = os.path.abspath(os.path.join(cwd, '..', 'history'))
    db_path = os.path.join(history_path, 'gdax_0.1.db')

    minutely_candles = candles.load_minutely_candles(db_path)
    minutely_candles.set_index('timestamp', inplace=True) # CSC: is this line necessary?

    # Calculate averages
    lead_amt = 1000
    lag_amt  = 5000
    # CSC: use talib to get some kind of weighted average
    window = minutely_candles.tail(lead_amt)
    lead_avg = calc_weighted_avg(window, "close", "volume")
    lag_avg  = calc_weighted_avg(window, "close", "volume")

    if __state == u.DECISION_SHORT and lead_avg > lag_avg:
        return u.DECISION_LONG
    elif __state == u.DECISION_LONG and lead_avg < lag_avg:
        return u.DECISION_SHORT
    else:
        return u.DECISION_HODL

# %%: Get hourly candles.
"""
cwd = os.getcwd()
history_path = os.path.abspath(os.path.join(cwd, '..', 'history'))
db_path = os.path.join(history_path, 'gdax_0.1.db')

minutely_candles = candles.load_minutely_candles(db_path)
hourly_candles = candles.agg_to_hourly(minutely_candles)
hourly_candles.set_index('timestamp', inplace=True)
print(hourly_candles.size)


# %%: Do the computation
lead = 1000
lag = 5000
pc_thresh = 0.025
ma_df = minutely_candles.copy()
ma_df['lead'] = ma_df['close'].rolling(lead).mean()
ma_df['lag'] = ma_df['close'].rolling(lag).mean()
ma_df.dropna(inplace = True)
ma_df['lead-lag'] = ma_df['lead'] - ma_df['lag']
ma_df['pc_diff'] = ma_df['lead-lag'] / ma_df['close']
ma_df['regime'] = np.where(ma_df['pc_diff'] > pc_thresh, 1, 0)
ma_df['regime'] = np.where(ma_df['pc_diff'] < -pc_thresh, -1, ma_df['regime'])
ma_df['Market'] = np.log(ma_df['close'] / ma_df['close'].shift(1))
ma_df['Strategy'] = ma_df['regime'].shift(1) * ma_df['Market']
ma_df[['Market','Strategy']] = ma_df[['Market','Strategy']].cumsum().apply(np.exp)

# %%: Assess (slightly more accurate assessment should go through gekko backtester)
ma_df[['Market','Strategy']].iloc[-1]
# ma_df[['Market','Strategy']][200000:].plot(figsize = (16,10))
"""

