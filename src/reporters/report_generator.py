# src/reporters/report_generator.py
import pandas as pd
import logging
from datetime import datetime
from src.utils.helpers import get_output_paths

def generate_report(**kwargs):
    paths = get_output_paths()
    df = pd.read_csv(paths["processed"])

    # Пример извештај: групирај по category
    report = df.groupby('category').size().reset_index(name='count')
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    out_file = f"{paths['report_dir']}/report_{timestamp}.csv"
    report.to_csv(out_file, index=False)

    logging.info(f"Report generated at {out_file}")
