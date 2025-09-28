#!/usr/bin/python3

from abc import ABC

"""this module adds a counter to the iter() function

    The counter is added at initialisation.
    It is then incremented whenever the iterable
        goes through '__next__' method.
    It is then returned to the called function in the
        corresponding main file.
"""


class CountedIterator(ABC):
    """Inherits from abstract class"""
    def __init__(self, iterable):
        """instantiates an iterable and a counter"""
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        """returns the iterator"""
        return self

    def __next__(self):
        """Increments the counter.

        Returns:
            item iterated over"""

        item = next(self.iterator)
        self.counter += 1
        return item

    def get_count(self):
        """Fetches counter.

        Returns:
            counter at the time it is called"""
        return self.counter
