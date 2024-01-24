#!/usr/bin/env python3
""" from pymongo import MongoClient """
import pymongo


def update_topics(mongo_collection, name, topics):
    """topics (list of strings) will be the list of 
    topics approached in the school"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
