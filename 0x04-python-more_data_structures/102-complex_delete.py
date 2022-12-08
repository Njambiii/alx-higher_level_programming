#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    to_delete = []

    for k, v in a_dictionary.items():
        if v == value:
            to_delete.append(k)
    for i in to_delete:
        del a_dictionary[i]
    return a_dictionary
