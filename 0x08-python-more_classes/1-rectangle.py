#!/usr/bin/python3
"""Defines  Rect. class."""


class Rectangle:
    """Represent  rect."""

    def __init__(self, w=0, h=0):
        """Initialize new Rect.

        Args:
            w (int): The width of the new rectangle.
            h (int): The height of the new rectangle.
        """
        self.w = w
        self.h = h

    @property
    def w(self):
        """Get/set the width of the rectangle."""
        return self.__w

    @w.setter
    def w(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__w = value

    @property
    def h(self):
        """Get/set the height of the rectangle."""
        return self.__h

    @h.setter
    def h(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__h = value
