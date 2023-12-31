from mongo import db

# defines the collection for inventory items
inventoryItemsCol = db["InventoryItems"]


# creates an inventory item
def createItem(itemId, name, price, amount):
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
