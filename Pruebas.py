import random
import requests
from bs4 import BeautifulSoup


NITTER_INSTANCE = "https://nitter.net"
queres = ["climate change crisis", "global warming effects", 
          "climate action now","sustainable living tips"]
query = random.choice(queres)

url = f"{NITTER_INSTANCE}/search?f=tweets&q={query.replace(' ', '+')}"

print(f"Fetching tweets from url: {url}")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
}

response = requests.get(url, headers=HEADERS, timeout=10)

print("Status:", response.status_code)
print("Headers:", response.headers)
print("Length:", len(response.text))
print("Text:", response.text[:200])

soup = BeautifulSoup(response.text, "html.parser")
print("soup:", soup.prettify()[:1000])  

tweets = []

# for item in soup.select(".timeline-item"):
#     print("item:", item)
#     content_div = item.select_one(".tweet-content.media-body")
#     if content_div:
#         text = content_div.get_text(" ", strip=True)
#         tweets.append(text)

#     if len(tweets) >= 5:
#         break

# print("Query:", query)
# print("Tweets found:", len(tweets))
# for t in tweets:
#     print("-", t)
