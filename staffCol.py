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
    delete = staffCol.delete_one({"staffId": staffId})
    if delete.deleted_count > 0:
        print(f"Staff member with ID:{staffId} was deleted successfully")
    else:
        print(f"Staff member with ID:{staffId} was not found or was already deleted")


# changes a staff member's role
def changeStaffRole(staffId, role):
    staff = staffCol.find_one({"staffId": staffId})
    if staff:
        staff["role"] = role
        # empties the metrics as the staff member now has a different role
        staff["metrics"] = {}

        # replaces the staff member's data with the new 'staff' data object
        staffCol.replace_one({"staffId": staffId}, staff)
        print(f"Changed staff with ID:{staffId}'s role to: {role}")
    else:
        print(f"Staff member with ID:{staffId} was not found")


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
            print(f"Authenticated staff member with ID:{staffId}")
            return True

    print(f"Failed to authenticate staff member with ID:{staffId}")
    return False


def changePassword(staffId, password):
    # custom secret key used for password hasing, stored in .env
    bcryptKey = os.environ.get("BCRYPTKEY")

    # salts and hashes the password
    salt = bcrypt.gensalt()
    hashedPassword = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.kdf(bcryptKey.encode("utf-8"), salt, desired_key_bytes=32),
    )

    update = staffCol.update_one(
        {"staffId": staffId}, {"$set": {"password": hashedPassword}}
    )
    if update.modified_count > 0:
        print(f"Staff member with ID:{staffId}'s password was changed successfully.")
    else:
        print(f"Staff member with ID:{staffId}'s password could not be changed.")
