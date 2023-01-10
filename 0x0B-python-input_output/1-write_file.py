#!/usr/bin/python3
"""Module ``1-write_file``"""


def write_file(filename="", text=""):
    """Writes a string to a text file
    Args:
        filename (str): The name of the file to write to
        text (str): The text to write to the file
    Return:
        Number of characters written
    """
    if not filename or not text:
        return 0

    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
