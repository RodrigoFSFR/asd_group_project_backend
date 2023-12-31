from mongo import db

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
