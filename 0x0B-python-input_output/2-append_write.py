#!/usr/bin/python3
"""Module ``2-append_write"""


def append_write(filename="", text=""):
    """Appends a text to the end of a `filename`
    Args:
        filename (str): Name of the file to append text to
        text (str): Text to append in the file
    Return:
        Number of characters added to the file
    """
    if not filename or not text:
        return 0

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
