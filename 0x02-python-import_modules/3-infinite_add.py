#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    sum = 0
    for i in range(1, len(args)):
        sum += int(args[i])
    print("{:d}".format(sum))
