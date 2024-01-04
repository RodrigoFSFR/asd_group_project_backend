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

    insertResult = menusCol.insert_one(menu)
    if insertResult.inserted_id:
        print(f"Created menu with ID:{menuId}")
        return True, 200
    else:
        print(f"Failed to create menu")
        return False, 500


@menusBp.route("/delete-menu", methods=["DELETE"])
# deletes a menu
def deleteMenu(menuId):
    deleteResult = menusCol.delete_one({"menuId": menuId})
    if deleteResult.deleted_count > 0:
        print(f"Menu with ID:{menuId} was deleted successfully")
        return True, 200
    else:
        print(f"Menu with ID:{menuId} was not found or was already deleted")
        return False, 500


@menusBp.route("/activate-menu", methods=["POST"])
# sets a menu to active
def activateMenu(menuId):
    menu = menusCol.find_one({"menuId": menuId})

    if menu:
        # sets the selected menu to active = "true"
        activationResult = menusCol.update_one(
            {"menuId": menuId}, {"$set": {"active": True}}
        )
        # sets all other menus to active = "false"
        menusCol.update_many({"menuId": {"$ne": menuId}}, {"$set": {"active": False}})

        if activationResult.modified_count > 0:
            print(f"Menu with ID:{menuId} is now the active menu")
            return True, 200
        else:
            print(f"Could not activate menu with ID:{menuId}")
            return False, 500
    else:
        print(f"Menu with ID:{menuId} was not found")
        return False, 500


@menusBp.route("/get-active-menu", methods=["GET"])
# fetches the active menu
def getActiveMenu():
    menu = menusCol.find_one({"active": True})
    if menu:
        return jsonify(menu), 200
    else:
        print("Could not retrieve the active menu")
        return False, 500


@menusBp.route("/get-all-menus", methods=["GET"])
# fetches all menus
def getAllMenus():
    menusList = list(menusCol.find({}, {"_id": 0}))
    if menusList:
        return jsonify(menusList), 200
    else:
        print("Could not retrieve the list of menus")
        return False, 500


@menusBp.route("/get-menu", methods=["GET"])
def getMenu(menuId):
    menu = menusCol.find_one({"menuId": menuId}, {"_id": 0})
    if menu:
        return jsonify(menu), 200
    else:
        print(f"Could not find menu with ID: {menuId}")
        return False, 500
