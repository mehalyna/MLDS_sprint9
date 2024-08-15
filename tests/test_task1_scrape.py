import pytest
from src.task1_scrape import scrape_webpage

def test_scrape_webpage():
    url = 'https://en.wikipedia.org/wiki/Web_scraping'  # Use a test URL or mock it
    items = scrape_webpage(url)

    assert isinstance(items, list), "Items should be a list"
    assert len(items) > 0, "No items were scraped"

