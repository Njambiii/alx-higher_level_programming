#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    argc = len(args)
    msg = ""
    if argc == 1:
        msg = "arguments."
    elif argc == 2:
        msg = "argument:"
    else:
        msg = "arguments:"

    print("{:d} {}".format(argc - 1, msg))
    for i in range(1, argc):
        print("{:d}: {}".format(i, args[i]))
