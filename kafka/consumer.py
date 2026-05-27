from kafka import KafkaConsumer

#connessione al broker Kafka
consumer = KafkaConsumer(   #crea un consumer stream-based
    'test_topic', #si iscrive al topic legge eventi dal log Kafka.

    bootstrap_servers='localhost:9092',

    auto_offset_reset='earliest',

    group_id='test-group' #kafka usa consumer group
)

print("Connected to Kafka")

#ascolto continuo dei messaggi
for message in consumer:

    print(f"Received: {message.value.decode()}")