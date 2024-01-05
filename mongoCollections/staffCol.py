from .common import db, getNextId
from flask import Blueprint, request, jsonify
import bcrypt, os  # bcrypt is used for password encryption and verification

# defines the collection for staff members
staffCol = db["Staff"]

# creates a blueprint to store the routes
staffBp = Blueprint("staff", __name__)

# custom secret key used for password hasing, stored in .env
bcryptKey = os.environ.get(
    "bcryptKey", "default"
)  # the key becomes "default" if it is not set in .env


@staffBp.route("/add-staff", methods=["POST"])
# creates a staff member
def createStaff():
    data = request.json
    name = data.get("name")
    password = str(data.get("password"))
    role = data.get("role")
    shift = data.get("shift")

    # salts and hashes the password
    salt = bcrypt.gensalt()
    hashedPassword = bcrypt.hashpw(password.encode("utf-8"), salt)

    staffId = getNextId(staffCol)
    staff = {
        "staffId": staffId,
        "password": hashedPassword,
        "role": role,
        "name": name,
        "shift": shift,
        "metrics": 0,
    }

    insertResult = staffCol.insert_one(staff)
    if insertResult.inserted_id:
        print(f"Staff member created with ID:{staffId}")
        return "True", 200
    else:
        print(f"Staff member could not be created")
        return "False", 500


@staffBp.route("/delete-staff", methods=["DELETE"])
# deletes a specific staff member
def deleteStaff():
    data = request.json
    staffId = data.get("staffId")

    deleteResult = staffCol.delete_one({"staffId": staffId})
    if deleteResult.deleted_count > 0:
        print(f"Staff member with ID:{staffId} was deleted successfully")
        return "True", 200
    else:
        print(f"Staff member with ID:{staffId} was not found or was already deleted")
        return "False", 500


@staffBp.route("/change-role", methods=["POST"])
# changes a staff member's role
def changeStaffRole():
    data = request.json
    staffId = data.get("staffId")
    role = data.get("role")

    staff = staffCol.find_one({"staffId": staffId})
    if staff:
        staff["role"] = role
        # empties the metrics as the staff member now has a different role
        staff["metrics"] = {}

        # replaces the staff member's data with the new 'staff' data object
        replaceResult = staffCol.replace_one({"staffId": staffId}, staff)
        if replaceResult.modified_count > 0:
            print(f"Changed staff with ID:{staffId}'s role to: {role}")
            return "True", 200
        else:
            print(f"Could not change staff with ID:{staffId}'s role to: {role}")
            return "False", 500
    else:
        print(f"Staff member with ID:{staffId} was not found")
        return "False", 500


@staffBp.route("/login", methods=["POST"])
# login function using staff details
def login():
    data = request.json
    staffId = data.get("staffId")
    password = data.get("password")

    staff = staffCol.find_one({"staffId": staffId})
    if staff:
        storedPassword = staff["password"]

        # hashes the input password with the same method as the one stored in the database
        hashedPassword = bcrypt.hashpw(password.encode("utf-8"), storedPassword)

        # compares the passwords using the built-in bcrypt.checkpw method
        if bcrypt.checkpw(hashedPassword, storedPassword):
            print(f"Authenticated staff member with ID:{staffId}")
            return "True", 200

    print(f"Failed to authenticate staff member with ID:{staffId}")
    return "False", 500


@staffBp.route("/change-password", methods=["POST"])
# changes a staff member's password
# only works if a manager's ID is inserted
# alongside the staff member or manager's own ID
def changePassword():
    data = request.json
    managerId = data.get("managerId")
    staffId = data.get("staffId")
    password = data.get("password")

    staff = staffCol.find_one({"staffId": managerId})
    if staff["type"] != "Manager":
        print(
            f"Incorrect manager ID: {managerId}, staff member with ID:{staffId}'s password could not be changed"
        )
        return "False", 500

    # salts and hashes the password
    salt = bcrypt.gensalt()
    hashedPassword = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.kdf(bcryptKey.encode("utf-8"), salt, desired_key_bytes=32, rounds=10),
    )

    updateResult = staffCol.update_one(
        {"staffId": staffId}, {"$set": {"password": hashedPassword}}
    )
    if updateResult.modified_count > 0:
        print(f"Staff member with ID:{staffId}'s password was changed successfully")
        return "True", 200
    else:
        print(f"Staff member with ID:{staffId}'s password could not be changed")
        return "False", 500


@staffBp.route("/get-all-staff", methods=["GET"])
# fetches all staff members' names, IDs and roles
def getAllStaff():
    staffList = list(
        staffCol.find(
            {},
            {
                "_id": 0,
                "password": 0,
                "metrics": 0,
            },
        )
    )
    if staffList:
        return jsonify(staffList), 200
    else:
        print("Could not retreive staff list")
        return "False", 500


@staffBp.route("/get-staff", methods=["GET"])
# fetches a specific staff member's information
def getStaff():
    data = request.json
    staffId = data.get("staffId")

    staff = staffCol.find_one({"staffId": staffId}, {"_id": 0})
    if staff:
        return jsonify(staff), 200
    else:
        print(f"Unable to find staff member with ID:{staffId}")
        return "False", 500
