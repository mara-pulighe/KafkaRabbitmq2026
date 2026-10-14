from kafka import KafkaConsumer
import time

consumer = KafkaConsumer(
    'test_topic_consumer_recovery',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='consumer-recovery-group',
    enable_auto_commit=False # Disable automatic offset commits
)

print("Connected to Kafka")

for message in consumer:

    print(f"Received: {message.value.decode()}")
    print("Processing...")

    time.sleep(30)
# Commit the offset after processing is complete
    consumer.commit()

    print("Offset committed")