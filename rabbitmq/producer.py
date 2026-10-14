import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue='test_queue')

# Define the message payload
message = "Hello from RabbitMQ" 

# Publish the message to the exchange
# The default exchange routes the message to the queue specified by the routing key
channel.basic_publish( 
    exchange='', 
    routing_key='test_queue',
    body=message
)

print(f"Sent: {message}")

connection.close()

# Represents the component that generates messages and introduces them into the messaging system