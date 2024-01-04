from .common import db, getNextId
from flask import Blueprint, jsonify

# defines the collection for menus
menusCol = db["Menus"]

# creates a blueprint to store the routes
menusBp = Blueprint("menus", __name__)


@menusBp.route("/add-menu", methods=["POST"])
# creates a menu
def createMenu(items):
    menuId = getNextId(menusCol)
    # creates the menu with 'active' set to false
    # as the 'active' status depends on the manager's confirmation
    menu = {"menuId": menuId, "active": False, "items": items}
    menusCol.insert_one(menu)
    print(f"Created menu with ID:{menuId}")
    return True


@menusBp.route("/delete-menu", methods=["DELETE"])
# deletes a menu
def deleteMenu(menuId):
    delete = menusCol.delete_one({"menuId": menuId})
    if delete.deleted_count > 0:
        print(f"Menu with ID:{menuId} was deleted successfully")
        return True
    else:
        print(f"Menu with ID:{menuId} was not found or was already deleted")
        return False


@menusBp.route("/activate-menu", methods=["POST"])
# sets a menu to active
def activateMenu(menuId):
    menu = menusCol.find_one({"menuId": menuId})

    if menu:
        # sets the selected menu to active = "true"
        menusCol.update_one({"menuId": menuId}, {"$set": {"active": True}})

        # sets all other menus to active = "false"
        menusCol.update_many({"menuId": {"$ne": menuId}}, {"$set": {"active": False}})

        print(f"Menu with ID:{menuId} is now the active menu")
        return True
    else:
        print(f"Menu with ID:{menuId} was not found")
        return False