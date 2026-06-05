import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)  # connettiti a RabbitMQ che gira sul mio computer

channel = connection.channel()  # crea un canale di comunicazione

channel.queue_declare(
    queue='test_queue_durable',
    durable=True
)

# codice che verrà eseguito quando arriva un messaggio
def callback(ch, method, properties, body):
    print(f"Received: {body.decode()}")  # perché RabbitMQ manda bytes

# per restare in ascolto
channel.basic_consume(
    queue='test_queue_durable',  # quale queue ascoltare
    on_message_callback=callback,
    auto_ack=True
)

print("Waiting for messages...")

channel.start_consuming()  # blocca il programma e lo lascia in attesa permanente

# è il componente che:
# legge i messaggi e li processa