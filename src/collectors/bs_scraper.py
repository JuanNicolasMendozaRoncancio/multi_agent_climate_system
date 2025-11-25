import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
}

def scrape_static_page(url):
    
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    
    paragraphs = [p.get_text() for p in soup.find_all('p')]
    text = '\n'.join(paragraphs) if paragraphs else ""

    return {"html": response.text, "text": text}