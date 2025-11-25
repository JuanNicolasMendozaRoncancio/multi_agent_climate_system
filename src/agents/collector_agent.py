from src.collectors.bs_scraper import scrape_static_page
from src.database.mongodb_client import get_collection
from src.database.schemas import raw_document


class CollectorAgent:
    def __init__(self, collection_name: str):
        self.collection = get_collection(collection_name)

    def collect_from_url(self, url: str, source: str = "generic"):

        scraped = scrape_static_page(url)
        document = raw_document(
            source=source,
            url=url,
            text=scraped["text"],
            html=scraped["html"],
            metadata={"scraper": "bs4"}
        )

        result = self.collection.insert_one(document)
        return result.inserted_id