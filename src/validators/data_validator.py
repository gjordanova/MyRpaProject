# src/validators/data_validator.py

import pandas as pd
import jsonschema
from jsonschema import validate

# JSON Schema за една книга
book_schema = {
    "type": "object",
    "properties": {
        "title":        {"type": "string"},
        "price":        {"type": "number", "minimum": 0},
        "in_stock":     {"type": "integer", "minimum": 0},
        "rating":       {"type": "string"},
        "category":     {"type": "string"},
        "url":          {"type": "string", "format": "uri"}
    },
    "required": ["title", "price", "in_stock", "rating", "category", "url"]
}

# JSON Schema за резиме по категорија
summary_schema = {
    "type": "object",
    "properties": {
        "category":    {"type": "string"},
        "book_count":  {"type": "integer", "minimum": 0},
        "avg_price":   {"type": "number", "minimum": 0},
        "total_stock": {"type": "integer", "minimum": 0}
    },
    "required": ["category", "book_count", "avg_price", "total_stock"]
}

def validate_data():
    # 1) Валидација на обработените книги
    df_books = pd.read_csv('processed_books.csv')
    for i, row in df_books.iterrows():
        record = {
            "title":    row["title"],
            "price":    row["price"],
            "in_stock": int(row["in_stock"]),
            "rating":   row["rating"],
            "category": row["category"],
            "url":      row["url"]
        }
        validate(instance=record, schema=book_schema)

    # 2) Валидација на резимето по категории
    df_summary = pd.read_csv('summary_by_category.csv')
    for i, row in df_summary.iterrows():
        summary = {
            "category":    row["category"],
            "book_count":  int(row["book_count"]),
            "avg_price":   row["avg_price"],
            "total_stock": int(row["total_stock"])
        }
        validate(instance=summary, schema=summary_schema)

    print(f"Validated {len(df_books)} book records and {len(df_summary)} summary records successfully.")
