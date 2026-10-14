from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092'
)

messages = [
    "Message 1",
    "Message 2",
    "Message 3",
    "Message 4",
    "Message 5"
]

for message in messages:

    producer.send(
        'test_topic_multi',
        value=message.encode()
    )

    print(f"Sent: {message}")

producer.flush()
producer.close()

