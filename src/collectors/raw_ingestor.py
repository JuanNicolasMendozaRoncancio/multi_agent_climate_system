from src.database.mongodb_client import db
from src.database.schemas import raw_article_schema
from src.collectors.bs_scraper import scrape_static_page
from src.collectors.playwright_scraper import scrape_dynamic_page


def proccess_document(doc):
    url = doc.get("url")
    parent_id = doc.get("_id")
    source = doc.get("source")
    title = doc.get("title")
    published_at = doc.get("published_at")

    if source=="rss_feed":
        scraped = scrape_static_page(url)
        scraper_used = "bs_scraper"
        html = scraped["html"]
        text = scraped["text"]

    elif source == "newsapi":
        scraped = scrape_dynamic_page(url)
        scraper_used = "playwright_scraper"
        html = scraped["html"]
        text = scraped["text"]

    
    article = raw_article_schema(
        url=url,
        text=text,
        html=html,
        title=title,
        source=source,
        scraper_used=scraper_used,
        parent_id=parent_id,
        published_at=published_at
    )

    db.raw.insert_one(article)
    return article
