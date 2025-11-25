import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
}

response = requests.get("https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss", headers=HEADERS, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
paragraphs = [p.get_text() for p in soup.find_all('p')]

print(paragraphs)
print(response.text.encode('utf-8', errors='ignore').decode('utf-8'))
