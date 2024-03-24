import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
import pickle
import yaml
import configparser

with open("params.yaml") as f:
    params = yaml.safe_load(f)

 
# params = configparser.ConfigParser() # не поддерживается dvc
# params.read('params.ini')
 

train = pd.read_csv('data/train.csv')

X_train = train.drop(['datetime', 'count', 'casual', 'registered'], axis=1)
y_train = train['count']

model = GradientBoostingRegressor(n_estimators=params["train"]["n_estimators"],
                                   learning_rate=params["train"]["learning_rate"],
                                   max_depth=params["train"]["max_depth"],
                                   random_state=params["train"]["random_state"])

# model = GradientBoostingRegressor(n_estimators=params.getint('train', 'n_estimators'),
#                                     learning_rate=params.getfloat('train', 'learning_rate'),
#                                     max_depth=params.getint('train', 'max_depth'),
#                                     random_state=params.getint('train', 'random_state'))


model.fit(X_train, y_train)


with open("data/weights.joblib", 'wb') as f:
    pickle.dump(model, f)

