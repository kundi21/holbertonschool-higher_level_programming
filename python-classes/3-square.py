#!/usr/bin/python3
"""Squirtle"""


class Square:
    """Squirtle Squirtle"""

    def __init__(self, size=0):
        """Size"""
        self.set_size(size)
        value = size

        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def get_size(self):
        return self.get_size

    def area(self):
        """Areaaaaaa"""
        return self.__size ** 2
    pass
