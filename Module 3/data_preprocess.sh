# shell script to download and clean the log data 


#!/bin/bash

# Download the web server access log file
#curl -o 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt'

# the text file is # delimitted, change it to , delimitted
# select the timestamp and visitorid columns

cut -d":" -f1,4 web-server-access-log.txt | tr "#" "," >> web-server-access-log.csv

#capitalzed the visitorid column

cut -d"," -f2 web-server-access-log.csv | tr [a-z] [A-Z] >> web-server-access-log.csv


