import feedparser
from email.utils import parsedate_to_datetime
from src.database.mongodb_client import db

from src.collectors.bs_scraper import scrape_static_page
from src.database.schemas import raw_article_schema

url = "https://www.theguardian.com/environment/rss"
feed = feedparser.parse(url)
articles = []
    
for entry in feed.entries:
        articles.append({
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "published": parsedate_to_datetime(entry.get("published", "")) if entry.get("published", "") else None,
            "summary": entry.get("summary", "")
        })

print(f"Number of articles fetched: {len(articles)}")
print("First article:", articles[0] if articles else "No articles found")

scraped = scrape_static_page(articles[0]["link"])
scraper_used = "bs_scraper"
html = scraped["html"]
text = scraped["text"]

article = raw_article_schema(
        url=url,
        text=text,
        html=html,
        title=articles[0]["title"],
        source="rss_feed",
        scraper_used=scraper_used,
        parent_id=None,
        published_at=articles[0]["published"]
    )

db.raw.insert_one(article)