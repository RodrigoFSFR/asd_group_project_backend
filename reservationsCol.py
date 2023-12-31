from mongo import db

# defines the collection for reservations
reservationsCol = db["Reservations"]


# books a reservation
def createReservation(name, phone, time, table):
    reservation = {"name": name, "phone": phone, "time": time, "table": table}
    reservationsCol.insert_one(reservation)
    print(f"Created a reservation for table {table} at {time}")


# deletes a reservation
def deleteReservation(time, table):
    delete = reservationsCol.delete_one({"time": time, "table": table})
    if delete.deleted_count > 0:
        print(f"Reservation for table {table} at {time} was deleted successfully")
    else:
        print(
            f"Reservation for table {table} at {time} was not found or already deleted"
        )
