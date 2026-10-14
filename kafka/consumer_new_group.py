from kafka import KafkaConsumer


consumer = KafkaConsumer(
    'test_topic_persistence',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='persistence-test-group-2'
)

print("Connected to Kafka")


for message in consumer:
    print(
        f"Received: {message.value.decode()} "
        f"(Offset: {message.offset})"
    )