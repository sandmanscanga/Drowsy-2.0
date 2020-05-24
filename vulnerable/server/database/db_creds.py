import json


def _load_creds(filename):
    filedirs = __file__.split("/")[:-1] + ["creds"]
    filepath = "/".join(filedirs + [filename])
    with open(filepath, "r") as f:
        json_data = json.load(f)
    return json_data


ROOT_CREDS = _load_creds("root.json")
USER_CREDS = _load_creds("user.json")
