from src.collectors.playwright_scraper import scrape_dynamic_page
from src.collectors.bs_scraper import scrape_static_page
from src.database.mongodb_client import get_collection
from src.database.schemas import raw_document


class CollectorAgent:
    def __init__(self, collection_name: str):
        self.collection = get_collection(collection_name)

    def collect_static(self, url: str, source: str = "generic"):

        scraped = scrape_static_page(url)
        document = raw_document(
            source=source,
            url=url,
            text=scraped["text"],
            html=scraped["html"],
            metadata={"scraper": "bs4"}
        )
        return self.collection.insert_one(document).inserted_id
    
    def collect_dynamic(self, url: str, source: str = "generic", wait_for_selector: str = "body"):
        data = scrape_dynamic_page(url, wait_for_selector=wait_for_selector)
        document = raw_document(
            source=source,
            url=url,
            text=data["text"],
            html=data["html"],
            metadata={"scraper": "playwright"}
        )
        return self.collection.insert_one(document).inserted_id