#!/usr/bin/python3
""" Task 2 module """
from models.base import Base


class Rectangle(Base):
    """Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the Rectangle 

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter width.

        """
        if type(value) is not int:
            raise ValueError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter height
        """
        if type(value) is not int:
            raise ValueError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter "x"
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter "x".
        """
        if type(value) is not int:
            raise ValueError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """
        Getter "y"
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter "y"
        """
        if type(value) is not int:
            raise ValueError("y must be an integer")
        self.__y = value
