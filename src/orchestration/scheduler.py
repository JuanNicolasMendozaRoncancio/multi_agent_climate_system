from src.orchestration.raw_pipeline import run_raw_pipeline, add_pure_dynamic, add_pure_static
from src.collectors.First_injection import first_collector_newsapi, first_collector_rss
from apscheduler.schedulers.blocking import BlockingScheduler
import random

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', hours=6)
def scheduled_collection():

    valid_rss_fedds = [
        "http://feeds.bbci.co.uk/news/science_and_environment/rss.xml",
        "https://www.theguardian.com/environment/rss",
        "https://news.mongabay.com/feed/"
    ]

    feed = random.choice(valid_rss_fedds)

    first_collector_rss(feed_url=feed)

    first_collector_newsapi()

@scheduler.scheduled_job('interval', hours=12)
def scheduled_raw_pipeline():
    run_raw_pipeline()


if __name__ == "__main__":
    print("🚀 Scheduler running...")
    scheduler.start()

