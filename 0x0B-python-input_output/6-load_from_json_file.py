#!/usr/bin/python3
"""a JSON file-reading fun."""
import json


def load_from_json_file(filename):
    """a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
