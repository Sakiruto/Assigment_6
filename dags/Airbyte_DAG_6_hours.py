from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Define default arguments
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["shrishvesh.reddy@hellozelo.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    "Airbyte_DAG_6_hours",
    default_args=default_args,
    description="This is a DAG written for basic testing that runs every 6 hours",
    schedule_interval=timedelta(hours=6),
    start_date=datetime(2025, 2, 1),
    catchup=False,
)

# Example task
def example_task():
    print("Task executed successfully.")

# Add the PythonOperator to the DAG
task = PythonOperator(
    task_id="example_task",
    python_callable=example_task,
    dag=dag,
)
