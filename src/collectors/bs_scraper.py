import requests
from bs4 import BeautifulSoup
from src.utils.paywall_detector import detect_paywall

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
}

def scrape_static_page(url):

    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()

    html = response.text

    scraped = scrape_static_page(url)

    if detect_paywall(scraped["html"]):
        return None
    
    soup = BeautifulSoup(html, 'html.parser')
    
    title = soup.title.string if soup.title else ""

    paragraphs = [p.get_text() for p in soup.find_all('p')]
    text = '\n'.join(paragraphs) if paragraphs else ""

    return {"title": title, "html": response.text, "text": text}