#!/usr/bin/python3

for i in range(0, 100):
    end = ", "
    if i == 99:
        end = "\n"

    if i < 10:
        print("0{}".format(i), end=end)
    else:
        print("{}".format(i), end=end)
