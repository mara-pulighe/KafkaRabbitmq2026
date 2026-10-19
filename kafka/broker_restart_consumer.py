from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test_topic_broker_restart',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='broker-restart-verification-group_id'
)

print("Connected to Kafka")

for message in consumer:
    print(
        f"Received: {message.value.decode()} "
        f"(Offset: {message.offset})"
    )