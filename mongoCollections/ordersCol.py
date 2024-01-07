from .common import db, getNextId
from flask import Blueprint, request, jsonify
from .staffCol import staffCol

# defines the collection for orders
ordersCol = db["Orders"]

# creates a blueprint to store the routes
ordersBp = Blueprint("orders", __name__)


@ordersBp.route("/add-order", methods=["POST"])
# creates an order
def createOrder():
    data = request.json
    items = data.get("items")

    orderId = getNextId(ordersCol)
    order = {"orderId": orderId, "items": items}

    insertResult = ordersCol.insert_one(order)
    if insertResult.inserted_id:
        print(f"Created order with ID:{orderId}")
        return "True", 200
    else:
        print(f"Failed to create order")
        return "False", 500


@ordersBp.route("/delete-order", methods=["DELETE"])
# deletes an order
def completeOrder():
    data = request.json
    orderId = data.get("orderId")

    deleteResult = ordersCol.delete_one({"orderId": orderId})
    if deleteResult.deleted_count > 0:
        print(f"Order with ID:{orderId} was deleted successfully")
        return "True", 200
    else:
        print(f"Order with ID:{orderId} was not found or was already deleted")
        return "False", 500


@ordersBp.route("/complete-order", methods=["DELETE"])
# completes (+deletes) an order
def completeOrder():
    data = request.json
    orderId = data.get("orderId")
    staffId = data.get("staffId")

    staff = staffCol.find_one({"staffId": staffId})

    if staff:
        newMetrics = int(staff["metrics"]) + 1

        updateResult = staffCol.update_one(
            {"staffId": staffId}, {"$set": {"metrics": newMetrics}}
        )

        deleteResult = ordersCol.delete_one({"orderId": orderId})
        if (updateResult.modified_count > 0) & (deleteResult.deleted_count > 0):
            print(f"Order with ID:{orderId} was completed successfully")
            return "True", 200
    else:
        print(f"Staff member with ID:{staffId} was not found")
        return "False", 500

    print(f"Order with ID:{orderId} was not found or was already deleted")
    return "False", 500


@ordersBp.route("/change-order")
# changes an order
def changeOrder():
    data = request.json
    orderId = data.get("orderId")
    items = data.get("items")

    updateResut = ordersCol.find_one_and_update(
        {"orderId": orderId}, {"$set": {"items": items}}
    )
    if updateResut.modified_count > 0:
        print(f"Order with ID:{orderId} was changed successfully")
        return "True", 200
    else:
        print(f"Could not change order with ID:{orderId}")
        return "False", 500


@ordersBp.route("/get-all-orders", methods=["GET"])
# fetches the list of orders
def getAllOrders():
    ordersList = list(ordersCol.find({}, {"_id": 0}))
    if ordersList:
        return jsonify(ordersList), 200
    else:
        print("Could not retrieve the list of orders")
        return "False", 500
