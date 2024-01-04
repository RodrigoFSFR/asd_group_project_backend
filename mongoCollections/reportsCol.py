from .common import db
from flask import Blueprint, request, jsonify
from staffCol import staffCol

# defines the collection for staff reports
reportsCol = db["Reports"]

# creates a blueprint to store the routes
reportsBp = Blueprint("reports", __name__)


@reportsBp.route("/add-report", methods=["POST"])
# creates a staff report
def createReport():
    data = request.json
    staffId = data.get("staffId")
    date = data.get("date")
    staff = staffCol.find_one({"staffId": staffId}, {"_id": 0})

    report = {
        "staffId": staffId,
        "name": staff["name"],
        "role": staff["role"],
        "date": date,
        "metrics": staff["metrics"],
    }

    insertResult = reportsCol.insert_one(report)
    if insertResult.inserted_id:
        print(f"Generated report for staff member with ID:{staffId}")
        return "True", 200
    else:
        print(f"Failed to generate report for staff member with ID:{staffId}")
        return "False", 500


@reportsBp.route("/delete-report", methods=["DELETE"])
# deletes a staff report
def deleteReport():
    data = request.json
    staffId = data.get("staffId")
    date = data.get("date")

    deleteResult = reportsCol.delete_one({"staffId": staffId, "date": date})
    if deleteResult.deleted_count > 0:
        print(f"Report with associated staff ID:{staffId} was deleted successfully")
        return "True", 200
    else:
        print(
            f"Report with associated staff ID:{staffId} was not found or already deleted"
        )
        return "False", 500


@reportsBp.route("/get-all-reports", methods=["GET"])
# fetches all reports
def getAllReports():
    reportsList = list(reportsCol.find({}, {"_id": 0}))
    if reportsList:
        return jsonify(reportsList), 200
    else:
        print(f"Could not retrieve staff reports list")
        return "False", 500


@reportsBp.route("/get-staff-reports", methods=["GET"])
# fetches reports for a specifc staff member
def getStaffReports():
    data = request.json
    staffId = data.get("staffId")

    reportsList = list(reportsCol.find({"staffId": staffId}, {"_id": 0}))
    if reportsList:
        return jsonify(reportsList), 200
    else:
        print(f"Could not find reports for staff member with ID: {staffId}")
        return "False", 500
