#! /bin/bash

# this script is made for a etl process that creates a access log

# run the following commmand to get the source file
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/ETL%20using%20shell%20scripting/web-server-access-log.txt.gz

# run the following sql script to create the database and table
psql -U postgres -d access_log -f access_init.sql

# uncompress the downloaded file
gunzip web-server-access-log.txt.gz

# see the data using the head command
# head -n 10 web-server-access-log.txt

# use the select columns 1-6 using the cut command for # delimmiter
cut -d"#" -f1-6 web-server-access-log.txt > extracted_data.txt

# use the tr command to convert the delimiter from # to ,
tr "#" "," < extracted_data.txt > transformed_data.csv

# load the data into the database using psql
export PGPASSWORD='your_password_here'

echo "\c access_log;\COPY access_log FROM 'transformed_data.csv' DELIMITER ',' CSV;" | psql -U postgres --host=localhost

echo "Data extraction and transformation completed successfully."

