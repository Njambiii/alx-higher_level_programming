#!/usr/bin/python3
def best_score(my_dict):
    if not my_dict:
        return None
    return "{:s}".format([key for key, v in my_dict.items()
                          if v == max(my_dict[x] for x in my_dict)][0])
