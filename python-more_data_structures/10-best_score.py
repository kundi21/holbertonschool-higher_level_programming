#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return
    max_value = max(a_dictionary.values())
    for i, j in a_dictionary.items():
        if max_value == j:
            return i
