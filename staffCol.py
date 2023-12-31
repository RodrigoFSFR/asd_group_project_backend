from mongo import db
import bcrypt, os

# defines the collection for staff members
staffCol = db["Staff"]


# creates a staff member
def createStaff(staffId, password, role, name, metrics):
    # custom secret key used for password hasing, stored in .env
    bcryptKey = os.environ.get("BCRYPTKEY")

    # salts and hashes the password
    salt = bcrypt.gensalt()
    hashedPassword = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.kdf(bcryptKey.encode("utf-8"), salt, desired_key_bytes=32),
    )

    staff = {
        "staffId": staffId,
        "password": hashedPassword,
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


# login function using staff details
def login(staffId, password):
    staff = staffCol.find_one({"staffId": staffId})
    if staff:
        storedPassword = staff["password"]
        bcryptKey = os.environ.get("BCRYPTKEY")

        # hashes the input password with the same method as the one stored in the database
        hashedPassword = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.kdf(bcryptKey.encode("utf-8"), storedPassword),
        )

        # compares the passwords using the built-in bcrypt.checkpw method
        if bcrypt.checkpw(hashedPassword, storedPassword):
            return True

    return False
