#!/usr/bin/python3


class SwimMixin:
    """Holds 'swim' method"""
    def swim(self):
        """Outputs 'the creature swims!'"""
        print("The creature swims!")


class FlyMixin:
    """Holds 'fly' method"""
    def fly(self):
        """Outputs 'The creature flies!'"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Inherits from Swim and Fly,
        adds new methods pertaining to Dragon"""
    def roar(self):
        """Outputs 'The dragon roars!'"""
        print("The dragon roars!")

    def spitfire(self):
        """Outputs 'The dragon spits fire!'"""
        print("The dragon spits fire!")
