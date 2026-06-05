import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(
    queue='test_queue_recovery'
)

def callback(ch, method, properties, body):

    print(f"Received: {body.decode()}")

    print("Simulating long processing...")
    time.sleep(30)

    print("Processing completed")

    ch.basic_ack(
        delivery_tag=method.delivery_tag
    )

    print("ACK sent")

channel.basic_consume(
    queue='test_queue_recovery',
    on_message_callback=callback,
    auto_ack=False
)

print("Waiting for messages...")

channel.start_consuming()

# legge i messaggi e li processa