from kafka import KafkaProducer

#connessione al broker Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092'
)

print("Connected to Kafka")

#messaggio nel topic
producer.send(
    'test_topic',
    b'Hello from Kafka'
)

#forza l'invio immediato
producer.flush()

print("Message sent")

#chiusura producer
producer.close()