
from kafka import KafkaProducer

print("Starting producer...")

producer = KafkaProducer(
    bootstrap_servers='localhost:9092'
)

print("Producer connected")

messages = [
    "Message 1",
    "Message 2",
    "Message 3",
    "Message 4",
    "Message 5"
]

for message in messages:
    producer.send(
        'test_topic_persistence',
        value=message.encode()
    )
    print(f"Sent: {message}")

producer.flush()
print("Messages sent")

producer.close()
print("Producer closed")