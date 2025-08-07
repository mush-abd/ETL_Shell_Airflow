# import the necessary module

from kafka.admin import KafkaAdminClient,NewTopic

# create an instance of KafkaAdminClient
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')

# create a new topic
topic_list = []
new_topic = NewTopic(name="bankbranch", num_partitions= 2, replication_factor=1)
topic_list.append(new_topic)

# create the topic in Kafka
admin_client.create_topics(new_topics=topic_list)

