#!/usr/bin/python3
def square(x):
    return x ** 2


def square_matrix_simple(matrix=[]):
    new_list = []
    for i in matrix:
        new_list.append(list(map(square, i)))
    return new_list
