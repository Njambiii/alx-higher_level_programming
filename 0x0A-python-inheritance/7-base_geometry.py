#!/usr/bin/python3
"""Module ``7-base_geometry``"""


class BaseGeometry:
    """For Geometry"""

    def area(self):
        """Method to raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates `value`

        Args:
            name (str): Name
            value: Value of `nam`

        Raises:
            TypeError if `value` is not an integer
            ValueError if `value` is <= zero
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
