#!/usr/bin/python3
"""task 8"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size):
        """initializator"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area"""
        return self.__size * self.__size

    def __str__(self):
        """[rectangle] width/height"""
        return f"[Square] {self.__size}/{self.__size}"
