# this bash script is used to extract and transform data using cut and tr commands

#! /bin/bash

# Extraction phase, from /etc/passwd file

cut -d":" -f1,3,6 /etc/passwd > extracted_data.txt

# Transformation phase, the original file is delimmited by ":", we will convert it to a CSV format
tr ":" "," < extracted_data.txt > transformed_data.csv

# Export the data to the pgsql using psql command
#first we need to give our password to a variable
export PGPASSWORD='your_password_here'
echo "\c <database_name>;\COPY users FROM '/path/to/transformed_data.csv' DELIMITER ',' CSV;" | psql --username=<username> --host=<hostname>

echo "Data extraction and transformation completed successfully."
# Note: Replace <database_name>, <username>, and <hostname> with your actual database
# credentials and paths.

# see a sample query to verify the data in the database
echo "Verifying data in the database..."
echo "SELECT * FROM users;" | psql --username=postgres --host=postgres template1

