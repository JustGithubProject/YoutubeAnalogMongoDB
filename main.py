from pymongo import MongoClient

from config import MONGODB_URI


# Connect to MongoDB server
client = MongoClient(MONGODB_URI)

# Create a new one(db) or connect to an existing one
db = client["youtube_database"]


# Create a new on(collection) or connecto to an existing one
user_collection = db["users"]





