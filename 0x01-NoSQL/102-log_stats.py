#!/usr/bin/env python3
""" 102. Log stats """
from pymongo import MongoClient


def log_stats(mongo_collection):
    """log stats"""
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print(f"{mongo_collection.estimated_document_count()} logs")
    print("Methods:")
    for m in method:
        print(
            f"\tmethod {m}: {mongo_collection.count_documents({'method': m})}"
        )
    print(
        f"{mongo_collection.count_documents(
            { 'method': 'GET', 'path': '/status' }
            )} status check"
    )


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_stats(client.logs.nginx)
    