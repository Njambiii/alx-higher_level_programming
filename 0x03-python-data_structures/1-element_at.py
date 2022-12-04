#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Function to retrieve an element in a list.
    Args:
        my_list: List with element
        idx: Index in list where element can be found
    Returns:
        Element at idx, or None if idx out of range
    """

    if idx >= 0 and idx < len(my_list):
        return my_list[idx]
