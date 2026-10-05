from kafka import KafkaProducer

print("Starting producer...")

producer = KafkaProducer(
    bootstrap_servers='localhost:9092'
)

print("Producer connected")

messages = [
    "Recovery Message 1",
    "Recovery Message 2",
    "Recovery Message 3",
    "Recovery Message 4",
    "Recovery Message 5"
]

for message in messages:
    producer.send(
        'test_topic_consumer_recovery',
        value=message.encode()
    )
    print(f"Sent: {message}")

producer.flush()

print("Messages sent")

producer.close()

print("Producer closed")