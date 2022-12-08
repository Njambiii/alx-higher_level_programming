#!/usr/bin/python3
def uniq_add(my_list=[]):
    check_list = []
    sum = 0
    for i in my_list:
        checked = 0
        if not check_list:
            sum += i
            check_list.append(i)
        else:
            for j in check_list:
                if j == i:
                    checked = 1
            if checked != 1:
                sum += i
                check_list.append(i)
    return sum
