#import the necessary libraries
from kafka import KafkaProducer
import json

# create an instance of KafkaProducer
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# send some messages to the topic
producer.send("bankbranch", {'atmid':1, 'transid':100})
producer.send("bankbranch", {'atmid':2, 'transid':101})
producer.send("bankbranch", {'atmid':3, 'transid':102})
producer.send("bankbranch", {'atmid':4, 'transid':103})
producer.send("bankbranch", {'atmid':5, 'transid':104})

# wait for all messages to be sent
producer.flush()

# close the producer
producer.close()