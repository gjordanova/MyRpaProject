import os
import json
import pandas as pd


def get_project_root() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)
    return path


def get_output_paths():
    root = get_project_root()
    outputs = os.path.join(root, "outputs")
    raw_dir = ensure_dir(os.path.join(outputs, "raw"))
    processed_dir = ensure_dir(os.path.join(outputs, "processed"))
    reports_dir = ensure_dir(os.path.join(outputs, "reports"))
    return {
        "raw":  os.path.join(raw_dir, "raw_data.json"),
        "processed": os.path.join(processed_dir, "processed_data.csv"),
        "reports": reports_dir,  # или os.path.join(reports_dir, "report.pdf")
    }


def save_raw(data: dict, path: str):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_raw(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_processed(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)


def save_report(df: pd.DataFrame, report_dir: str, name: str):
    path = os.path.join(report_dir, f"{name}.xlsx")
    df.to_excel(path, index=False)
    return path
