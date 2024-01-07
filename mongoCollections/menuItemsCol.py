from .common import db, getNextId
from flask import Blueprint, request, jsonify

# defines the collection for inventory items
menuItemsCol = db["menuItems"]

# creates a blueprint to store the routes
menuItemsBp = Blueprint("menuItems", __name__)


@menuItemsBp.route("/add-menu-item", methods=["POST"])
# creates an inventory item
def createItem():
    data = request.json
    name = data.get("name")
    price = data.get("price")
    description = data.get("description")
    itemType = data.get("type")

    itemId = getNextId(menuItemsCol)
    item = {
        "itemId": itemId,
        "name": name,
        "price": price,
        "description": description,
        "itemType": itemType,
        "availability": "True",
    }

    duplicate = menuItemsCol.find_one({"name": name})
    if duplicate:
        print(f"A menu item with the name: {name} already exists")
        return "False", 500

    insertResult = menuItemsCol.insert_one(item)
    if insertResult.inserted_id:
        print(f"Created the following menu item: {name}")
        return "True", 200
    else:
        print(f"Could not create menu item")
        return "False", 500


@menuItemsBp.route("/delete-menu-item", methods=["DELETE"])
# deletes an inventory item
def deleteItem():
    data = request.json
    itemId = data.get("itemId")

    delete = menuItemsCol.delete_one({"itemId": itemId})
    if delete.deleted_count > 0:
        print(f"Menu item with ID:{itemId} was deleted successfully")
        return "True", 200
    else:
        print(f"Menu item with ID:{itemId} was not found or was already deleted")
        return "False", 500


@menuItemsBp.route("/change-menu-item", methods=["POST"])
# changes the amount of an item
def changeItemAmount():
    data = request.json
    itemId = data.get("itemId")
    name = data.get("name")
    price = data.get("price")
    description = data.get("description")
    availability = data.get("availability")

    duplicate = menuItemsCol.find_one({"name": name})
    if duplicate:
        print(f"A menu item with the name: {name} already exists")
        return "False", 500

    item = menuItemsCol.find_one({"itemId": itemId})
    if item:
        updateResult = menuItemsCol.update_one(
            {"itemId": itemId},
            {
                "$set": {
                    "description": description,
                    "name": name,
                    "price": price,
                    "availability": availability,
                }
            },
        )
        if updateResult.modified_count > 0:
            print(f"Menu item with ID:{itemId} was successfully changed")
            return "True", 200
        else:
            print(f"Menu item with ID:{itemId} could not be changed")
            return "False", 500
    else:
        print(f"Menu item with ID:{itemId} was not found")
        return "False", 500


@menuItemsBp.route("/get-all-menu-items", methods=["GET"])
# fetches all items
def getAllItems():
    itemsList = list(menuItemsCol.find({}, {"_id": 0}))
    if itemsList:
        return jsonify(itemsList), 200
    else:
        print("Could not retrieve list of menu items")
        return "False", 500


@menuItemsBp.route("/get-menu-item", methods=["GET"])
# fetches a specific item
def getItem():
    data = request.json
    itemId = data.get("itemId")

    item = menuItemsCol.find_one({"itemId": itemId}, {"_id": 0})
    if item:
        return jsonify(item), 200
    else:
        print(f"Could not find menu item with ID: {itemId}")
        return "False", 500
