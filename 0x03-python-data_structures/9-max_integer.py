#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Function that finds an integer.
    Operation is carried out assuming only integers are present in the list.
    The biggest number in the list is the integer to search for.
    Args:
        my_list: List containing integers
    Returns:
        Biggest number in list, or None if list is empty
    """

    if my_list != []:
        newList = sorted(my_list)
        lastIdx = len(newList) - 1
        return newList[lastIdx]
    return None
