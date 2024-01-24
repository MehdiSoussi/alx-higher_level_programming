#!/usr/bin/python3
""" python script """


class Square():
    """Class representing a square with an attribute private size"""

    def __init__(self, size=0):
        """ Initializing the instances"""

        self.__size = size

    @property
    def size(self):
        """ size proprety"""

        return self.__size

    @size.setter
    def size(self, value):
        """ size setter"""

        if isinstance(size, int):
            if size > 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ area method"""

        return self.__size * self.__size
