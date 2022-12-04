#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Function to add two tuples assuming only integers in tuples.
    If a tuple is smaller than 2, value of 0 is used for each missing integer
    If a tuple is bigger than 2, first 2 integers are used.
    Args:
        tuple_a: First tuple
        tuple_b: Second tuple
    Returns:
        Tuple with 2 integers with first argument being the addition of the
        first element of each tuple_a and tuple_b, and second element being the
        addition of the second arguments of tuple_a and tuple_b
    """

    new_a = tuple_a + (0, 0)
    new_b = tuple_b + (0, 0)

    firstElement = new_a[0] + new_b[0]
    secElement = new_a[1] + new_b[1]

    return firstElement, secElement
