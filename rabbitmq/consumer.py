import pika

connection = pika.BlockingConnection( #sincrono bloccante 
    pika.ConnectionParameters('localhost')
)#connettiti a RabbitMQ che gira sul mio computer

channel = connection.channel() #crea un canale di comunicazione

channel.queue_declare(queue='test_queue')#crea una queue chiamata test_queue se non esiste

#codice che verrà eseguito quando arriva un messaggio 
def callback(ch, method, properties, body):#ch è canale
    print(f"Received: {body.decode()}") #perchè rabbit manda bytes

#per restare in ascolto 
channel.basic_consume(
    queue='test_queue', #quale queue ascoltare
    on_message_callback=callback,
    auto_ack=True  #Il consumer dice a RabbitMQ “messaggio ricevuto correttamente”
)

print("Waiting for messages...")

channel.start_consuming() #blocca il programma e lo lascia in attesa permanente



#è il componente che: legge i messaggi e li processa