from mongo import db

# defines the collection for inventory items
inventoryItemsCol = db["InventoryItems"]


# creates an inventory item
def createItem(itemId, name, price, amount):
    item = {"itemId": itemId, "name": name, "price": price, "amount": amount}
    inventoryItemsCol.insert_one(item)


# deletes an inventory item
def deleteItem(itemId):
    inventoryItemsCol.delete_one({"itemId": itemId})


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
    else:
        return
