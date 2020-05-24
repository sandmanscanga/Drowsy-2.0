from flask import Flask
from server.database.db_prep import db_prep


def create_server(db_size):
    db_prep(db_size)
    app = Flask(__name__)
    from server.vuln.routes import vulns
    app.register_blueprint(vulns)
    return app
