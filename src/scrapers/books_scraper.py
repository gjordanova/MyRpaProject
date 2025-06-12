import requests
from bs4 import BeautifulSoup
from src.utils.helpers import get_output_paths, save_raw

def scrape_books():
    base_url = "https://books.toscrape.com/"
    books = []
    page = 1

    while True:
        url = f"{base_url}catalogue/page-{page}.html"
        r = requests.get(url)
        if r.status_code != 200:
            break

        soup = BeautifulSoup(r.text, 'html.parser')
        for item in soup.select('.product_pod'):
            books.append({
                'title':    item.h3.a['title'],
                'price':    item.select_one('.price_color').text,
                'stock':    item.select_one('.availability').text.strip(),
                'rating':   item.p['class'][1],
                'category': soup.select_one('ul.breadcrumb li:nth-child(3) a').text,
            })

        page += 1


    paths = get_output_paths()
    raw_path = paths["raw"]
    save_raw(books, raw_path)
