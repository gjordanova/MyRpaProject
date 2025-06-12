import os

def get_output_paths(base_dir=None):
    base = base_dir or os.path.join(os.getcwd(), "outputs")
    raw = os.path.join(base, "raw", "books.csv")
    processed = os.path.join(base, "processed", "books_clean.csv")
    reports = os.path.join(base, "reports")
    for p in [os.path.dirname(raw), os.path.dirname(processed), reports]:
        os.makedirs(p, exist_ok=True)
    return {"raw": raw, "processed": processed, "reports": reports}
