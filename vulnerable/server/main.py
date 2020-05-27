"""Module used to load the vuln blueprint"""
# pylint: disable=import-outside-toplevel,import-error
from flask import Flask
from server.database.utils.db_prep import db_prep


def create_server(db_size):
    """Returns an instance of the vulnerable application

    Creates an instance of the vuln blueprint with the specified
    number of users and returns the application object.

    Args:
        db_size (int): the number of users to load into the database

    Returns:
        obj: returns the application in an object

    """
    db_prep(db_size)
    app = Flask(__name__)
    from server.vuln.routes import vulns
    app.register_blueprint(vulns)
    return app
