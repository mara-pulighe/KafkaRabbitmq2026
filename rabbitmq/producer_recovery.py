import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(
    queue='test_queue_recovery'
)

message = "Recovery Test Message"

channel.basic_publish(
    exchange='',
    routing_key='test_queue_recovery',
    body=message
)

print(f"Sent: {message}")

connection.close()

# rappresenta il componente che genera eventi
# punto di ingresso dei messaggi nel sistema distribuito