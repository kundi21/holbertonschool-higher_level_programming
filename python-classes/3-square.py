#!/usr/bin/python3
"""Squirtle"""


class Square:
    """Squirtle Squirtle"""

    def __init__(self, size=0):
        """Size"""
        self.__size = size

        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Areaaaaaa"""
        self.area = self.__size * self.__size
        return self.area
    pass
