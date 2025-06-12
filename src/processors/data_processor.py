# src/processors/data_processor.py

import pandas as pd

def process_data():
    """
    - Чита books.csv
    - Го конвертира price од string во float
    - Го екстрахира бројот на достапни книги од availability
    - Ги пресметува просечната цена и вкупниот број книги по category
    - Ги чува два резултати:
        * processed_books.csv (целосен „clean“ DataFrame)
        * summary_by_category.csv (агрегиран извештај)
    """

    # 1. Читање на суровиот CSV
    df = pd.read_csv('books.csv')

    # 2. Конверзија на price: тргни '£' и преведи во float
    df['price'] = df['price'].str.replace('£', '', regex=False).astype(float)

    # 3. Извлекување на бројот од availability (на пример "In stock (22 available)")
    df['in_stock'] = (
        df['availability']
          .str.extract(r'(\d+)', expand=False)
          .astype(int)
    )

    # 4. Пресметки по category
    summary = (
        df
        .groupby('category')
        .agg(
            book_count=('title', 'count'),
            avg_price=('price', 'mean'),
            total_stock=('in_stock', 'sum'),
        )
        .reset_index()
        .sort_values('avg_price', ascending=False)
    )

    # 5. Зачувување на резултатите
    df.to_csv('processed_books.csv', index=False, encoding='utf-8')
    summary.to_csv('summary_by_category.csv', index=False, encoding='utf-8')

    # 6. Приказ на краток извештај во лог
    print(f"Processed {len(df)} records")
    print("Top categories by average price:")
    print(summary.head(5).to_string(index=False))
