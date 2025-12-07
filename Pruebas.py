from src.agents.collector_agent import CollectorAgent
from src.collectors.newsapi_client import fetch_top_headlines


agent = CollectorAgent("test_collection")
urls = fetch_top_headlines()


inserted_count = 0
for url in urls:
    id = agent.collect_dynamic(url, source="newsapi")
    if id is not None:
        inserted_count += 1
print(f"Total documents inserted: {inserted_count}")