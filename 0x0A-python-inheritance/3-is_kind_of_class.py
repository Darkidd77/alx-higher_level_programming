#!/usr/bin/python3
"""Defines class and inherited class-checking fun."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an inst or inherited inst of a class.

    Args:
        obj (any): The object.
        a_class (type): The class to match to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
