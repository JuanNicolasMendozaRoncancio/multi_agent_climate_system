from src.collectors.playwright_scraper import scrape_dynamic_page
from src.collectors.bs_scraper import scrape_static_page
from src.database.mongodb_client import get_collection
from src.collectors.newsapi_client import fetch_top_headlines
from src.collectors.rss_scraper import fetch_rss_feed
from src.collectors.twitter_api import fetch_tweets
from src.database.schemas import RawDocument
from src.utils.logger import logger



class CollectorAgent:

    def __init__(self, collection_name: str):
        self.collection = get_collection(collection_name)
    
    def collect_static(self, url: str, source: str = "generic"):

        scraped = scrape_static_page(url)

        if scraped is None:
            return None
        
        document = RawDocument(
            source=source,
            title=scraped.get("title"),
            content=scraped.get("text", ""),
            url=url,
            raw_metadata={
                "scraper": "bs4",
                "html": scraped.get("html")
            }
        )

        inserted_id = self.collection.insert_one(document.to_mongo()).inserted_id
        return inserted_id

    def collect_dynamic(self, url: str, source: str = "generic", wait_for_selector: str = "body"):

        data = scrape_dynamic_page(url, wait_for_selector=wait_for_selector)

        
        document = RawDocument(
            source=source,
            title=data.get("title"),
            content=data.get("text", ""),
            url=url,
            raw_metadata={
                "scraper": "playwright",
                "html": data.get("html")
            }
        )

        inserted_id = self.collection.insert_one(document.to_mongo()).inserted_id
        return inserted_id
    

    
    def collect_newsapi(self):


        articles = fetch_top_headlines()
        inserted = 0

        for url in articles:
            
            data = scrape_dynamic_page(url, wait_for_selector="body")

            if data is None:
                continue
            
            document = RawDocument(
                source="newsapi",
                title=data.get("title"),
                content=data.get("text", ""),
                url=url,
                raw_metadata={
                    "scraper": "playwright",
                    "html": data.get("html")
                }
            )
            
            inserted_id = self.collection.insert_one(document.to_mongo()).inserted_id
            inserted += 1
       
        return inserted
    
    def collect_rss(self, feed_url: str):

        items = fetch_rss_feed(feed_url)
        inserted = 0

        for item in items:
            document = RawDocument(
                source="rss_feed",
                title=item.get("title", ""),
                url=item.get("link", ""),
                content=item.get("summary", ""),
                published_at=item.get("published", None),
                raw_metadata=item
            )

            self.collection.insert_one(document.to_mongo())
            inserted += 1
        return inserted
    
    def collect_twitter(self, query: str = "climate change", max_results: int = 10):
        tweets = fetch_tweets(query=query, max_results=max_results)
        inserted = 0

        for tweet in tweets:
            document = RawDocument(
                source="twitter",
                title = None,
                content=tweet.get("text", ""),
                url=tweet.get("id", ""),
                published_at=tweet.get("created_at", None),
                raw_metadata=tweet
            )

            self.collection.insert_one(document.to_mongo())
            inserted += 1
        return inserted