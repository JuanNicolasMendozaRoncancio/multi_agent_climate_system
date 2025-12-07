from src.agents.collector_agent import CollectorAgent


def first_collector_newsapi():
    agent = CollectorAgent("First_injection_collection")
    agent.collect_newsapi()

def first_collector_rss(feed_url: str):
    agent = CollectorAgent("First_injection_collection")

    agent.collect_rss(feed_url)
