#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return
    max_value = 0
    new_key = None
    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            new_key = key
            return max_Key
