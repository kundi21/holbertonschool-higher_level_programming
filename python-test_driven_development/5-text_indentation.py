#!/usr/bin/python3
"""
task 5
"""


def text_indentation(text):
    if text is None or type(text) is not str:
        raise TypeError("text must be a string")

    newline = False

    for char in text:
        if newline:
            if char == ' ':
                continue
            newline = False
        print(char, end="")
        if char in ['.', '?', ':']:
            print()
            print()
            newline = True
