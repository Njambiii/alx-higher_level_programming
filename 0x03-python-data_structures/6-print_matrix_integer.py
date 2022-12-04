#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers assuming only integers are present in matrix.
    Args:
        matrix: Matrix containing integers
    """

    if matrix != [[]]:
        for row in matrix:
            for idx in range(len(row)):
                if idx == len(row) - 1:
                    print("{:d}".format(row[idx]))
                    continue
                print("{:d}".format(row[idx]), end=' ')
    else:
        print()
