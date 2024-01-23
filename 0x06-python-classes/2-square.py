#!/usr/bin/python3
''' Def. class: Square '''


class Square:
    ''' Def. a square. '''

    def __init__(self, size=0):
        ''' init. new square.

       Args:
           size: new square size.
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
