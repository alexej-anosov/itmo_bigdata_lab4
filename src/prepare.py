import pandas as pd
from datetime import datetime


df = pd.read_csv('src/data/dataset.csv')
df['year'] = df['datetime'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S').year)
df['month'] = df['datetime'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S').month)
df['day'] = df['datetime'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S').day)
df['hour'] = df['datetime'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S').hour)


train = df[df['day']<15]
test = df[df['day']>=15]


train.to_csv('src/data/train.csv')
test.to_csv('src/data/test.csv')
