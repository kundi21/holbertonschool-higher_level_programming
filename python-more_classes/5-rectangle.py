#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """Rectangle """

    def __init__(self, width=0, height=0):
        """width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """rectangle representation"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for height in range(self.__height):
            for _ in range(self.__width):
                rectangle += "#"
            if height != self.__height - 1:
                rectangle += '\n'
        return rectangle

    def __repr__(self):
        """repr"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """delete message"""
        print("Bye rectangle...")
