#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_char = None
    if not sentence:
        print("Length: {} - First character: {}".format(length, first_char))
    else:
        first_char = sentence[0]
        print("Length: {} - First character: {}".format(length, first_char))
