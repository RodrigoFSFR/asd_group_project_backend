import pymongo

# establishes a connection to the MongoDB server
# uses the default local connection (localhost:27017) for an easier set-up
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["HRMS"]  # database name (Horizon Restaurants Management System)
