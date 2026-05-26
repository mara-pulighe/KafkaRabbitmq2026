import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue='test_queue')

message = "Hello from RabbitMQ" #payload, contenuto del messaggio

channel.basic_publish( #pubblica un messaggio nel broker
    exchange='', #i producer NON mandano direttamente alle queue, mandano agli exchange. L’exchange: decide dove inoltrare i messaggi
    routing_key='test_queue',
    body=message
)

print(f"Sent: {message}")

connection.close()

#rappresenta il componente che genera eventi il punto di ingresso dei messaggi nel sistema distribuito