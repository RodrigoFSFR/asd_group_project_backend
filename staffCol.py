from mongo import db

# defines the collection for staff members
staffCol = db["Staff"]


# creates a staff member
def createStaff(staffId, password, role, name, metrics):
    staff = {
        "staffId": staffId,
        "password": password,
        "role": role,
        "name": name,
        "metrics": metrics,
    }
    staffCol.insert_one(staff)


# deletes a specific staff member
def deleteStaff(staffId):
    staffCol.delete_one({"id": staffId})


# changes a staff member's role and wipes their metrics
def changeStaffRole(staffId, role):
    staffCol.update_one(
        {"id": staffId}, {"$set": {"type": role}, "$unset": {"metrics": ""}}
    )
