#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Function to delete an element at an index in a list.
    Args:
        my_list: List to find element
        idx: Index in list at which item to be deleted can be found
    """

    if my_list != []:
        if idx >= 0 and idx < len(my_list):
            del my_list[idx]
    return my_list
