# src/processors/data_processor.py
import pandas as pd
import logging
from src.utils.helpers import get_output_paths

def process_data(**kwargs):
    paths = get_output_paths()
    df = pd.read_csv(paths["processed"])

    # Пример процесирање: отстрани € и конвертирај price во float
    df['price'] = df['price'].str.replace('£', '').astype(float)
    df['in_stock'] = df['stock'].str.contains("In stock")
    df = df.drop(columns=['stock'])

    df.to_csv(paths["processed"], index=False)
    logging.info("Data processed and saved.")
