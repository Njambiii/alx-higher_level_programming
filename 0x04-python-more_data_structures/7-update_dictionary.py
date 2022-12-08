#!/usr/bin/python3
def update_dictionary(my_dict, key, value):
    if key not in my_dict:
        my_dict.update({key: value})
    else:
        del my_dict[key]
        my_dict.update({key: value})
    return my_dict
