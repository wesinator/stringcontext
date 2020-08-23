#!/usr/bin/env python3

def context(string, index, contextnum):
    """returns the full string of the context before, after,
    and including the character at index.
    """
    try:
        return context_before(string, index, contextnum) \
        + string[index] \
        + context_after(string, index, contextnum)
    except IndexError:
        return ''


def context_before(string, index, contextnum):
    """gets the specified number of characters before the given index,
    or until the beginning of the string.
    """
    if contextnum < 0:
        raise ValueError("Context amount cannot be negative")

    bound = index - contextnum
    # start at beginning of string if contextnum is greater than length before
    if bound < 0:
        bound = 0

    return string[bound:index]


def context_after(string, index, contextnum):
    """gets the specified number of characters after the given index,
    or until the end of the string.
    """
    if contextnum < 0:
        raise ValueError("Context amount cannot be negative")

    bound = index + contextnum
    return string[index + 1:bound + 1]
