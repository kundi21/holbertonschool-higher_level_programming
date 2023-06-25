#!/usr/bin/python3
"""task 1"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    and returns the number of characters written"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
        return len(text)
    
