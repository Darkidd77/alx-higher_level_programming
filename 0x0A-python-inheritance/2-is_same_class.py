#!/usr/bin/python3
"""Defines class-checking fun."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.

    Args:
        obj (any): The object.
        a_class (type): The class to match to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) is a_class:
        return True
    return False
