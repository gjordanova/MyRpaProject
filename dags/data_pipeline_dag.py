from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from config.settings import BASE_URL
from src.utils.helpers import get_output_paths

from src.scrapers.books_scraper import scrape_books
from src.processors.data_processor import process_data
from src.validators.data_validator import validate_data
from src.reporters.report_generator import generate_report

# Default arguments for the DAG
default_args = {
    'owner': 'you',
    'depends_on_past': False,
    'retries': 1,
}

# Instantiate the DAG
with DAG(
    dag_id='data_pipeline',
    default_args=default_args,
    description='Scrape, process, validate, and report on book data',
    start_date=datetime(2025, 1, 1),
    schedule_interval='@daily',
    catchup=False,
) as dag:

    # Retrieve configured paths for I/O
    paths = get_output_paths()

    # Task 1: Scrape books from the source URL and save raw data
    t1 = PythonOperator(
        task_id='scrape_books',
        python_callable=scrape_books,
    )

    # Task 2: Process the raw data into a cleaned CSV
    t2 = PythonOperator(
        task_id='process_data',
        python_callable=process_data,
    )

    # Task 3: Validate the processed data
    t3 = PythonOperator(
        task_id='validate_data',
        python_callable=validate_data,
    )

    # Task 4: Generate a report based on the validated data
    t4 = PythonOperator(
        task_id='generate_report',
        python_callable=generate_report,
    )

    # Define task order: scrape → process → validate → report
    t1 >> t2 >> t3 >> t4
