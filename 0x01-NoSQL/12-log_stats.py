#!/usr/bin/env python3
""" 12. Log stats """
from pymongo import MongoClient


def log_stats(mongo_collection):
    """Log stats"""
    print(f"{mongo_collection.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    count = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{count} status check")


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    log_stats(client.logs.nginx)
