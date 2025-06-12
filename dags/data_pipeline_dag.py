from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

from config.settings import BASE_URL
from src.utils.helpers import get_output_paths
from src.scrapers.books_scraper import scrape_books
from src.processors.data_processor import process_data
from src.validators.data_validator import validate_data
from src.reporters.report_generator import generate_report

paths = get_output_paths()

default_args = {
    "owner": "you",
    "depends_on_past": False,
    "retries": 1,
}

with DAG(
    dag_id="data_pipeline",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    t1 = PythonOperator(
        task_id="scrape_books",
        python_callable=lambda: scrape_books(BASE_URL, paths["raw"]),
    )
    t2 = PythonOperator(
        task_id="process_data",
        python_callable=lambda: process_data(paths["raw"], paths["processed"]),
    )
    t3 = PythonOperator(
        task_id="validate_data",
        python_callable=lambda: validate_data(paths["processed"]),
    )
    t4 = PythonOperator(
        task_id="generate_report",
        python_callable=lambda: generate_report(paths["processed"], paths["reports"]),
    )

    t1 >> t2 >> t3 >> t4
