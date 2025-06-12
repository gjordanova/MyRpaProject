# src/scrapers/books_scraper.py
import logging
import requests
import pandas as pd
from bs4 import BeautifulSoup

from src.utils.helpers import get_output_paths, save_raw
from config.settings import BASE_URL

def scrape_books(**kwargs):
    paths = get_output_paths()
    raw_path = paths["raw"]

    books = []
    page = 1
    while True:
        url = BASE_URL.rstrip("/") + f"/catalogue/page-{page}.html"
        logging.info(f"Fetching page {page}: {url}")
        r = requests.get(url)
        if r.status_code != 200:
            logging.info(f"Page {page} returned {r.status_code}, stopping.")
            break
        soup = BeautifulSoup(r.text, 'html.parser')
        items = soup.select('.product_pod')
        if not items:
            logging.info(f"No products on page {page}, stopping.")
            break
        for item in items:
            title = item.h3.a['title']
            price = item.select_one('.price_color').text
            stock = item.select_one('.availability').text.strip()
            rating = item.p['class'][1]
            category = soup.select_one('ul.breadcrumb li:nth-child(3) a').text
            books.append({
                'title': title,
                'price': price,
                'stock': stock,
                'rating': rating,
                'category': category,
            })
        page += 1

    # зачување raw data JSON
    save_raw(books, raw_path)

    # и како CSV за процесирање
    df = pd.DataFrame(books)
    df.to_csv(paths["processed"], index=False)
    logging.info(f"Scraped {len(books)} books.")
