import os

# flask is used because it simplifies and
# optimizes the http server and routing
from flask import Flask

# imports all collections in the collections folder
# so that their routes can be used by the server
from mongoCollections import (
    inventoryItemsCol,
    menusCol,
    reportsCol,
    reservationsCol,
    staffCol,
)

server = Flask(__name__)

# registers all blueprints from the collections
# the blueprints contain the http request routes
server.register_blueprint(inventoryItemsCol.inventoryItemsBp)
server.register_blueprint(menusCol.menusBp)
server.register_blueprint(reportsCol.reportsBp)
server.register_blueprint(reservationsCol.reservationsBp)
server.register_blueprint(staffCol.staffBp)

# host and post set in the .env file
# sets defaults in case they're not defined in the .env file
host = os.getenv("httpHost", "localhost")
port = int(os.getenv("httpPort", 8080))

# starts the flask http server
if __name__ == "__main__":
    server.run(debug=True, host=host, port=port)
