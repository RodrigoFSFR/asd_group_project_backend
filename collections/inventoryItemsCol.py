from .common import db, getNextId
from flask import Blueprint, jsonify

# defines the collection for inventory items
inventoryItemsCol = db["InventoryItems"]

# creates a blueprint to store the routes
inventoryItemsBp = Blueprint("inventoryItems", __name__)


@inventoryItemsBp.route("/add-item", methods=["POST"])
# creates an inventory item
def createItem(name, price, amount):
    itemId = getNextId(inventoryItemsCol)
    item = {"itemId": itemId, "name": name, "price": price, "amount": amount}

    insertResult = inventoryItemsCol.insert_one(item)
    if insertResult.inserted_id:
        print(f"Created the following item: {name}")
        return True
    else:
        print(f"Could not create item")
        return False


@inventoryItemsBp.route("/delete-item", methods=["DELETE"])
# deletes an inventory item
def deleteItem(itemId):
    delete = inventoryItemsCol.delete_one({"itemId": itemId})
    if delete.deleted_count > 0:
        print(f"Item with ID:{itemId} was deleted successfully")
        return True
    else:
        print(f"Item with ID:{itemId} was not found or was already deleted")
        return False


@inventoryItemsBp.route("/change-item", methods=["POST"])
# changes the amount of an item
def changeItemAmount(itemId, amount):
    item = inventoryItemsCol.find_one({"itemId": itemId})
    if item:
        # adds/subtracts to the current amount of an item
        currentAmount = item.get("amount")
        newAmount = currentAmount + amount

        updateResult = inventoryItemsCol.update_one(
            {"itemId": itemId}, {"$set": {"amount": newAmount}}
        )
        if updateResult.modified_count > 0:
            print(
                f"Item with ID:{itemId}'s amount was successfully changed to {newAmount}"
            )
            return True
        else:
            print(f"Item with ID:{itemId} could not be changed to {newAmount}")
            return True
    else:
        print(f"Item with ID:{itemId} was not found")
        return False
