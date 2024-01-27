#!/usr/bin/env python3

"""script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{nginx_collection.count_documents({})} logs")
    print("Methods:")

    for method in methods:
        req_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {req_count}")

    st = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{st} status check")

    print("IPs:")

    ips = nginx_collection.aggregate(
        [
            {"$group": {"_id": "$ip", "totalRequests": {"$sum": 1}}},
            {"$sort": {"totalRequests": -1}},
            {"$limit": 10},
        ]
    )

    for ip in ips:
        print(f"\t{ip['_id']}: {ip['totalRequests']}")
