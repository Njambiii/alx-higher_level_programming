#!/usr/bin/python3

def safe_function(fct, *args):
    """Function that executes a function safely"""

    try:
        return fct(*args)
    except Exception as err:
        from sys import stderr
        stderr.write("Exception: {}\n".format(err))
