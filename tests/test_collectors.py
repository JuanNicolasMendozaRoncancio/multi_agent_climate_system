from src.database.mongodb_client import get_collection
from src.agents.collector_agent import CollectorAgent


def test_collector_newsapi():
    agent = CollectorAgent("test_collection")

    inserted_count = agent.collect_newsapi()
    print("Number of articles collected:", inserted_count)

def test_collector_rss():
    agent = CollectorAgent("test_collection")

    feed_url = "http://feeds.bbci.co.uk/news/science_and_environment/rss.xml"

    inserted_count = agent.collect_rss(feed_url)
    print("Number of RSS items collected:", inserted_count)


test_collector_rss()
test_collector_newsapi()