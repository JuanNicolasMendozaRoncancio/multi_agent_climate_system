from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGODB_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "climate_system")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

def get_collection(collection_name):
    return db[collection_name]