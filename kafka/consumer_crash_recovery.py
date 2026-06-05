from kafka import KafkaConsumer
import time

consumer = KafkaConsumer(
    'test_topic_multi',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='manual-commit-group',
    enable_auto_commit=False
)

print("Connected to Kafka")

for message in consumer:

    print(f"Received: {message.value.decode()}")
    print("Processing...")

    time.sleep(30)

    consumer.commit()

    print("Offset committed")