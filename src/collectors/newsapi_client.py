import requests
import os
from dotenv import load_dotenv

load_dotenv()
NEWSAPI_API_KEY = os.getenv("NEWSAPI_API_KEY")

url = "https://newsdata.io/api/1/latest? apikey=pub_5d7b7057c4304ce3b29310fa4afdc1fc&q=Climate Change&country=us&language=en&category=environment&prioritydomain=top&image=0&video=0&removeduplicate=1&sort=relevancy&sort=relevancy"

def fetch_top_headlines():

    response = requests.get(url)
    response.raise_for_status()  
    links = []

    data = response.json()
    for article in data.get("results", []):
        links.append(article.get("link", ""))

    return links

