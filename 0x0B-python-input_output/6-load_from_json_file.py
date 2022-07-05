#!/usr/bin/python3
""" 6-load_from_json_file: def load_from_json_file """
import json


def load_from_json_file(filename):
    """ creates an Object from a JSON file
        Args:
            filename: file to be read
    """
    with open(filename) as f:
        return json.load(f)
