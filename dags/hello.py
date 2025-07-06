# Import module
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define DAG
dag = DAG(
    dag_id="hello_world_ikhsan",
    description='Hello World',
    schedule_interval='@daily',
    start_date=datetime(2025, 7, 6),
    catchup=False,
    tags=['ikhsan']
)

# Define Task
def print_hello():
    return 'Hello World'

task_helllo = PythonOperator(
    task_id = 'print_hello',
    python_callable=print_hello,
    dag=dag
)

# Define Dependency
task_helllo