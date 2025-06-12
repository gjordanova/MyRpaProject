# src/utils/helpers.py
import os
from config.settings import OUTPUT_DIR

def get_output_paths():
    raw = os.path.join(OUTPUT_DIR, "raw_data.json")
    processed = os.path.join(OUTPUT_DIR, "processed_data.csv")
    report = os.path.join(OUTPUT_DIR, "reports", "report.html")
    # Осигурај се дека фолдерите постојат
    os.makedirs(os.path.dirname(raw), exist_ok=True)
    os.makedirs(os.path.dirname(processed), exist_ok=True)
    os.makedirs(os.path.dirname(report), exist_ok=True)
    return {"raw": raw, "processed": processed, "report": report}

def save_raw(data, path):
    import json
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
