#!/usr/bin/env python3
""" 102. Log stats """
from pymongo import MongoClient


def log_stats(mongo_collection):
    """Log stats"""
    return mongo_collection.aggregate([
        {"$sortByCount": "$ip"},
        {"$limit": 10}
    ])

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx = client.logs.nginx
    for ip in log_stats(nginx):
        print("[{}] {}".format(ip.get("_id"), ip.get("count")))
