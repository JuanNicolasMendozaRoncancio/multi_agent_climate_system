import requests
import os
from dotenv import load_dotenv

load_dotenv()
NEWSAPI_API_KEY = os.getenv("NEWSAPI_API_KEY")

BASE_URL = "https://newsapi.org/v2/"

def fetch_top_headlines(query=None, country=None, category=None, page_size=20):
    """
    Fetch top headlines from NewsAPI.

    Parameters:
        query (str): Keywords or phrases to search for.
        country (str): 2-letter ISO 3166-1 code of the country you want to get headlines for.
        category (str): Category you want to get headlines for.
        page_size (int): Number of results to return per page.

    Returns:
        dict: JSON response from NewsAPI containing top headlines.
    """
    url = f"{BASE_URL}top-headlines"
    params = {
        "apiKey": NEWSAPI_API_KEY,
        "q": query,
        "country": country,
        "category": category,
        "pageSize": page_size
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()  

    data = response.json()
    return data.get("articles", [])