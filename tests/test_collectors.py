from src.database.mongodb_client import get_collection
from src.agents.collector_agent import CollectorAgent

def test_get_collection():
    col = get_collection("test_collection")
    result = col.insert_one({"message": "Hola Mundo desde MongoDB"})
    print("Inserted document ID:", result.inserted_id)

def test_collector_static():
    agent = CollectorAgent("test_collection")

    url = "https://climate.nasa.gov/news/"

    id = agent.collect_static(url, source="nasa_climate_news")
    print("Collected document ID:", id)

def test_collector_dynamic():
    agent = CollectorAgent("test_collection")

    url = "https://www.nytimes.com/section/climate"

    id = agent.collect_dynamic(url)
    print("Collected document ID:", id)


test_collector_dynamic()