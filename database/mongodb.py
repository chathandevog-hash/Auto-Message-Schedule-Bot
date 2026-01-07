from pymongo import MongoClient
from config.config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["auto_message_bot"]
collection = db["schedules"]

def add_message(data):
    return collection.insert_one(data).inserted_id

def get_all(chat_id=None):
    if chat_id is None:
        return list(collection.find({}))
    return list(collection.find({"chat_id": chat_id}))

def get_all_running():
    return list(collection.find({"status": "running"}))

def stop_message(msg_id):
    collection.update_one({"_id": msg_id}, {"$set": {"status": "stopped"}})
