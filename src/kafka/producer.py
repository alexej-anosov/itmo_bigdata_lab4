from confluent_kafka import Producer
import json

class KafkaProducer:
    def __init__(self, servers: str):

        self.producer_conf = {
            'bootstrap.servers': servers
        }
        self.producer = Producer(self.producer_conf)


    def delivery_report(self, err, msg):
        if err is not None:
            print(f"Message delivery failed: {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


    async def send(self, topic: str, data: dict):

        message = json.dumps(data)
        self.producer.produce(topic, value=message, callback=self.delivery_report)
        self.producer.flush()
