from .common import db
from flask import Blueprint, jsonify

# defines the collection for staff reports
reportsCol = db["Reports"]

# creates a blueprint to store the routes
reportsBp = Blueprint("reports", __name__)


@reportsBp.route("/add-report", methods=["POST"])
# creates a staff report
def createReport(staffId, name, role, date, metrics):
    report = {
        "staffId": staffId,
        "name": name,
        "role": role,
        "date": date,
        "metrics": metrics,
    }

    insertResult = reportsCol.insert_one(report)
    if insertResult.inserted_id:
        print(f"Generated report for staff member with ID:{staffId}")
        return True
    else:
        print(f"Failed to generate report for staff member with ID:{staffId}")
        return False


@reportsBp.route("/delete-report", methods=["DELETE"])
# deletes a staff report
def deleteReport(staffId, date):
    deleteResult = reportsCol.delete_one({"staffId": staffId, "date": date})
    if deleteResult.deleted_count > 0:
        print(f"Report with associated staff ID:{staffId} was deleted successfully")
        return True
    else:
        print(
            f"Report with associated staff ID:{staffId} was not found or already deleted"
        )
        return False
