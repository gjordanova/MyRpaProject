# src/utils/helpers.py
import os
import json

from config.settings import RAW_OUTPUT, PROCESSED_OUTPUT, REPORT_OUTPUT_DIR

def get_output_paths():
    os.makedirs(os.path.dirname(RAW_OUTPUT), exist_ok=True)
    os.makedirs(os.path.dirname(PROCESSED_OUTPUT), exist_ok=True)
    os.makedirs(REPORT_OUTPUT_DIR, exist_ok=True)
    return {
        "raw": RAW_OUTPUT,
        "processed": PROCESSED_OUTPUT,
        "report_dir": REPORT_OUTPUT_DIR,
    }

def save_raw(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
