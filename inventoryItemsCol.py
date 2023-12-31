from mongo import db

# defines the collection for inventory items
inventoryItemsCol = db["InventoryItems"]


# adds an item to the inventory (InventoryItems collection,
# as there is no 'Inventory/Inventories' collection)
def addItem(itemId, name, price, amount):
    item = {"itemId": itemId, "name": name, "price": price, "amount": amount}
    inventoryItemsCol.insert_one(item)
