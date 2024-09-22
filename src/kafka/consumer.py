from confluent_kafka import Consumer, KafkaError
import json
import time
import sys
sys.path.append('.')
from db import Prediction, get_session


class KafkaConsumer:
    def __init__(self, servers: str, group_id: str, topic: str):
        self.consumer_conf = {
            'bootstrap.servers': servers,
            'group.id': group_id,
            'auto.offset.reset': 'earliest'
        }
        self.consumer = Consumer(self.consumer_conf)
        self.topic = topic

    async def consume(self):

        self.consumer.subscribe([self.topic])

        try:
            
            while True:
                time.sleep(1)
                msg = self.consumer.poll(timeout=1.0)
                
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:

                        continue
                    else:
                        print(f"Error: {msg.error()}")
                        break

                data = json.loads(msg.value().decode('utf-8'))
                
                async for db in get_session():

                    new_prediction = Prediction(
                        season = data['season'],
                        holiday = data['holiday'],
                        workingday = data['workingday'],
                        weather = data['weather'],
                        temp =  data['temp'],
                        atemp =  data['atemp'],
                        humidity =  data['humidity'],
                        windspeed =  data['windspeed'],
                        year =  data['year'],
                        month =  data['month'],
                        day =  data['day'],
                        hour =  data['hour'],
                        prediction = data['result']
                    )

                    db.add(new_prediction)
                    await db.commit()

        finally:

            self.consumer.close()