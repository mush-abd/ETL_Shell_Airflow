# THis is a DAG that extracts, transforms, and loads server logs using BashOperator in Apache Airflow.
#

#python library imports

import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator as BO
import requests
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago


#default arguments
default_args = {
    'owner' : 'Musharraf',
    'start_date' :days_ago(0),
    'email' : ['datawithmush@gmail.com'],
    'retry_delay' : timedelta(minutes=5),
}


#dag definition
dag = DAG(
    'Bash_Server_DAG',
    default_args = default_args,
    description = 'Extract and load server log using bash operator',
    schedule_interval = timedelta(minutes=1),

)


#tasks
extract_call = BO(
    task_id = 'extract',
        bash_command = 'wget -qO - "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt" | cut -d"#" -f1,4 | tr "#" "," >> extracted_log.txt',
        dag = dag

)

transform_call = BO(
    task_id = 'transform',
    bash_command = 'awk -F"," "{ $2 = toupper($2)}" extracted_log.txt >> transformed_log.txt',
    dag = dag
)

load_call = BO(
    task_id = 'load',
    bash_command = 'tar -cvz loaded_compressed.tar.gz transformed_log.txt',
    dag = dag
)

#dependencies

extract_call >> transform_call >> load_call