#shell script to run a Kafka producer and consumer

#!/bin/bash

#download kafka if not already present
if [ ! -d "kafka_2.13-3.8.0" ]; then
  echo "Kafka not found, downloading..."
  wget https://downloads.apache.org/kafka/3.8.0/kafka_2.13-3.8.0.tgz
  tar -xzf kafka_2.13-3.8.0.tgz
else
  echo "Kafka already downloaded."
fi

#extract kafka from the downloaded tar file
tar -xzf kafka_2.13-3.8.0.tgz

#navigate to the Kafka directory
cd kafka_2.13-3.8.0

#generate a cluster id that will uniquely identify the Kafka cluster
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"

#KRaft requires the log directories to be configured. Run the following command to configure the log directories passing the cluster ID.
bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties

#Now that KRaft is configured, you can start the Kafka server by running the following command.
bin/kafka-server-start.sh config/kraft/server.properties

#You can be sure that the Kafka server has started 
#when the output displays messages like "Kafka Server started".

#Exercise 3: Create a topic and start producer

#Start a new terminal and change to the kafka_2.13-3.8.0 directory.
cd kafka_2.13-3.8.0

# To create a topic named news, run the command below.
bin/kafka-topics.sh --create --topic news --bootstrap-server localhost:9092

# To verify that the topic was created, run the command below.
bin/kafka-topics.sh --list --bootstrap-server localhost:9092

#You need a producer to send messages to Kafka. Run the command below to start a producer.
bin/kafka-console-producer.sh   --bootstrap-server localhost:9092   --topic news
#You can now type messages into the terminal, and they will be sent to the Kafka topic named "news".


#Exercise 4: Start Consumer

# Start a new terminal and change to the kafka_2.13-3.8.0 directory.

cd kafka_2.13-3.8.0

# Run the command below to listen to the messages in the topic news.
bin/kafka-console-consumer.sh   --bootstrap-server localhost:9092   --topic news   --from-beginning


#Exercise 5: Explore Kafka directories
#Start a new terminal and navigate to the kafka_2.13-3.8.0 directory.
cd kafka_2.13-3.8.0

#Notice there is a tmp directory. The kraft-combine-logs inside the tmp directory contains all the logs. To check the logs generated for the topic news run the following command:
ls /tmp/kraft-combined-logs/news-0

#You can also view the contents of the log file using the command below:
cat /tmp/kraft-combined-logs/news-0/0000000000000000000000000000000000.log
