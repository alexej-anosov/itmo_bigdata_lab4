import asyncio
from consumer import KafkaConsumer

# Initialize the KafkaConsumer
kafka_consumer = KafkaConsumer(
    servers='kafka:9092',  # Kafka service inside Docker network
    group_id='save_to_db_group',
    topic='save_to_db'
)

# Main function to run the consumer
async def main():
    await kafka_consumer.consume()

if __name__ == '__main__':
    # Start the consumer
    asyncio.run(main())