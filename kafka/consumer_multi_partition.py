from kafka import KafkaConsumer


consumer = KafkaConsumer(   
    'test_topic_multi', 

    bootstrap_servers='localhost:9092',

    auto_offset_reset='earliest',

    group_id='test-group' 
)

print("Connected to Kafka")

#ascolto continuo dei messaggi
for message in consumer:

    print(f"Received: {message.value.decode()}")