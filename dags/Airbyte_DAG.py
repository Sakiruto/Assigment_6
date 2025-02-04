from airflow import DAG
from airflow.operators.python import PythonOperator, ExternalPythonOperator
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
    "Airbyte_DAG",
    default_args=default_args,
    description="This is a DAG written for basic testing",
    schedule_interval=timedelta(hours=6),
    start_date=datetime(2025, 2, 1),
    catchup=False,
)
# def hello_world():
#     import airbyte as ab  
#     results = ab.get_available_connectors()
#     print(results)


def hello_world():
    print("Hello World")

def Test_Airbyte():
    import airbyte as ab
    results = ab.get_available_connectors()
    print(results)


task1 = PythonOperator(
    task_id="Print_Hello_World",
    python_callable=hello_world,
    dag=dag,
)

task2 = ExternalPythonOperator(
    task_id="Testing_External_Airbyte",
    python_callable=Test_Airbyte,
    python="/home/hp/Documents/zello_intern/Assignment_6/airflow/pyairbyte-venv/bin/python",  # Relative path to the virtual environment's Python
    dag=dag, 
)


task1 >> task2
