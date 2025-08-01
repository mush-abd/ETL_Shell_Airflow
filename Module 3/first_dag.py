# This code defines a simple Airflow DAG that prints "Hello, World!" and the current date.
# The DAG is scheduled to run every 5 seconds, starting from August 1, 2025.
# It consists of two tasks: one that prints a greeting and another that prints the current date


import airflow
from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator



default_args = {
    'owner' : 'Musharraf',
    'start_date' : datetime(2025, 8, 1),
    'retries' : 1,
    'retry_delay' : timedelta(minutes=5)
}


deg = DAG(
    'my_first_dag',
    default_args=default_args,
    description = 'My first simple DAG',
    schedule = timedelta(seconds=5)
)

task1 = BashOperator(
    task_id = 'print_hello'
    bash_command = 'echo "Hello, World!, The date and times are:"',
    dag = dag,
)

task2 = BashOperator(
    task_id = 'print_date',
    bash_command = 'date',
    dag = dag,
)


task1 >> task2

