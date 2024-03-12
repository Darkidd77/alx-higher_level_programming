#!/usr/bin/python3
"""Defines a function for integer addition."""


def add_integer(a, b=98):
    """Returns the result of adding two integers.

    If the arg. are floats, they are typecasted to integers before addition.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
