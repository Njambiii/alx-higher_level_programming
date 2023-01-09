#!/usr/bin/python3
"""This is the ``1-my_list`` module

It contains the lone class ``MyList`` which is a subclass of ``list``
"""


class MyList(list):
    """A class that inherits ``list``"""

    def print_sorted(self):
        """Function that prints the list, in sorted order (ascending)"""

        newList = self[:]
        newList.sort()
        print("{}".format(newList))
