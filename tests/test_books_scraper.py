from scrapers.books_scraper import scrape_books
import os

def test_scrape_creates_csv(tmp_path, monkeypatch):

    monkeypatch.chdir(tmp_path)

    scrape_books()

    assert (tmp_path / 'books.csv').exists()
    df = pandas.read_csv(tmp_path / 'books.csv')
    assert 'title' in df.columns
