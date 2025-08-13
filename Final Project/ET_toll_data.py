from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta


# default arguments

default_args = {
    'owner' : 'Musharraf',
    'start_date' : days_ago(0),
    'email' : 'datawithmush@gmail.com',
    'email_on_failure' : True,
    'email_on_retry' : True, 
    'retries' : 1,
    'retry_delay' : timedelta(minutes=5),
}

#define dag 

dag = DAG(
    'ETL_toll_data',
    schedule_interval = timedelta(days=1),
    default_args = default_args,
    description = 'Apache Airflow Final Assignment'
)

# create tasks

unzip_data = BashOperator(
    task_id = 'unzip_data',
    bash_command = 'tar -xzf /home/project/airflow/dags/finalassignment/tolldata.tgz -C ./',
    dag = dag
)

extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command="cut -d',' -f1,2,3,4 vehicle-data.csv | tr -d '\r' > csv_data.csv",
    dag=dag,
)

extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command="cut -d$'\t' -f5,6,7 tollplaza-data.tsv | tr '\t' ',' | tr -d '\r' > tsv_data.csv",
    dag=dag,
)

extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command="cut -c 59-61,62-67 payment-data.txt | tr ' ' ',' | tr -d '\r' > fixed_width_data.csv",
    dag=dag,
)

consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command="paste -d',' csv_data.csv tsv_data.csv fixed_width_data.csv > extracted_data.csv",
    dag=dag,
)

transform_data = BashOperator(
    task_id = 'transform_data',
    bash_command = "cut -f4 < extracted_data.csv | tr [a-z] [A-Z] > transformed_data.csv",
    dag=dag,
)

#task pipeline

unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> \
extract_data_from_fixed_width >> consolidate_data >> transform_data