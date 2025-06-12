# dags/data_pipeline_dag.py

import os, sys
# Проширување на PYTHONPATH за да може да се најдат модули во src/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

from config.settings import BASE_URL
from src.scrapers.books_scraper import scrape_books
from src.processors.data_processor import process_data
from src.validators.data_validator import validate_data
from src.reporters.report_generator import generate_report

with DAG(
    dag_id='data_pipeline',
    default_args={
        'owner': 'you',
        'depends_on_past': False,
        'retries': 1,
    },
    description='scrape → process → validate → report',
    schedule_interval='@daily',
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=['rpa'],
) as dag:

    t1 = PythonOperator(
        task_id='scrape_books',
        python_callable=scrape_books,
    )
    t2 = PythonOperator(
        task_id='process_data',
        python_callable=process_data,
    )
    t3 = PythonOperator(
        task_id='validate_data',
        python_callable=validate_data,
    )
    t4 = PythonOperator(
        task_id='generate_report',
        python_callable=generate_report,
    )

    t1 >> t2 >> t3 >> t4
