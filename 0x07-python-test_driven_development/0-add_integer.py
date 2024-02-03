#!/usr/bin/python3
"""Defines a function for integer addition."""


def add_integer(a, b=98):
    """Returns the result of adding two integers.

    If the arg. are floats, they are typecasted to integers before addition.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
