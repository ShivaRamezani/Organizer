import json

def read_json(json_path):
    """to read the json file.

    :param json_path: The path of the json file
    :type json_path: Path
    """
    with open (json_path) as f:
        return json.load(f)
