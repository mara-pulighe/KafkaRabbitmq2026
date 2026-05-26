import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue='test_queue')

messages = [
    "Message 1",
    "Message 2",
    "Message 3",
    "Message 4",
    "Message 5"
]

for message in messages:

    channel.basic_publish(
        exchange='',
        routing_key='test_queue',
        body=message
    )

    print(f"Sent: {message}")

connection.close()

#in questo caso il producer genera più eventi e il consumer processa sequenzialmente 