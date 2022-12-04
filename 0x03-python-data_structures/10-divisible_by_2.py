#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Function to find multiples of 2 in a list of integers.
    It is assumed list will only contain integers.
    Args:
        my_list: List containing integers
    Returns:
        New list containing True if index in my_list is divisible by 2 or
        false if not.
    """

    if my_list != []:
        newList = []
        for integer in my_list:
            if integer % 2 == 0:
                newList.append(True)
            else:
                newList.append(False)
        return newList
