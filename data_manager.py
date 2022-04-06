from sqlite3 import DatabaseError
from pymongo import MongoClient
import os

username = os.environ.get('MONGO_USERNAME')
password = os.environ.get('MONGO_PASSWORD')
mongo_uri = os.environ.get('MONGO_URI')
mongo_db = os.environ.get('MONGO_DB')
mongo_collection = os.environ.get('MONGO_COLLECTION')


def bulk_insert(documents):
    try:
        client = MongoClient(f"mongodb+srv://{username}:{password}@{mongo_uri}?retryWrites=true&w=majority")
    except:
        raise ConnectionError('Error in connecting to MongoDB server.')
    
    try:
        db = client[mongo_db]
        collection = db[mongo_collection]  
        collection.insert_many(documents)
    except:
        raise DatabaseError('Error in saving data in database.')