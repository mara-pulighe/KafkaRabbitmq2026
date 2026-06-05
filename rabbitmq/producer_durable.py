import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)  # connettiti a RabbitMQ

channel = connection.channel()  # crea un canale di comunicazione

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
            delivery_mode=2  # rende persistente il messaggio
        )
    )

    print(f"Sent: {message}")

connection.close()

# rappresenta il componente che genera eventi
# punto di ingresso dei messaggi nel sistema distribuito