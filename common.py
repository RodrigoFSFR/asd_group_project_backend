# common vars file

import pymongo

# establishes a connection to the MongoDB server
# uses the default local connection (localhost:27017) for an easier set-up
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["HRMS"]  # database name (Horizon Restaurants Management System)


# generates an ID for an item of any given collection, starting with '1'
def getNextId(collection):
    return collection.count_documents({}) + 1
