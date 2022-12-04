#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all characters c and C from a string.
    Args:
        my_string: String to operate on
    Returns:
        new string
    """

    newString = ""
    for i in my_string:
        if i in "Cc":
            continue
        newString += i
    return newString
