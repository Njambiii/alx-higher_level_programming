#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Function to get length of a string and first character.
    Args:
        sentence: String to get character and length from
    Returns:
        Length of sentence and first character as tuple
    """

    strLen = len(sentence)
    if strLen > 0:
        return strLen, sentence[0]
    return strLen, None
