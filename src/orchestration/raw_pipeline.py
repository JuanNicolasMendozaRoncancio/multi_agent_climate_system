from src.database.mongodb_client import db
from src.collectors.raw_ingestor import proccess_document
from src.database.mongodb_client import get_collection
from src.database.schemas import raw_article_schema
from src.collectors.bs_scraper import scrape_static_page
from src.collectors.playwright_scraper import scrape_dynamic_page

def add_pure_static(url):

    scraped = scrape_static_page(url)

    doc = raw_article_schema(
        url=url,
        text=scraped["text"],
        html=scraped["html"],
        title=scraped["title"],
        source="pure_static_test",
        scraper_used="bs_scraper"
    )

    collection = get_collection("raw")
    collection.insert_one(doc)

def add_pure_dynamic(url):

    scraped = scrape_dynamic_page(url)

    doc = raw_article_schema(
        url=url,
        text=scraped["text"],
        html=scraped["html"],
        title=scraped["title"],
        source="pure_dynamic_test",
        scraper_used="playwright_scraper"
    )

    collection = get_collection("raw")
    collection.insert_one(doc)

def run_raw_pipeline():

    docs = db.First_injection_collection.find({"source": {"$in": ["rss_feed", "newsapi"]}})

    for doc in docs:
        try:
            proccess_document(doc)
            print(f"[OK] Procesado: {doc['url']}")
        except ValueError as e:
            print(f"Error processing article from {doc.get('url')}: {e}")


#IF you want to test the raw pipeline with pure static or dynamic pages, uncomment below:
# add_pure_dynamic("Your URLs")
# add_pure_static("Your URLs")
