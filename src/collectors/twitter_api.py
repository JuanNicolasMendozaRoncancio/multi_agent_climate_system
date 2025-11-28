import requests
import os
from dotenv import load_dotenv

load_dotenv()
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

def fetch_tweets(query, max_results=10):
    """
    Fetch recent tweets from Twitter API v2.

    Parameters:
        query (str): The search query to filter tweets.
        max_results (int): Maximum number of results to return (up to 100).
    Returns:
        list: A list of tweets matching the query.
    """
    url = "https://api.twitter.com/2/tweets/search/recent"
    headers = {
        "Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"
    }
    params = {
        "query": query,
        "max_results": max_results,
        "tweet.fields": "created_at,author_id,text"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        return []