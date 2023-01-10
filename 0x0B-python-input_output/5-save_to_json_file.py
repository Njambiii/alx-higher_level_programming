#!/usr/bin/python3
"""Module ``5-save_to_json_file``"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation
    Args:
        my_obj (obj): Python object
        filename (str): Name of the file to write to
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
