from pymongo import MongoClient

DB_NAME = "learning1"
MONGO_URI = f"mongodb://localhost:27017/{DB_NAME}"

conn = MongoClient(MONGO_URI)