from .common import db, getNextId
from flask import Blueprint, request, jsonify

# defines the collection for reservations
reservationsCol = db["Reservations"]

# creates a blueprint to store the routes
reservationsBp = Blueprint("reservations", __name__)


@reservationsBp.route("/add-reservation", methods=["POST"])
# books a reservation
def createReservation():
    data = request.json
    name = data.get("name")
    phone = data.get("phone")
    time = data.get("time")
    table = data.get("table")

    reservationId = getNextId(reservationsCol)
    reservation = {
        "reservationId": reservationId,
        "name": name,
        "phone": phone,
        "time": time,
        "table": table,
    }

    insertResult = reservationsCol.insert_one(reservation)
    if insertResult.inserted_id:
        print(f"Created a reservation for table {table} at {time}")
        return "True", 200
    else:
        print(f"Could not create a reservation for table {table} at {time}")
        return "False", 500


@reservationsBp.route("/delete-reservation", methods=["DELETE"])
# deletes a reservation
def deleteReservation():
    data = request.json
    reservationId = data.get("reservationId")

    deleteResult = reservationsCol.delete_one({"reservationId": reservationId})
    if deleteResult.deleted_count > 0:
        print(f"Reservation with ID: {reservationId} was deleted successfully")
        return "True", 200
    else:
        print(f"Reservation with ID: {reservationId} was not found or already deleted")
        return "False", 500


@reservationsBp.route("/change-reservation", methods=["POST"])
# changes a reservation's time and/or table
def changeReservation():
    data = request.json
    reservationId = data.get("reservationId")
    time = data.get("time")
    table = data.get("table")

    updateResult = reservationsCol.find_one_and_update(
        {"reservationId": reservationId}, {"$set": {"time": time, "table": table}}
    )
    if updateResult.modified_count > 0:
        print(
            f"Reservation with ID: {reservationId} changed to table {table} at {time}"
        )
        return "True", 200
    else:
        print(
            f"Failed to change reservation with ID: {reservationId} to table {table} at {time}"
        )
        return "False", 500


@reservationsBp.route("/get-all-reservations", methods=["GET"])
# fetches the list of all reservations
def getAllReservations():
    reservationsList = list(
        reservationsCol.find(
            {},
            {"_id": 0},
        )
    )
    if reservationsList:
        return jsonify(reservationsList), 200
    else:
        return "False", 500


@reservationsBp.route("/get-reservation", methods=["GET"])
# fetches a specific reservation
def getReservation():
    data = request.json
    reservationId = data.get("reservationId")

    reservation = reservationsCol.find_one({"reservationId": reservationId}, {"_id": 0})
    if reservation:
        return jsonify(reservation), 200
    else:
        print(f"Could not find reservation with ID: {reservationId}")
        return "False", 500
