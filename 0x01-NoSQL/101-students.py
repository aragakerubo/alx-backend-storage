#!/usr/bin/env python3
""" 101. Top students """
from pymongo import MongoClient


def top_students(mongo_collection):
    """top students"""
    return mongo_collection.aggregate(
        [
            {"$unwind": "$topics"},
            {
                "$group": {
                    "_id": "$_id",
                    "averageScore": {"$avg": "$topics.score"},
                }
            },
            {"$sort": {"averageScore": -1}},
        ]
    )


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    top_students(client.my_db.students)
