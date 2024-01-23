#!/usr/bin/python3
''' Def. class: Square. '''


class Square:
    ''' rep. a square. '''

    def __init__(self, size=0):
        ''' init. new square.

        Args:
            size: new square size.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Return square area.'''
        return self.__size * self.__size
