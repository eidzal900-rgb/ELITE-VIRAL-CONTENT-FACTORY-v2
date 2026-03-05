import json
import os
import config


def save_json(filename, data):

    os.makedirs(config.DATA_FOLDER, exist_ok=True)

    path = os.path.join(config.DATA_FOLDER, filename)

    with open(path, "w") as f:

        json.dump(data, f, indent=2)
