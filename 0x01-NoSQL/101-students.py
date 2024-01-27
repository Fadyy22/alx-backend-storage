#!/usr/bin/env python3

"""module containing top_students function"""


def top_students(mongo_collection):
    """function that returns all students sorted by average score"""
    students = mongo_collection.aggregate(
        [
            {
                "$project": {
                    "_id": 1,
                    "name": 1,
                    "averageScore": {"$avg": "$topics.score"},
                    "topics": 1,
                }
            },
            {"$sort": {"averageScore": -1}},
        ]
    )

    return students
