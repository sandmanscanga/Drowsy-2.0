"""Module used to load the vuln blueprint"""
# pylint: disable=import-outside-toplevel,import-error
from flask import Flask
from server.database.utils.db_prep import db_prep


def create_server(db_size):
    """Returns an instance of the vulnerable application"""
    db_prep(db_size)
    app = Flask(__name__)
    from server.vuln.routes import vulns
    app.register_blueprint(vulns)
    return app
