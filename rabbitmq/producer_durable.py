import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
) 

channel = connection.channel()  

# Declare a durable queue that survives broker restarts
channel.queue_declare(
    queue='test_queue_durable',
    durable=True
)

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
        routing_key='test_queue_durable',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2  # Mark the message as persistent
        )
    )

    print(f"Sent: {message}")

connection.close()
