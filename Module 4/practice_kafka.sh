# weather data producer and consumer on kafka

# Make sure that the Kafka server is still running. Change to the kafka_2.13-3.8.0 directory and run the following command:
cd kafka_2.13-3.8.0
bin/kafka-topics.sh --create --topic weather --bootstrap-server localhost:9092

#Post messages to the topic weather.
bin/kafka-console-producer.sh   --bootstrap-server localhost:9092   --topic weather

# Read the messages from the topic weather.
bin/kafka-console-consumer.sh   --bootstrap-server localhost:9092   --topic weather

# To explore the Kafka directories, you can list the contents of the logs directory.
ls -l logs

