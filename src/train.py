import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
import pickle
import yaml


with open("params.yaml") as f:
    params = yaml.safe_load(f)

train = pd.read_csv('src/data/train.csv')

X_train = train.drop(['datetime', 'count', 'casual', 'registered'], axis=1)
y_train = train['count']

model = GradientBoostingRegressor(n_estimators=params["train"]["n_estimators"],
                                   learning_rate=params["train"]["learning_rate"],
                                   max_depth=params["train"]["max_depth"],
                                   random_state=params["train"]["random_state"])

model.fit(X_train, y_train)

with open("src/data/weights.joblib", 'wb') as f:
    pickle.dump(model, f)
