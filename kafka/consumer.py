from kafka import KafkaConsumer


consumer = KafkaConsumer(   
    'test_topic', # Subscribe to the topic and read events from its log

    bootstrap_servers='localhost:9092',

    auto_offset_reset='earliest', # Start from the earliest available offset if no valid offset is committed

    group_id='test-group' # Identify the consumer group
)

print("Connected to Kafka")


for message in consumer:

    print(f"Received: {message.value.decode()}")