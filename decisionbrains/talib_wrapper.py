import talib as t
import talib.abstract as ta
import talib_config as tc

# Only useful documentation available: https://github.com/stoni/ta-lib/blob/master/include/ta_func.h
# Best examples on usage come from the tests: https://github.com/mrjbq7/ta-lib/blob/master/talib/test_abstract.py

def help():
    for name in ta.__TA_FUNCTION_NAMES__:
        print(name + " (" + ta.Function(name).info["display_name"] + ")")
        print("    Group: " + ta.Function(name).info['group'])
        print("    Input: " + str(ta.Function(name).info['input_names']))
        print("    Parameters: " + str(ta.Function(name).info['parameters']))
        print("    Output: " + str(ta.Function(name).info['output_names']))

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

def with_config(name):
    uname = name.upper()
    if uname not in tc.config:
        raise ValueError("No config found for " + name + ". Try again, you worthless sack of shit.")
    func_config = tc.config[uname]
    ta_func = ta.Function(uname)
    ta_func.parameters = func_config["parameters"]
    ta_func.input_names = func_config["input_names"]
    return ta_func()

def quote(s):
    return "'" + s + "'"

def gen_config():
    tab = "    "
    print("config = {")
    function_groups = t.get_function_groups()
    for group_name in function_groups:
        print(tab + "# Group: " + group_name)
        for name in function_groups[group_name]:
            info = ta.Function(name).info
            print(tab + quote(info["name"]) + " : { # " + info["display_name"])

            print(tab*2 + "'parameters' : {")
            params = info["parameters"]
            for p_key in params:
                print(tab*3 + quote(p_key) + " : " + str(params[p_key]) + ",")
            print(tab*2 + "},")

            input_names = info["input_names"]
            print(tab*2 + "'input_names' : {")
            for in_key in input_names:
                v = input_names[in_key]
                print(tab*3 + quote(in_key) + " : " + (quote(v) if isinstance(v, str) else str(v)) + ",")
            print(tab*2 + "},")

            print(tab*2 + "# Output: " + str(ta.Function(name).info['output_names']))
            print(tab + "},")
        print("\n")
    print("}")
