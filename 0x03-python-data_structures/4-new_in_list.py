#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific index without modifying it.
    Args:
        my_list: List to perform operation on
        idx: Index at which to place new element
        element: Element to place in list
    Returns:
        Copy containing modification, or an unmodified copy if idx out of range
    """

    newList = my_list[:]
    if idx >= 0 and idx < len(my_list):
        newList[idx] = element
    return newList
