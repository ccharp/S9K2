import json
import pandas as pd
import numpy as np
import talib as t
import talib.abstract as ta

# Only useful documentation available: https://github.com/stoni/ta-lib/blob/master/include/ta_func.h
# Best examples on usage come from the tests: https://github.com/mrjbq7/ta-lib/blob/master/talib/test_abstract.py

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

def get_default_config():
    configs = {}
    # TODO: consider organizing by group
    for name in t.__TA_FUNCTION_NAMES__:
        info = ta.Function(name).info
        # There are many keys on info -- we only care about these two
        configs[name] = [{
            'parameters': info['parameters'],
            'input_names': info['input_names']
        }]
    return configs

def load_config(name="talib_default.json"):
    with open(name, 'r') as f:
        return json.load(f)

def write_config(name="talib_default.json", config=get_default_config()):
    with open(name, "w+") as f:
        json.dump(config, f, indent=2, sort_keys=True)

# Tsk, tsk. Global state.
_configs = load_config()

def with_config(name, data):
    uname = name.upper()
    if uname not in _configs:
        raise ValueError('No config found for "{0}".'.format(name))

    # apparently isn't a nice way create an empty data frame...
    results = pd.DataFrame(np.nan, index=[0], columns=["A"])
    for func_config in _configs[uname]:
        ta_func = ta.Function(uname)
        ta_func.parameters = func_config["parameters"]
        ta_func.input_names = func_config["input_names"]
        results.append(ta_func(data))
    return results.drop("A", 1)
