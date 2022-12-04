#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Function to print a list of integers assuming only integers in list.
    Args:
        my_list: List of integers
    """

    for integer in my_list:
        print("{:d}".format(integer))
