#!/usr/bin/python3
"""Module ``4-from_json_string``"""
import json


def from_json_string(my_str):
    """Gets an object represented by a JSON string
    Args:
        my_str (str): JSON string
    Return:
        Object represented by a JSON string
    """
    return json.loads(my_str)
