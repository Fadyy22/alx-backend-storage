#!/usr/bin/env python3

"""script that provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


client = MongoClient("mongodb://127.0.0.1:27017")
nginx_collection = client.logs.nginx

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

st_ch = nginx_collection.count_documents({"method": "GET", "path": "/status"})

print(f"{nginx_collection.count_documents({})} logs")
print("Methods:")

for method in methods:
    no_method_req = nginx_collection.count_documents({"method": method})
    print(f"\tmethod {method}: {no_method_req}")


print(f"{st_ch} status check")
