# src/validators/data_validator.py
import pandas as pd
import logging
from src.utils.helpers import get_output_paths

def validate_data(**kwargs):
    paths = get_output_paths()
    df = pd.read_csv(paths["processed"])

    # Пример валидации: нема празни title, price > 0
    assert df['title'].notnull().all(), "Null title found"
    assert (df['price'] > 0).all(), "Non-positive price found"

    logging.info("Data validation passed.")
