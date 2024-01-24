#!/usr/bin/env python3
""" mongo_collection will be the pymongo collection object """


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of school having a specific topic 
    topic (string) will be topic searched
    """
    return mongo_collection.find({"topics": topic})
