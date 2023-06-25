#!/usr/bin/python3
""" task 6"""


import json


def load_from_json_file(filename):
    """Load"""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
