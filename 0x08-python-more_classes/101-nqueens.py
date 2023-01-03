#!/usr/bin/python3

"""
N Queens puzzle module
"""

import sys

def main(argv):
    if len(argv) is not 1:
        print("Usage: nqueens N")
        sys.exit(1)
    N = int(argv[0])
    if type(N) is not int:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    print(int(argv[0]))

if __name__ == "__main__":
    main(sys.argv[1:])
