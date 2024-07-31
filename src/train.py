import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
import pickle
import argparse
import yaml


class Trainer:
    def __init__(self, config_path):
        with open(config_path, "r") as file:
            params = yaml.safe_load(file)
        with open(params['hyperparams']) as f:
            self.hyperparams = yaml.safe_load(f)

        self.train_dataset = pd.read_csv(params['train_path'])
        self.model_path = params['model_path']

    def train(self):
        X_train = self.train_dataset.drop(['datetime', 'count', 'casual', 'registered'], axis=1)
        y_train = self.train_dataset['count']

        model = GradientBoostingRegressor(n_estimators=self.hyperparams["train"]["n_estimators"],
                                        learning_rate=self.hyperparams["train"]["learning_rate"],
                                        max_depth=self.hyperparams["train"]["max_depth"],
                                        random_state=self.hyperparams["train"]["random_state"])

        model.fit(X_train, y_train)

        with open(self.model_path, 'wb') as f:
            pickle.dump(model, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run train pipeline using yaml-config.")
    parser.add_argument(
        "--config_path", type=str, required=True, help="Path to yaml-config."
    )
    config_path = parser.parse_args().config_path
    Trainer(config_path).train()