"""Configuration file"""

import os

from dotenv import load_dotenv
from pymongo import MongoClient


# Parse a .env file
load_dotenv()


MONGODB_URI = os.environ.get("MONGODB_URI")


def connect_to_database():
    """Connect to MongoDB"""
    client = MongoClient(MONGODB_URI)

    # Create a new one(db) or connect to an existing one
    db = client["youtube_database"]
    return db
