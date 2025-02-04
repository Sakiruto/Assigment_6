
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Define default arguments
default_args = {
    "owner": "airflow",
    "depends_on_past": False,  # Changed from datetime to False
    "email": ["shrishvesh.reddy@hellozelo.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

# Define the DAG
dag = DAG(
    "Basic_Dag",  # DAG names should not have spaces
    default_args=default_args,
    description="This is a DAG written for basic testing",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2025, 2, 1),  # Added start_date
    catchup=False,  # Prevents running missed DAGs
)

# Define the Python function
def hello_world():
    print("Hello World")


# Define the task
task = PythonOperator(
    task_id="Print_Hello_World",  # Fixed typo: task_Id -> task_id
    python_callable=hello_world,
    dag=dag,
)
     
