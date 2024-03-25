import pandas as pd
from sklearn.metrics import root_mean_squared_log_error
import pickle
import json


with open("data/weights.joblib", 'rb') as f:
    model = pickle.load(f)


test = pd.read_csv('data/test.csv')

X_test = test.drop(['datetime', 'count', 'casual', 'registered'], axis=1)
y_test = test['count']

predictions = model.predict(X_test)
predictions = [max(0, x) for x in predictions]

rmsle = root_mean_squared_log_error(y_test, predictions)
print('RMSLE:', rmsle)

with open("data/metrics.json", "w") as f:
    json.dump({"rmsle": rmsle}, f)
    f.write("\n")
