#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Function to replace an element in a list at a specified index.
    Args:
        my_list: List to place element
        idx: Index at which to place element
        element: New element to place at index
    Returns:
        Modified list, or original list if index is out of range
    """

    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
        return my_list
    return my_list
