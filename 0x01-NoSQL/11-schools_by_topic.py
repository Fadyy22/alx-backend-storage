#!/usr/bin/env python3

"""module containing schools_by_topic function"""


def schools_by_topic(mongo_collection, topic):
    """function that returns the list of school having a specific topic"""
    return mongo_collection.find({"topics": {"$elemMatch": topic}})
