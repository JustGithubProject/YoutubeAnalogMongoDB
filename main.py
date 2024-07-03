from pymongo import MongoClient

from config import MONGODB_URI



def connect_to_database():
    # Connect to MongoDB server
    client = MongoClient(MONGODB_URI)

    # Create a new one(db) or connect to an existing one
    db = client["youtube_database"]
    return db





