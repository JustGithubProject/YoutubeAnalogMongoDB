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



def create_database_and_collections():
    client = MongoClient(MONGODB_URI)  # Подключаемся к MongoDB
    db = client["youtube_database"]  # Создаем базу данных

    # Создаем коллекции users и videos
    users_collection = db["users"]
    videos_collection = db["videos"]

    print("Database and collections created successfully!")
    
    
"""
use admin
db.createUser({
  user: "yourusername",
  pwd: "yourpassword",
  roles: [{ role: "readWrite", db: "yourdatabase" }]
})
"""