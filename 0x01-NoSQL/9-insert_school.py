#!/usr/bin/env python3

"""module containing insert_school function"""


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a collection based on kwargs"""
    return mongo_collection.insert_one(kwargs)
