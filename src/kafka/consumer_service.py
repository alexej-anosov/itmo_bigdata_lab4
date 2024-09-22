import asyncio
from consumer import KafkaConsumer


kafka_consumer = KafkaConsumer(
    servers='kafka:9092',  
    group_id='save_to_db_group',
    topic='save_to_db'
)

async def main():
    await kafka_consumer.consume()

if __name__ == '__main__':
    asyncio.run(main())