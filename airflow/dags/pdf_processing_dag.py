from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def extract_data(**kwargs):
    # Code for extracting data
    print("Extracting data...")

def validate_data(**kwargs):
    # Code for data validation
    print("Validating data...")

def load_data_to_snowflake(**kwargs):
    # Code for loading data to Snowflake
    print("Loading data to Snowflake...")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 20),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG('pdf_processing_pipeline', default_args=default_args, schedule_interval=None) as dag:
    start_task = DummyOperator(task_id='start_task')
    
    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
        provide_context=True
    )
    
    validate_task = PythonOperator(
        task_id='validate_data',
        python_callable=validate_data,
        provide_context=True
    )
    
    load_task = PythonOperator(
        task_id='load_data_to_snowflake',
        python_callable=load_data_to_snowflake,
        provide_context=True
    )

    start_task >> extract_task >> validate_task >> load_task
