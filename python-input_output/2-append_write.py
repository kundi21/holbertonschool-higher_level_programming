#!/usr/bin/python3
"""task 1"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a
    text file (UTF8) and returns the number of characters added"""
    with open(filename, mode="a", encoding="utf-8") as myFile:
        myFile.write(text)
        return len(text)
    