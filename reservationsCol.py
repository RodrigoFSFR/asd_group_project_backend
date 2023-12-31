from mongo import db

# defines the collection for reservations
reservationsCol = db["Reservations"]


# books a reservation
def createReservation(name, phone, time, table):
    reservation = {"name": name, "phone": phone, "time": time, "table": table}
    reservationsCol.insert_one(reservation)


# deletes a reservation
def deleteReservation(time, table):
    reservationsCol.delete_one({"time": time, "table": table})
