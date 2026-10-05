from kafka import KafkaProducer

print("Starting producer...")

producer = KafkaProducer(
    bootstrap_servers='localhost:9092'
)

print("Producer connected")

messages = [
    "Persistence Message 1",
    "Persistence Message 2",
    "Persistence Message 3",
    "Persistence Message 4",
    "Persistence Message 5"
]

for message in messages:
    producer.send(
        'test_topic_broker_restart',
        value=message.encode()
    )
    print(f"Sent: {message}")

producer.flush()

print("Messages sent")

producer.close()

print("Producer closed")