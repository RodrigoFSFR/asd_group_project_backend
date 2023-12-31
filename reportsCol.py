from common import db

# defines the collection for staff reports
reportsCol = db["Reports"]


# creates a staff report
def createReport(staffId, name, role, date, metrics):
    report = {
        "staffId": staffId,
        "name": name,
        "role": role,
        "date": date,
        "metrics": metrics,
    }
    reportsCol.insert_one(report)
    print(f"Generated report for staff member with ID:{staffId}")


def deleteReport(staffId, date):
    delete = reportsCol.delete_one({"staffId": staffId, "date": date})
    if delete.deleted_count > 0:
        print(f"Report with associated staff ID:{staffId} was deleted successfully")
    else:
        print(
            f"Report with associated staff ID:{staffId} was not found or already deleted"
        )
