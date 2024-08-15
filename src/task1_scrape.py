import requests
from bs4 import BeautifulSoup


def scrape_webpage(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('h2')  # Modify this according to the target webpage

    return [item.get_text(strip=True) for item in items]


if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/Web_scraping'  # Replace with the actual URL
    items = scrape_webpage(url)
    for item in items:
        print(item)
