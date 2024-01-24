#!/usr/bin/env python3
""" Module for using PyMongo
Returns the new _id
"""


def insert_school(mongo_collection, **kwargs):
    """ From pymongo import MongoClient
      Inserts new doc in collection based on kwargs """
    return mongo_collection.insert_one(kwargs).inserted_id
