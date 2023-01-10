#!/usr/bin/python3
"""Module ``3-to_json_string``"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)
    Args:
        my_obj (obj): The Python object to return representation of
    Return:
        JSON representation
    """
    return json.dumps(my_obj)
