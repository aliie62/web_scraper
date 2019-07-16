from pymongo import MongoClient
import ssl
import datetime
import re

def __connect():
    username = 'USER MONGODB USERNAME'
    password = 'YOUR MONGODB PASSWORD'
    #instead of 127.0.0.1 in below, enter your MongoDB URI
    client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username,password),ssl_cert_reqs=ssl.CERT_NONE)
    return client

def bulk_insert(documents):
    client = __connect()
    db = client['YOUR DB NAME']
    collection = db['YOUR COLLECTION NAME']  
    result = collection.insert_many(documents)
    return result.inserted_ids