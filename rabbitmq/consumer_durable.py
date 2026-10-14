import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)  

channel = connection.channel() 

channel.queue_declare(
    queue='test_queue_durable',
    durable=True
)


def callback(ch, method, properties, body):
    print(f"Received: {body.decode()}")  


channel.basic_consume(
    queue='test_queue_durable',  
    on_message_callback=callback,
    auto_ack=True
)

print("Waiting for messages...")

channel.start_consuming()  