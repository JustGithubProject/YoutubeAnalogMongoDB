from pymongo import MongoClient


uri = "mongodb://localhost:27017/"

# Connect to MongoDB server
client = MongoClient(uri)

# Create a new one(db) or connect to an existing one
db = client["youtube_database"]


# Create a new on(collection) or connecto to an existing one
user_collection = db["users"]





