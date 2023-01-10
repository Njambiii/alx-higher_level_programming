#!/usr/bin/python3
"""Module ``6-load_from_json_file``"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file
    Args:
        filename (str): The name of the JSON file
    Return:
        The PyObject
    """
    with open(filename, 'r') as json_f:
        return json.load(json_f)
