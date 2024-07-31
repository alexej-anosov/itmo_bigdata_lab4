import pandas as pd
from datetime import datetime
import argparse
import yaml


class SplitsCreator:
    def __init__(self, config_path):
        with open(config_path, "r") as file:
            params = yaml.safe_load(file)
            
        self.dataset_path = params['dataset_path']
        self.train_path = params['train_path']
        self.test_path = params['test_path']
        
    def split(self):
        df = pd.read_csv(self.dataset_path)
        df['year'] = df['datetime'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S').year)
        df['month'] = df['datetime'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S').month)
        df['day'] = df['datetime'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S').day)
        df['hour'] = df['datetime'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S').hour)
        train = df[df['day']<15]
        test = df[df['day']>=15]
        return train, test

    def split_and_save(self):
        train, test = self.split()
        train.to_csv(self.train_path, index=False)
        test.to_csv(self.test_path, index=False)
       

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run data preparation pipeline using yaml-config.")
    parser.add_argument(
        "--config_path", type=str, required=True, help="Path to yaml-config."
    )
    config_path = parser.parse_args().config_path
    SplitsCreator(config_path).split_and_save()
