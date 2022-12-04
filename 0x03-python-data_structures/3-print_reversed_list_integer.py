#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers of a list assuming list contains only integers.
    Args:
        my_list: List to print from
    """

    if my_list is not None:
        for idx in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[idx]))
