#!/usr/bin/env python3
""" 102. Log stats """
#!/usr/bin/env python3
from pymongo import MongoClient


def log_stats(nginx):
    """
    Provides statistics about the nginx logs stored in the MongoDB collection.
    Additionally, it displays the top 10 most frequent IPs.
    """
    # Get total number of documents
    total_logs = nginx.count_documents({})
    print(f"{total_logs} logs")

    # Count the occurrences of each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count the number of documents with method=GET and path=/status
    status_check = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

    # Get the top 10 most frequent IPs
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10},
    ]
    top_ips = list(nginx.aggregate(pipeline))

    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx = client.logs.nginx

    log_stats(nginx)
