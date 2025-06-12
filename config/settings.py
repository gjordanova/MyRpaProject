# config/settings.py

import os
from pathlib import Path

# 1. Root на проектот (две нивоа нагоре од оваа датотека)
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Базна URL за scrape
BASE_URL = "https://books.toscrape.com/"

# 3. Главна папка каде што одат сите output-и
OUTPUT_DIR = BASE_DIR / "outputs"

# 4. Подпапки за raw, processed и reports
RAW_DIR       = OUTPUT_DIR / "raw"
PROCESSED_DIR = OUTPUT_DIR / "processed"
REPORTS_DIR   = OUTPUT_DIR / "reports"

# 5. Проверка и евентуално создавање на папките при старт
for folder in (RAW_DIR, PROCESSED_DIR, REPORTS_DIR):
    os.makedirs(folder, exist_ok=True)
