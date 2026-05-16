import json
import os


def get_config():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "..", "config", "config.json")
    with open(file_path, "r") as file:
        return json.load(file)
