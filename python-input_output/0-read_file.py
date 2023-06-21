#!/usr/bin/python3
"""task 0"""


def read_file(filename=""):
    """read file and then print"""
    with open(filename, encoding="utf-8") as myFile:
        file = myFile.read()
        print(file)

