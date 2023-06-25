#!/usr/bin/python3
"""Squirtle"""


class Square:
    """Squirtle Squirtle"""

    def __init__(self, size=0):
        "Size"
        self.__size = size

    @property
    def size(self):
        "Getter"
        return self.__size

    @size.setter
    def size(self, value):
        "Setter"
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Areaaaaaa"""
        self.area = self.__size * self.__size
        return self.area

    def my_print(self):
        "My_print"
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
