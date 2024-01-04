from .common import db, getNextId
from flask import Blueprint, jsonify

# defines the collection for inventory items
inventoryItemsCol = db["InventoryItems"]

# creates a blueprint to store the routes
inventoryItemsBp = Blueprint("inventoryItems", __name__)


# creates an inventory item
def createItem(name, price, amount):
    itemId = getNextId(inventoryItemsCol)
    item = {"itemId": itemId, "name": name, "price": price, "amount": amount}
    inventoryItemsCol.insert_one(item)
    print(f"Created the following item: {name}")


# deletes an inventory item
def deleteItem(itemId):
    delete = inventoryItemsCol.delete_one({"itemId": itemId})
    if delete.deleted_count > 0:
        print(f"Item with ID:{itemId} was deleted successfully")
    else:
        print(f"Item with ID:{itemId} was not found or was already deleted")


# changes the amount of an item
def changeItemAmount(itemId, amount):
    item = inventoryItemsCol.find_one({"itemId": itemId})
    if item:
        # adds/subtracts to the current amount of an item
        currentAmount = item.get("amount")
        newAmount = currentAmount + amount

        inventoryItemsCol.update_one(
            {"itemId": itemId}, {"$set": {"amount": newAmount}}
        )
        print(f"Item with ID:{itemId} was successfully changed")
    else:
        print(f"Item with ID:{itemId} was not found")
