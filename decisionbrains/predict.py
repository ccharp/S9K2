# %%: Set up environment.
import os
import candles
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cwd = os.getcwd()
history_path = os.path.abspath(os.path.join(cwd, '..', 'history'))
db_path = os.path.join(history_path, 'gdax_0.1.db')

# %%: Get hourly candles.

minutely_candles = candles.load_minutely_candles(db_path)
hourly_candles = candles.agg_to_hourly(minutely_candles)
hourly_candles = candles.add_bollinger_bands(hourly_candles, 48)

# %%: Set up features & response variable.

temp = hourly_candles.set_index('timestamp')

close_price = temp['close']
target = 100.0 * (close_price - close_price.shift()) / close_price

lags = []
for i in range(24):
    lagged = temp.shift(i+1)
    cols = list(temp.columns)
    renames = {}
    for col in cols:
        renames[col] = col + '_shift' + str(i+1)
    lags.append(lagged.rename(columns=renames))

lagged = pd.concat(lags, axis=1).dropna()

lagged['delta'] = target
lagged.dropna(inplace=True)

# %%: Prep data for model.

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X = lagged.drop('delta', axis=1)
y = lagged['delta']

# Split into train and holdout sets.
# Train set is used for model selection.
# Holdout set is used to evaluate final model.
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=888)

# Scale predictors and response
X_scaler = StandardScaler().fit(X_train)
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)

# %%: Train model and make predictions.

from sklearn.svm import SVR
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import mean_squared_error

# Perform model selection using cross-validation.
model_base = SVR(max_iter=1e6)
param_search_space = {
    'kernel': ['linear','poly','rbf','sigmoid'],
    'C': np.logspace(-5,1,7),
    'epsilon': np.logspace(-6,-1,6)
}

hyperparameter_search = RandomizedSearchCV(model_base,
                                           param_distributions=param_search_space,
                                           n_iter=25,
                                           n_jobs=5,
                                           random_state=888)

model = hyperparameter_search
model.fit(X_train_scaled, y_train.ravel())

# %% Evaluate model predictions.

# Show root mean squared error on data the model has never seen.
prediction_test = model.predict(X_test_scaled)
rmse_test = np.sqrt(mean_squared_error(y_test.ravel(), prediction_test))
print('Test RMSE {0}'.format(rmse_test))

# Confirm that predictions don't have obvious bias.
plt.scatter(y_test, prediction_test)
