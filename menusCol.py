from common import db, getNextId

# defines the collection for menus
menusCol = db["Menus"]


# creates a menu
def createMenu(items):
    menuId = getNextId(menusCol)
    # creates the menu with 'active' set to false
    # as the 'active' status depends on the manager's confirmation
    menu = {"menuId": menuId, "active": False, "items": items}
    menusCol.insert_one(menu)


# deletes a menu
def deleteMenu(menuId):
    delete = menusCol.delete_one({"menuId": menuId})
    if delete.deleted_count > 0:
        print(f"Menu with ID:{menuId} was deleted successfully")
    else:
        print(f"Menu with ID:{menuId} was not found or was already deleted")


# sets a menu to active
def activateMenu(menuId):
    menu = menusCol.find_one({"menuId": menuId})

    if menu:
        # sets the selected menu to active = "true"
        menusCol.update_one({"menuId": menuId}, {"$set": {"active": True}})

        # sets all other menus to active = "false"
        menusCol.update_many({"menuId": {"$ne": menuId}}, {"$set": {"active": False}})

        print(f"Menu with ID:{menuId} is now the active menu")
    else:
        print(f"Menu with ID:{menuId} was not found")
