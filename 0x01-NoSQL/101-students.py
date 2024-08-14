#!/usr/bin/env python3
""" 101. Top students """
from pymongo import MongoClient


def top_students(mongo_collection):
    """Top students"""
    return mongo_collection.aggregate(
        [
            {
                "$project": {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"},
                }
            },
            {"$sort": {"averageScore": -1}},
        ]
    )


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    students = client.my_db.students
    for student in top_students(students):
        print(student)
