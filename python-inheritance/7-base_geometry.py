#!/usr/bin/python3
"""task 4"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """area is not implemented exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """validates if name is an integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
    