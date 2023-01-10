#!/usr/bin/python3
"""Module ``8-class_to_json``"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure for JSON
    serialization of an object
    """
    return vars(obj)
