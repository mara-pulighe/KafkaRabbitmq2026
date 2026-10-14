import pika

connection = pika.BlockingConnection( 
    pika.ConnectionParameters('localhost')
)

channel = connection.channel() # Create a communication channel

channel.queue_declare(queue='test_queue')# Declare the queue; create it if it does not already exist

# Define the callback function executed when a message is received
def callback(ch, method, properties, body):
    print(f"Received: {body.decode()}") # Decode the message payload from bytes to a string

# Register the consumer to receive messages from the queue
channel.basic_consume(
    queue='test_queue', # Specify the queue to consume from
    on_message_callback=callback,
    auto_ack=True  # Automatically acknowledge each message upon delivery
)

print("Waiting for messages...")

channel.start_consuming() 



# Consumer component: receives and processes messages from the queue