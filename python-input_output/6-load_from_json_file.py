#!/usr/bin/python3
import json
"""task 6"""


def load_from_json_file(filename):
    """unction that creates an Object from a “JSON file”"""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
