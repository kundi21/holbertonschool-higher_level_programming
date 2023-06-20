#!/usr/bin/python3
"""task 8"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class with inherits from BaseException"""
    def __init__(self, width, height):
        """width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        """returns area"""
        return self.__width * self.__height
    
    def __str__(self):
        """[rectangle] width/height"""
        return f"[Rectangle] {self.__width}/{self.__height}"