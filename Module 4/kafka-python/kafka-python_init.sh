#bash program to start a Kafka server to be used by the python kafka client

#!/bin/bash

# Check if Kafka directory exists, if not, download and extract it
if [ ! -d "kafka_2.13-3.8.0" ]; then
  echo "Kafka not found, downloading..."
  wget https://downloads.apache.org/kafka/3.8.0/kafka_2.13-3.8.0.tgz
  tar -xzf kafka_2.13-3.8.0.tgz
else
  echo "Kafka already downloaded."
fi


# change to the Kafka directory
cd kafka_2.13-3.8.0

# Generate a cluster ID that will uniquely identify the Kafka cluster
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"

# KRaft requires the log directories to be configured. Run the following command to configure the log directories passing the cluster ID.
bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft

#start the kafka server
bin/kafka-server-start.sh config/kraft/server.properties

#open a new terminal and switch to the kafka_2.13-3.8.0 directory
cd kafka_2.13-3.8.0

#download the kafka-python library if not already installed
if ! python3 -c "import kafka" &> /dev/null; then
    echo "kafka-python library not found, installing..."
    pip install kafka-python
else
    echo "kafka-python library already installed."
fi  

#create python files for admin, producer, and consumer
code kafka_admin.py
code producer.py
code consumer.py

# run the python scripts
python3 kafka_admin.py
python3 producer.py
python3 consumer.py


