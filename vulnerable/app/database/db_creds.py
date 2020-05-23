import json


def load_creds_file(rel_path):
    prefix = ""
    parent_dirs = __file__.split("/")[:-1]
    if len(parent_dirs):
        prefix = "/".join(parent_dirs) + "/"
    print(prefix)
    with open(prefix + "creds/" + rel_path, "r") as f:
        json_data = json.load(f)
    return json_data


ROOT_CREDS = load_creds_file("root.json")
USER_CREDS = load_creds_file("user.json")
