#!/usr/bin/python3


def weight_average(my_list=[]):
    avg = 0
    if len(my_list) > 0:
        prod = 0
        sum = 0
        for x, y in my_list:
            prod += x * y
            sum += y
        avg = prod / sum
    return avg
