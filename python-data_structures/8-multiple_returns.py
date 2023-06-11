#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_char = None
    if sentence is None or sentence == "":
        return (length, first_char)
    else:
        first_char = sentence[0]
        return (length, first_char)
