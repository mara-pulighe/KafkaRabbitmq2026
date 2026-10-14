from kafka import KafkaProducer


producer = KafkaProducer(
    bootstrap_servers='localhost:9092'
)

print("Connected to Kafka")


producer.send(
    'test_topic',
    b'Hello from Kafka'
)

# Wait for pending messages to be sent
producer.flush()

print("Message sent")


producer.close()