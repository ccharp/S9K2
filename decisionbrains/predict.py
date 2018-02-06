# %%: Set up environment.
import os
import candles
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from talib_wrapper import TechnicalAnalysis

cwd = os.getcwd()
history_path = os.path.abspath(os.path.join(cwd, '..', 'history'))
db_path = os.path.join(history_path, 'gdax_0.1.db')

# %%: Get hourly candles.

minutely_candles = candles.load_minutely_candles(db_path)
hourly_candles = candles.agg_to_hourly(minutely_candles)
hourly_candles.set_index('timestamp', inplace=True)

# %%: Set up features & response variable.

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.base import BaseEstimator, TransformerMixin

class NoFitMixin():
    def fit(self, X, y=None):
        return self

class Lag(BaseEstimator, NoFitMixin, TransformerMixin):
    def __init__(self, lookback=24, compute_diffs=True):
        self.lookback = lookback
        self.compute_diffs = compute_diffs
    def transform(self, X, y=None):
        features = []
        lags = [X]
        for i in range(self.lookback):
            lagged = X.shift(i+1)
            renames = {col:'{0}_shift{1}'.format(col, i+1) for _,col in enumerate(X.columns)}
            lags.append(lagged.rename(columns=renames))
        features.extend(lags)

        if self.compute_diffs:
            diffs = []
            for curr, prev in zip(lags, lags[1:]):
                temp = pd.DataFrame()
                for i in range(len(curr.columns)):
                    col_name = curr.columns[i] + '_diff_' + prev.columns[i]
                    temp[col_name] = curr.iloc[:,i] - prev.iloc[:,i]
                    diffs.append(temp)
            features.extend(diffs)

        return pd.concat(features, axis=1)

class ComputeTarget(BaseEstimator, NoFitMixin, TransformerMixin):
    def transform(self, X, y=None):
        _X = X.copy()
        close_price = _X['close']
        _X['target'] = (100.0 * (close_price - close_price.shift()) / close_price).shift(-1)
        return _X

technical_indicator_pipe = Pipeline([
    ('compute_target', ComputeTarget()),
    ('compute_indicators', TechnicalAnalysis('talib_config.json')),
    ('drop_raw', FunctionTransformer(lambda df: df.drop(['high', 'low', 'open', 'close', 'volume', 'trades'], axis=1), validate=False)),
    ('lag', Lag(12)),
    ('drop_na', FunctionTransformer(lambda df: df.dropna(), validate=False))
])

# %%: Prep data for model.

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

indicators = technical_indicator_pipe.transform(hourly_candles)

X = indicators.drop('target', axis=1)
y = indicators['target']

# Split into train and holdout sets.
# Train set is used for model selection.
# Holdout set is used to evaluate final model.
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=8888)

# Scale predictors and response
X_scaler = StandardScaler().fit(X_train)
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)

# %%: Train model and make predictions.

from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error

# Perform model selection using cross-validation.
model_base = Ridge()
param_search_space = {
    'alpha': [10**i for i in range(-2,3)]
}

hyperparameter_search = GridSearchCV(model_base,
                                     param_grid=param_search_space,
                                     n_jobs=5,
                                     cv=3,
                                     scoring='neg_mean_squared_error')

model = hyperparameter_search
model.fit(X_train_scaled, y_train.ravel())

# %% Evaluate model predictions.

# Show root mean squared error on training data.
prediction_train = model.predict(X_train_scaled)
rmse_train = np.sqrt(mean_squared_error(y_train.ravel(), prediction_train))
print('Train RMSE {0}'.format(rmse_train))

# Show root mean squared error on test data.
prediction_test = model.predict(X_test_scaled)
rmse_test = np.sqrt(mean_squared_error(y_test.ravel(), prediction_test))
print('Test RMSE {0}'.format(rmse_test))

# Confirm that predictions don't have obvious bias.
plt.scatter(y_train, prediction_train)
plt.show()

plt.scatter(y_test, prediction_test)
plt.show()

