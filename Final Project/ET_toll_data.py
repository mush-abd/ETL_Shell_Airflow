from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
import os


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

project_dir = '/opt/airflow/project/' # NEW CONTAINER PATH'

# download_data = BashOperator(
#     task_id='download_data',
#     bash_command=f'sudo curl https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz -o {project_dir}/staging_area/tolldata.tgz',
#     dag=dag
# )

unzip_data = BashOperator(
    task_id = 'unzip_data',
    bash_command = f'tar -xzf {project_dir}/staging_area/tolldata.tgz -C {project_dir}/staging_area/',
    dag = dag
)

extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command= f"cut -d',' -f1,2,3,4 '{project_dir}/staging_area/vehicle-data.csv' | tr -d '\r' > {project_dir}/staging_area/csv_data.csv",
    dag=dag,
)

extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command= f"cut -d$'\t' -f5,6,7 {project_dir}/staging_area/tollplaza-data.tsv | tr '\t' ',' | tr -d '\r' > {project_dir}/staging_area/tsv_data.csv",
    dag=dag,
)

extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command= f"cut -c 59-61,62-67 {project_dir}/staging_area/payment-data.txt | tr ' ' ',' | tr -d '\r' > {project_dir}/staging_area/fixed_width_data.csv",
    dag=dag,
)

consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command= f"paste -d',' {project_dir}/staging_area/csv_data.csv {project_dir}/staging_area/tsv_data.csv {project_dir}/staging_area/fixed_width_data.csv > {project_dir}/staging_area/extracted_data.csv",
    dag=dag,
)

transform_data = BashOperator(
    task_id = 'transform_data',
    bash_command = f"cut -f4 {project_dir}/staging_area/extracted_data.csv | tr [a-z] [A-Z] > {project_dir}/transformed_data/transformed_data.csv",
    dag=dag,
)

#task pipeline

unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> \
extract_data_from_fixed_width >> consolidate_data >> transform_data