from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test_topic_replay',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='replay-test-group'
)

print("Connected to Kafka")

for message in consumer:
    print(
        f"Received: {message.value.decode()} "
        f"(Offset: {message.offset})"
    )