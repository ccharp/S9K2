import talib as t

"""
Some configuation parameters may reference a *matype value. Use one of the following or 0:
    t.MA_Type.SMA: 'Simple Moving Average',
    t.MA_Type.EMA: 'Exponential Moving Average',
    t.MA_Type.WMA: 'Weighted Moving Average',
    t.MA_Type.DEMA: 'Double Exponential Moving Average',
    t.MA_Type.TEMA: 'Triple Exponential Moving Average',
    t.MA_Type.TRIMA: 'Triangular Moving Average',
    t.MA_Type.KAMA: 'Kaufman Adaptive Moving Average',
    t.MA_Type.MAMA: 'MESA Adaptive Moving Average',
    t.MA_Type.T3: 'Triple Generalized Double Exponential Moving Average',
"""

# CONFIGS
# DO NOT CHANGE KEYS OR STRUCTURE -- ONLY VALUES
config = {
    # Group: Cycle Indicators
    'HT_DCPERIOD' : { # Hilbert Transform - Dominant Cycle Period
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'HT_DCPHASE' : { # Hilbert Transform - Dominant Cycle Phase
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'HT_PHASOR' : { # Hilbert Transform - Phasor Components
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['inphase', 'quadrature']
    },
    'HT_SINE' : { # Hilbert Transform - SineWave
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['sine', 'leadsine']
    },
    'HT_TRENDMODE' : { # Hilbert Transform - Trend vs Cycle Mode
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['integer']
    },


    # Group: Math Operators
    'ADD' : { # Vector Arithmetic Add
        'parameters' : {
        },
        'input_names' : {
            'price0' : 'high',
            'price1' : 'low',
        },
        # Output: ['real']
    },
    'DIV' : { # Vector Arithmetic Div
        'parameters' : {
        },
        'input_names' : {
            'price0' : 'high',
            'price1' : 'low',
        },
        # Output: ['real']
    },
    'MAX' : { # Highest value over a specified period
        'parameters' : {
            'timeperiod' : 30,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'MAXINDEX' : { # Index of highest value over a specified period
        'parameters' : {
            'timeperiod' : 30,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['integer']
    },
    'MIN' : { # Lowest value over a specified period
        'parameters' : {
            'timeperiod' : 30,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'MININDEX' : { # Index of lowest value over a specified period
        'parameters' : {
            'timeperiod' : 30,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['integer']
    },
    'MINMAX' : { # Lowest and highest values over a specified period
        'parameters' : {
            'timeperiod' : 30,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['min', 'max']
    },
    'MINMAXINDEX' : { # Indexes of lowest and highest values over a specified period
        'parameters' : {
            'timeperiod' : 30,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['minidx', 'maxidx']
    },
    'MULT' : { # Vector Arithmetic Mult
        'parameters' : {
        },
        'input_names' : {
            'price0' : 'high',
            'price1' : 'low',
        },
        # Output: ['real']
    },
    'SUB' : { # Vector Arithmetic Substraction
        'parameters' : {
        },
        'input_names' : {
            'price0' : 'high',
            'price1' : 'low',
        },
        # Output: ['real']
    },
    'SUM' : { # Summation
        'parameters' : {
            'timeperiod' : 30,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },


    # Group: Math Transform
    'ACOS' : { # Vector Trigonometric ACos
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'ASIN' : { # Vector Trigonometric ASin
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'ATAN' : { # Vector Trigonometric ATan
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'CEIL' : { # Vector Ceil
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'COS' : { # Vector Trigonometric Cos
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'COSH' : { # Vector Trigonometric Cosh
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'EXP' : { # Vector Arithmetic Exp
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'FLOOR' : { # Vector Floor
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'LN' : { # Vector Log Natural
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'LOG10' : { # Vector Log10
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'SIN' : { # Vector Trigonometric Sin
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'SINH' : { # Vector Trigonometric Sinh
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'SQRT' : { # Vector Square Root
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'TAN' : { # Vector Trigonometric Tan
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'TANH' : { # Vector Trigonometric Tanh
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },


    # Group: Momentum Indicators
    'ADX' : { # Average Directional Movement Index
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'prices' : ['high', 'low', 'close'],
        },
        # Output: ['real']
    },
    'ADXR' : { # Average Directional Movement Index Rating
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'prices' : ['high', 'low', 'close'],
        },
        # Output: ['real']
    },
    'APO' : { # Absolute Price Oscillator
        'parameters' : {
            'fastperiod' : 12,
            'slowperiod' : 26,
            'matype' : 0,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'AROON' : { # Aroon
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'prices' : ['high', 'low'],
        },
        # Output: ['aroondown', 'aroonup']
    },
    'AROONOSC' : { # Aroon Oscillator
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'prices' : ['high', 'low'],
        },
        # Output: ['real']
    },
    'BOP' : { # Balance Of Power
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['real']
    },
    'CCI' : { # Commodity Channel Index
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'prices' : ['high', 'low', 'close'],
        },
        # Output: ['real']
    },
    'CMO' : { # Chande Momentum Oscillator
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'DX' : { # Directional Movement Index
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'prices' : ['high', 'low', 'close'],
        },
        # Output: ['real']
    },
    'MACD' : { # Moving Average Convergence/Divergence
        'parameters' : {
            'fastperiod' : 12,
            'slowperiod' : 26,
            'signalperiod' : 9,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['macd', 'macdsignal', 'macdhist']
    },
    'MACDEXT' : { # MACD with controllable MA type
        'parameters' : {
            'fastperiod' : 12,
            'fastmatype' : 0,
            'slowperiod' : 26,
            'slowmatype' : 0,
            'signalperiod' : 9,
            'signalmatype' : 0,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['macd', 'macdsignal', 'macdhist']
    },
    'MACDFIX' : { # Moving Average Convergence/Divergence Fix 12/26
        'parameters' : {
            'signalperiod' : 9,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['macd', 'macdsignal', 'macdhist']
    },
    'MFI' : { # Money Flow Index
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'prices' : ['high', 'low', 'close', 'volume'],
        },
        # Output: ['real']
    },
    'MINUS_DI' : { # Minus Directional Indicator
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'prices' : ['high', 'low', 'close'],
        },
        # Output: ['real']
    },
    'MINUS_DM' : { # Minus Directional Movement
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'prices' : ['high', 'low'],
        },
        # Output: ['real']
    },
    'MOM' : { # Momentum
        'parameters' : {
            'timeperiod' : 10,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'PLUS_DI' : { # Plus Directional Indicator
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'prices' : ['high', 'low', 'close'],
        },
        # Output: ['real']
    },
    'PLUS_DM' : { # Plus Directional Movement
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'prices' : ['high', 'low'],
        },
        # Output: ['real']
    },
    'PPO' : { # Percentage Price Oscillator
        'parameters' : {
            'fastperiod' : 12,
            'slowperiod' : 26,
            'matype' : 0,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'ROC' : { # Rate of change : ((price/prevPrice)-1)*100
        'parameters' : {
            'timeperiod' : 10,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'ROCP' : { # Rate of change Percentage: (price-prevPrice)/prevPrice
        'parameters' : {
            'timeperiod' : 10,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'ROCR' : { # Rate of change ratio: (price/prevPrice)
        'parameters' : {
            'timeperiod' : 10,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'ROCR100' : { # Rate of change ratio 100 scale: (price/prevPrice)*100
        'parameters' : {
            'timeperiod' : 10,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'RSI' : { # Relative Strength Index
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'STOCH' : { # Stochastic
        'parameters' : {
            'fastk_period' : 5,
            'slowk_period' : 3,
            'slowk_matype' : 0,
            'slowd_period' : 3,
            'slowd_matype' : 0,
        },
        'input_names' : {
            'prices' : ['high', 'low', 'close'],
        },
        # Output: ['slowk', 'slowd']
    },
    'STOCHF' : { # Stochastic Fast
        'parameters' : {
            'fastk_period' : 5,
            'fastd_period' : 3,
            'fastd_matype' : 0,
        },
        'input_names' : {
            'prices' : ['high', 'low', 'close'],
        },
        # Output: ['fastk', 'fastd']
    },
    'STOCHRSI' : { # Stochastic Relative Strength Index
        'parameters' : {
            'timeperiod' : 14,
            'fastk_period' : 5,
            'fastd_period' : 3,
            'fastd_matype' : 0,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['fastk', 'fastd']
    },
    'TRIX' : { # 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
        'parameters' : {
            'timeperiod' : 30,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'ULTOSC' : { # Ultimate Oscillator
        'parameters' : {
            'timeperiod1' : 7,
            'timeperiod2' : 14,
            'timeperiod3' : 28,
        },
        'input_names' : {
            'prices' : ['high', 'low', 'close'],
        },
        # Output: ['real']
    },
    'WILLR' : { # Williams' %R
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'prices' : ['high', 'low', 'close'],
        },
        # Output: ['real']
    },


    # Group: Overlap Studies
    'BBANDS' : { # Bollinger Bands
        'parameters' : {
            'timeperiod' : 5,
            'nbdevup' : 2,
            'nbdevdn' : 2,
            'matype' : 0,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['upperband', 'middleband', 'lowerband']
    },
    'DEMA' : { # Double Exponential Moving Average
        'parameters' : {
            'timeperiod' : 30,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'EMA' : { # Exponential Moving Average
        'parameters' : {
            'timeperiod' : 30,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'HT_TRENDLINE' : { # Hilbert Transform - Instantaneous Trendline
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'KAMA' : { # Kaufman Adaptive Moving Average
        'parameters' : {
            'timeperiod' : 30,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'MA' : { # Moving average
        'parameters' : {
            'timeperiod' : 30,
            'matype' : 0,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'MAMA' : { # MESA Adaptive Moving Average
        'parameters' : {
            'fastlimit' : 0.5,
            'slowlimit' : 0.05,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['mama', 'fama']
    },
    'MAVP' : { # Moving average with variable period
        'parameters' : {
            'minperiod' : 2,
            'maxperiod' : 30,
            'matype' : 0,
        },
        'input_names' : {
            'price' : 'close',
            'periods' : 'periods',
        },
        # Output: ['real']
    },
    'MIDPOINT' : { # MidPoint over period
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'MIDPRICE' : { # Midpoint Price over period
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'prices' : ['high', 'low'],
        },
        # Output: ['real']
    },
    'SAR' : { # Parabolic SAR
        'parameters' : {
            'acceleration' : 0.02,
            'maximum' : 0.2,
        },
        'input_names' : {
            'prices' : ['high', 'low'],
        },
        # Output: ['real']
    },
    'SAREXT' : { # Parabolic SAR - Extended
        'parameters' : {
            'startvalue' : 0,
            'offsetonreverse' : 0,
            'accelerationinitlong' : 0.02,
            'accelerationlong' : 0.02,
            'accelerationmaxlong' : 0.2,
            'accelerationinitshort' : 0.02,
            'accelerationshort' : 0.02,
            'accelerationmaxshort' : 0.2,
        },
        'input_names' : {
            'prices' : ['high', 'low'],
        },
        # Output: ['real']
    },
    'SMA' : { # Simple Moving Average
        'parameters' : {
            'timeperiod' : 30,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'T3' : { # Triple Exponential Moving Average (T3)
        'parameters' : {
            'timeperiod' : 5,
            'vfactor' : 0.7,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'TEMA' : { # Triple Exponential Moving Average
        'parameters' : {
            'timeperiod' : 30,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'TRIMA' : { # Triangular Moving Average
        'parameters' : {
            'timeperiod' : 30,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'WMA' : { # Weighted Moving Average
        'parameters' : {
            'timeperiod' : 30,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },


    # Group: Pattern Recognition
    'CDL2CROWS' : { # Two Crows
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDL3BLACKCROWS' : { # Three Black Crows
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDL3INSIDE' : { # Three Inside Up/Down
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDL3LINESTRIKE' : { # Three-Line Strike
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDL3OUTSIDE' : { # Three Outside Up/Down
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDL3STARSINSOUTH' : { # Three Stars In The South
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDL3WHITESOLDIERS' : { # Three Advancing White Soldiers
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLABANDONEDBABY' : { # Abandoned Baby
        'parameters' : {
            'penetration' : 0.3,
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLADVANCEBLOCK' : { # Advance Block
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLBELTHOLD' : { # Belt-hold
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLBREAKAWAY' : { # Breakaway
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLCLOSINGMARUBOZU' : { # Closing Marubozu
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLCONCEALBABYSWALL' : { # Concealing Baby Swallow
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLCOUNTERATTACK' : { # Counterattack
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLDARKCLOUDCOVER' : { # Dark Cloud Cover
        'parameters' : {
            'penetration' : 0.5,
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLDOJI' : { # Doji
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLDOJISTAR' : { # Doji Star
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLDRAGONFLYDOJI' : { # Dragonfly Doji
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLENGULFING' : { # Engulfing Pattern
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLEVENINGDOJISTAR' : { # Evening Doji Star
        'parameters' : {
            'penetration' : 0.3,
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLEVENINGSTAR' : { # Evening Star
        'parameters' : {
            'penetration' : 0.3,
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLGAPSIDESIDEWHITE' : { # Up/Down-gap side-by-side white lines
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLGRAVESTONEDOJI' : { # Gravestone Doji
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLHAMMER' : { # Hammer
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLHANGINGMAN' : { # Hanging Man
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLHARAMI' : { # Harami Pattern
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLHARAMICROSS' : { # Harami Cross Pattern
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLHIGHWAVE' : { # High-Wave Candle
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLHIKKAKE' : { # Hikkake Pattern
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLHIKKAKEMOD' : { # Modified Hikkake Pattern
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLHOMINGPIGEON' : { # Homing Pigeon
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLIDENTICAL3CROWS' : { # Identical Three Crows
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLINNECK' : { # In-Neck Pattern
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLINVERTEDHAMMER' : { # Inverted Hammer
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLKICKING' : { # Kicking
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLKICKINGBYLENGTH' : { # Kicking - bull/bear determined by the longer marubozu
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLLADDERBOTTOM' : { # Ladder Bottom
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLLONGLEGGEDDOJI' : { # Long Legged Doji
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLLONGLINE' : { # Long Line Candle
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLMARUBOZU' : { # Marubozu
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLMATCHINGLOW' : { # Matching Low
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLMATHOLD' : { # Mat Hold
        'parameters' : {
            'penetration' : 0.5,
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLMORNINGDOJISTAR' : { # Morning Doji Star
        'parameters' : {
            'penetration' : 0.3,
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLMORNINGSTAR' : { # Morning Star
        'parameters' : {
            'penetration' : 0.3,
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLONNECK' : { # On-Neck Pattern
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLPIERCING' : { # Piercing Pattern
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLRICKSHAWMAN' : { # Rickshaw Man
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLRISEFALL3METHODS' : { # Rising/Falling Three Methods
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLSEPARATINGLINES' : { # Separating Lines
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLSHOOTINGSTAR' : { # Shooting Star
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLSHORTLINE' : { # Short Line Candle
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLSPINNINGTOP' : { # Spinning Top
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLSTALLEDPATTERN' : { # Stalled Pattern
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLSTICKSANDWICH' : { # Stick Sandwich
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLTAKURI' : { # Takuri (Dragonfly Doji with very long lower shadow)
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLTASUKIGAP' : { # Tasuki Gap
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLTHRUSTING' : { # Thrusting Pattern
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLTRISTAR' : { # Tristar Pattern
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLUNIQUE3RIVER' : { # Unique 3 River
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLUPSIDEGAP2CROWS' : { # Upside Gap Two Crows
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },
    'CDLXSIDEGAP3METHODS' : { # Upside/Downside Gap Three Methods
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['integer']
    },


    # Group: Price Transform
    'AVGPRICE' : { # Average Price
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['open', 'high', 'low', 'close'],
        },
        # Output: ['real']
    },
    'MEDPRICE' : { # Median Price
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['high', 'low'],
        },
        # Output: ['real']
    },
    'TYPPRICE' : { # Typical Price
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['high', 'low', 'close'],
        },
        # Output: ['real']
    },
    'WCLPRICE' : { # Weighted Close Price
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['high', 'low', 'close'],
        },
        # Output: ['real']
    },


    # Group: Statistic Functions
    'BETA' : { # Beta
        'parameters' : {
            'timeperiod' : 5,
        },
        'input_names' : {
            'price0' : 'high',
            'price1' : 'low',
        },
        # Output: ['real']
    },
    'CORREL' : { # Pearson's Correlation Coefficient (r)
        'parameters' : {
            'timeperiod' : 30,
        },
        'input_names' : {
            'price0' : 'high',
            'price1' : 'low',
        },
        # Output: ['real']
    },
    'LINEARREG' : { # Linear Regression
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'LINEARREG_ANGLE' : { # Linear Regression Angle
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'LINEARREG_INTERCEPT' : { # Linear Regression Intercept
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'LINEARREG_SLOPE' : { # Linear Regression Slope
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'STDDEV' : { # Standard Deviation
        'parameters' : {
            'timeperiod' : 5,
            'nbdev' : 1,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'TSF' : { # Time Series Forecast
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },
    'VAR' : { # Variance
        'parameters' : {
            'timeperiod' : 5,
            'nbdev' : 1,
        },
        'input_names' : {
            'price' : 'close',
        },
        # Output: ['real']
    },


    # Group: Volatility Indicators
    'ATR' : { # Average True Range
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'prices' : ['high', 'low', 'close'],
        },
        # Output: ['real']
    },
    'NATR' : { # Normalized Average True Range
        'parameters' : {
            'timeperiod' : 14,
        },
        'input_names' : {
            'prices' : ['high', 'low', 'close'],
        },
        # Output: ['real']
    },
    'TRANGE' : { # True Range
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['high', 'low', 'close'],
        },
        # Output: ['real']
    },


    # Group: Volume Indicators
    'AD' : { # Chaikin A/D Line
        'parameters' : {
        },
        'input_names' : {
            'prices' : ['high', 'low', 'close', 'volume'],
        },
        # Output: ['real']
    },
    'ADOSC' : { # Chaikin A/D Oscillator
        'parameters' : {
            'fastperiod' : 3,
            'slowperiod' : 10,
        },
        'input_names' : {
            'prices' : ['high', 'low', 'close', 'volume'],
        },
        # Output: ['real']
    },
    'OBV' : { # On Balance Volume
        'parameters' : {
        },
        'input_names' : {
            'price' : 'close',
            'prices' : ['volume'],
        },
        # Output: ['real']
    },
}