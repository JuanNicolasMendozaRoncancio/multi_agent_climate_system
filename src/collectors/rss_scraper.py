import feedparser

def fetch_rss_feed(url):    
    """
    Fetch and parse an RSS feed.

    Parameters:
        url (str): The URL of the RSS feed.
    Returns:
        list: A list of entries from the RSS feed.
    """
    feed = feedparser.parse(url)
    articles = []
    
    for entry in feed.entries:
        articles.append({
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "published": entry.get("published", ""),
            "summary": entry.get("summary", "")
        })
    return articles