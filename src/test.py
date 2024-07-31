import pandas as pd
from sklearn.metrics import root_mean_squared_log_error
import pickle
import json
import argparse
import yaml


class Tester:
    def __init__(self, config_path):
        with open(config_path, "r") as file:
            params = yaml.safe_load(file)
        
        self.test_dataset = pd.read_csv(params['test_path'])
        with open(params['model_path'], 'rb') as f:
            self.model = pickle.load(f)
        self.metric_path = params['metric_path']

    def test(self):
        X_test = self.test_dataset.drop(['datetime', 'count', 'casual', 'registered'], axis=1)
        y_test = self.test_dataset['count']
        predictions = self.model.predict(X_test)
        predictions = [max(0, x) for x in predictions]

        rmsle = root_mean_squared_log_error(y_test, predictions)

        with open(self.metric_path, "w") as f:
            json.dump({"rmsle": rmsle}, f)
            f.write("\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run test pipeline using yaml-config.")
    parser.add_argument(
        "--config_path", type=str, required=True, help="Path to yaml-config."
    )
    config_path = parser.parse_args().config_path
    Tester(config_path).test()