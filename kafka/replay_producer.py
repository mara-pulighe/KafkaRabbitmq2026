from kafka import KafkaProducer

print("Starting producer...")

producer = KafkaProducer(
    bootstrap_servers='localhost:9092'
)

print("Producer connected")

messages = [
    "Replay Message 1",
    "Replay Message 2",
    "Replay Message 3",
    "Replay Message 4",
    "Replay Message 5"
]

for message in messages:
    producer.send(
        'test_topic_replay',
        value=message.encode()
    )
    print(f"Sent: {message}")

producer.flush()

print("Messages sent")

producer.close()

print("Producer closed")