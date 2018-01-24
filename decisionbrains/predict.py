# %%: Set up environment.
import os
import candles
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plydata import query
from plotnine import ggplot, geom_line, geom_point, aes, theme, element_text, ggtitle
from datetime import datetime, timedelta

cwd = os.getcwd()
history_path = os.path.abspath(os.path.join(cwd, '..', 'history'))
db_path = os.path.join(history_path, 'gdax_0.1.db')

# %%: Load minutely candles.

minutely_candles = candles.load_minutely_candles(db_path)
minutely_candles = candles.add_bollinger_bands(minutely_candles, 120)
print(minutely_candles.head())

# %%: Turn minutely candles into hourly candles.

hourly_candles = candles.agg_to_hourly(minutely_candles)
hourly_candles = candles.add_bollinger_bands(hourly_candles, 48)
print(hourly_candles.head())

# %%: Set up features & response variable.

hourly_candles.set_index('timestamp', inplace=True)

lags = [hourly_candles]
for i in range(24):
    lagged = hourly_candles.copy().shift(i+1)
    cols = list(hourly_candles.columns)
    renames = {}
    for col in cols:
        renames[col] = col + '_shift' + str(i+1)
    lags.append(lagged.rename(columns=renames))

X = pd.concat(lags, axis=1).dropna()

close_price = X['close']
X['delta'] = (close_price - close_price.shift()) / close_price
X.dropna(inplace=True)
X.head()

# %%: Prep data for model.

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import mean_squared_error

temp = X['delta']
y = np.array(temp).reshape((len(temp), 1))
X.drop(columns=['delta'], inplace=True)

# Split into train and holdout sets.
# Train set is used for model selection.
# Holdout set is used to evaluate final model.
X_train, X_holdout, y_train, y_holdout = train_test_split(X, y, train_size=0.8, random_state=888)

# Scale predictors and response to be on same scale [0,1] (I think)
X_scaler = StandardScaler()
X_train_scaled = X_scaler.fit_transform(X_train)
X_holdout_scaled = X_scaler.transform(X_holdout)

y_scaler = StandardScaler()
y_train_scaled = y_scaler.fit_transform(y_train)
y_holdout_scaled = y_scaler.transform(y_holdout)

param_search_space = {
    'kernel': ['linear','poly','rbf','sigmoid'],
    'C': np.logspace(-5,1,7),
    'epsilon': np.logspace(-6,-1,6)
}

# %%: Train model and make predictions.

# Perform model selection using cross-validation.
model_base = SVR(max_iter=1e6)
hyperparameter_search = RandomizedSearchCV(model_base,
                                           param_distributions=param_search_space,
                                           n_iter=100,
                                           n_jobs=1,
                                           random_state=888)

model = hyperparameter_search
model.fit(X_train_scaled, y_train_scaled)

print(model.best_estimator_)

prediction_holdout = y_scaler.inverse_transform(model.predict(X_holdout_scaled))

# Show root mean squared error on data the model has never seen.
rms_holdout = mean_squared_error(y_holdout, prediction_holdout)**(0.5)
print('Holdout RMS {0}'.format(rms_holdout))
