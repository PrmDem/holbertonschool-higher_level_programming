#!/usr/bin/python

class Fish:
    """Gives the habitat and movement type of a fish"""

    def swim(self):
        """prints a sentence"""
        print("The fish is swimming")

    def habitat(self):
        """prints a sentence"""
        print("The fish lives in water")


class Bird:
    """Gives the habitat and movement type of a bird"""

    def fly(self):
        """prints a sentence"""
        print("The bird is flying")

    def habitat(self):
        """prints a sentence"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):

    def fly(self):
        """overrides fly method from bird"""
        print("The flying fish is soaring!")

    def swim(self):
        """overrides swim method from fish"""
        print("The flying fish is swimming!")

    def habitat(self):
        """overrides both parent classes' method
            and prints habitat of flying fish"""
        print("The flying fish lives both in water and the sky!")
