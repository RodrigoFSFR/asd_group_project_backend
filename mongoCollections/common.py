# common vars file
import pymongo, os

# MongoDB connection
#        v


# host and port set in the .env file
# sets defaults in case they're not defined in the .env file
host = os.environ.get("dbHost", "localhost")
port = os.environ.get("dbPort", "27017")

# establishes a connection to the MongoDB server
client = pymongo.MongoClient(f"mongodb://{host}:{port}/")
db = client["HRMS"]  # database name (Horizon Restaurants Management System)


# Shared functions
#       v


# generates an ID for an item of any given collection, starting with '1'
def getNextId(collection):
    return collection.count_documents({}) + 1
