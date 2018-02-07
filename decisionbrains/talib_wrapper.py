import json
import pandas as pd
import numpy as np
import talib as t
import talib.abstract as ta
from sklearn.base import BaseEstimator, TransformerMixin

# Only useful documentation available: https://github.com/stoni/ta-lib/blob/master/include/ta_func.h
# Best examples on usage come from the tests: https://github.com/mrjbq7/ta-lib/blob/master/talib/test_abstract.py

class TechnicalAnalysis(BaseEstimator, TransformerMixin):
    def __init__(self, config_filepath='talib_config.json'):
        self.config = load_config(config_filepath)

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        indicators = self.compute_all_indicators(X)
        return pd.concat([X, indicators], axis=1)

    def compute_technical_indicator(self, data, indicator_config):
        name = indicator_config['name']
        ta_func = ta.Function(name)
        params = indicator_config['parameters']
        ta_func.parameters = params
        ta_func.input_names = indicator_config['input_names']
        indicator = ta_func(data)
        indicator_name = name
        if len(params) > 0:
            indicator_name += '_' + '_'.join(['{0}_{1}'.format(*x) for x in zip(params.keys(), params.values())])
        indicator.name = indicator_name
        return indicator

    def compute_all_indicators(self, data):
        indicators = []
        for indicator_name in self.config.keys():
            for configuration in self.config[indicator_name]:
                try:
                    indicator = self.compute_technical_indicator(data, configuration)
                    indicators.append(indicator)
                except Exception as e:
                    print('Error computing indicator "{0}" with config "{1}": {2}'.format(indicator_name, configuration, e))
        return pd.concat(indicators, axis=1)

def get_default_config():
    configs = {}
    # TODO: consider organizing by group
    for name in t.__TA_FUNCTION_NAMES__:
        info = ta.Function(name).info
        # There are many keys on info -- we only care about these two
        configs[name] = [{
            'name': info['name'],
            'parameters': info['parameters'],
            'input_names': info['input_names']
        }]
    return configs

def load_config(name="talib_config.json"):
    with open(name, 'r') as f:
        return json.load(f)

def write_config(name="talib_config.json", config=get_default_config()):
    with open(name, "w+") as f:
        json.dump(config, f, indent=2, sort_keys=True)

def get_cycle_indicators():
    return t.get_function_groups()['Cycle Indicators']

def get_math_operators():
    return t.get_function_groups()['Math Operators']

def get_math_transforms():
    return t.get_function_groups()['Math Transform']

def get_momentum_indicators():
    return t.get_function_groups()['Momentum Indicators']

def get_overlap_studies():
    return t.get_function_groups()['Overlap Studies']

def get_volatility_indicators():
    return t.get_function_groups()['Volatility Indicators']

def get_price_transforms():
    return t.get_function_groups()['Price Transorm']

def get_pattern_recognizers():
    return t.get_function_groups()['Pattern Recognition']

def get_volume_indicators():
    return t.get_function_groups()['Volume Indicators']
