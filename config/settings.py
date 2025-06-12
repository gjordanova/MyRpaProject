# config/settings.py

import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


BASE_URL = "https://books.toscrape.com/"


OUTPUT_DIR = BASE_DIR / "outputs"


RAW_DIR       = OUTPUT_DIR / "raw"
PROCESSED_DIR = OUTPUT_DIR / "processed"
REPORTS_DIR   = OUTPUT_DIR / "reports"


for folder in (RAW_DIR, PROCESSED_DIR, REPORTS_DIR):
    os.makedirs(folder, exist_ok=True)
