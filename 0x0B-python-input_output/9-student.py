#!/usr/bin/python3
"""Module ``9-student``"""


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

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return vars(self)
