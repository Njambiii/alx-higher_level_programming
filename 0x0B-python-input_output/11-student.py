#!/usr/bin/python3
"""Module ``11-student``"""


class Student:
    """A class for Students"""

    def __init__(self, first_name, last_name, age):
        """Inilializes the first, last names, and the age of the student
        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of th student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""

        a_dict = vars(self)
        if type(attrs) == list and all(isinstance(i, str) for i in attrs):
            new_dict = {}
            for key in filter(lambda key: key in a_dict, attrs):
                new_dict[key] = a_dict[key]
            return new_dict

        return a_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance present in `json`
        Args:
            json (dict): A dictionary
        """
        for k, v in json.items():
            if k in vars(self):
                setattr(self, k, v)
