"""Module for handling the database credentials"""
import json


def _load_creds(filename):
    """Returns the credentials from file as a JSON dictionary"""
    filedirs = __file__.split("/")[:-1] + ["..", "creds"]
    filepath = "/".join(filedirs + [filename])
    with open(filepath, "r") as file:
        json_data = json.load(file)
    return json_data


ROOT_CREDS = _load_creds("root.json")
USER_CREDS = _load_creds("user.json")
