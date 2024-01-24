#!/usr/bin/python3
""" python script """


class Square():
    """Class representing a square with an attribute private size"""

    def __init__(self, size=0):
        """ Initializing the instances"""
        if isinstance(size, int):
            if size > 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
