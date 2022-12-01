#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    hidden = dir(hidden_4)

    for file in hidden:
        if file.startswith("__") is not True:
            print("{}".format(file))
