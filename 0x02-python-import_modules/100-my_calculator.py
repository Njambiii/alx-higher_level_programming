#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    argv = sys.argv
    argc = len(argv)

    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    result = 0

    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "*":
        result = mul(a, b)
    elif op == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {} {:d} = {:d}".format(a, op, b, result))


if __name__ == "__main__":
    main()
