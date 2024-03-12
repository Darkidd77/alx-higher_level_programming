#!/usr/bin/python3
'''Module for Base class'''

class Base:
    '''the base of our OOP hierarchy'''

    __nb_objects = 0

    def __init__(self, id=None):
        """Init. a new Base.

        Args:
            id (int): id of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
