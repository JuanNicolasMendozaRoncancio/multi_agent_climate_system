from src.database.mongodb_client import get_collection
from src.agents.collector_agent import CollectorAgent

def test_get_collection():
    col = get_collection("test_collection")
    result = col.insert_one({"message": "Hola Mundo desde MongoDB"})
    print("Inserted document ID:", result.inserted_id)

def test_collector_static():
    agent = CollectorAgent("test_collection")

    url = "https://climate.nasa.gov/news/3330/nasa-study-temperature-anomalies-in-2023/"

    id = agent.collect_static(url, source="nasa_climate_news")
    print("Collected document ID:", id)

def test_collector_dynamic():
    agent = CollectorAgent("test_collection")

    url = "https://www.nytimes.com/section/climate"

    id = agent.collect_dynamic(url)
    print("Collected document ID:", id)

def test_collector_newsapi():
    agent = CollectorAgent("test_collection")

    inserted_count = agent.collect_newsapi(query="Climate change")
    print("Number of articles collected:", inserted_count)

def test_collector_rss():
    agent = CollectorAgent("test_collection")

    feed_url = "http://feeds.bbci.co.uk/news/science_and_environment/rss.xml"

    inserted_count = agent.collect_rss(feed_url)
    print("Number of RSS items collected:", inserted_count)

def test_collector_twitter():
    agent = CollectorAgent("test_collection")

    inserted_count = agent.collect_twitter(query="climate change", max_results=5)
    print("Number of tweets collected:", inserted_count)


test_collector_twitter()