import airflow
from airflow.models import DAG
from airflow.operators.python import PythonOperator

from datetime import timedelta
from airflow.utils.dates import days_ago

import requests

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt'
extracted_file = 'server-log-extract.txt'
transformed_file = 'server-log-transform.txt'
loaded_file = 'server-log-load.csv'
# functions for ETL

def extract():

    global url
    global extracted_file
    response = requests.get(url)
    with open(extracted_file, 'wb') as file:
        file.write(response.content)

def transform():

    global extracted_file
    global transformed_file
    with open(extracted_file, 'r') as infile, open(transformed_file, 'w') as outfile:
        for line in infile:
            # print(line)
            fields = line.strip().split("#")
            print(f'fields: {fields}')
            selected = [fields[i] for i in [0, 3]]
            output = ",".join(selected)
            # print(output)
            outfile.write(output + "\n")

def load():

    global transformed_file
    global loaded_file
    with open(transformed_file, 'r') as infile, open(loaded_file, 'w') as outfile:
        for line in infile:
            fields = line.strip().split(",")
            fields[1] = fields[1].upper()
            output = ",".join(fields)
            outfile.write(output + "\n")

def validate():
    global loaded_file
    with open(loaded_file) as infile:
        for line in infile:
            print(line)


# default args

default_args = {
    'owner' : 'Musharraf', 
    'start_date' : days_ago(0),
    'email' : ['datawithmush@gmail.com'],
    'retry_delay' : timedelta(minutes=5),
}

# DAG definition
mydag = DAG (
    'python-etl-dag',
    default_args = default_args,
    description = 'DAG to extract, transform and load server access log',
    schedule_interval = timedelta(days=1)
)


#tasks for ETL

extract_call = PythonOperator(
    task_id = 'extract',
    python_callable = extract,
    dag = mydag
)

transform_call = PythonOperator(
    task_id = 'transform',
    python_callable = transform,
    dag = mydag
)

load_call = PythonOperator(
    task_id = 'load',
    python_callable = load,
    dag = mydag

)
validate_call = PythonOperator(
    task_id = 'validate',
    python_callable = validate,
    dag = mydag
)

# Pipeline

extract_call >> transform_call >> load_call >> validate_call
# This will ensure that the tasks are executed in the order: extract -> transform -> load -> validate

if __name__ == "__main__":
    mydag.cli()  # This allows the DAG to be run from the command line for testing purposes.
