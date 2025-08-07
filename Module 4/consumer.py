#import required libraries
from kafka import KafkaConsumer

# Create a Kafka consumer to read messages from the 'bankbranch' topic
# Set group_id to None to avoid committing offsets
consumer = KafkaConsumer('bankbranch',
                        group_id=None,
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset = 'earliest')

# Print a greeting and the consumer object
print("Hello")
print(consumer)

# Continuously read messages from the topic and print them
print("Reading messages from 'bankbranch' topic:")
for msg in consumer:
    print(msg.value.decode("utf-8"))