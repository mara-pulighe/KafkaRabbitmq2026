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
# Simulate a long-running message-processing task
    print("Simulating long processing...")
    time.sleep(30)

    print("Processing completed")
# Acknowledge the message only after processing is complete
    ch.basic_ack(
        delivery_tag=method.delivery_tag
    )

    print("ACK sent")
# Register the consumer with manual message acknowledgements
channel.basic_consume(
    queue='test_queue_recovery',
    on_message_callback=callback,
    auto_ack=False
)

print("Waiting for messages...")

channel.start_consuming()

