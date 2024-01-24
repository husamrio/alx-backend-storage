#!/usr/bin/env python3
""" Lists all documents in a collection
Return a list of all documents in a collection or an empty list """


def list_all(mongo_collection):
    """ mongo_collection will be the pymongo collection object
    """
    return [each for each in mongo_collection.find()]
