#!/usr/bin/python3
from abc import ABC, abstractmethod

"""This module instantiates animals,
        such as dogs and cats, from abstract
        subclasses of the same name.

    Methods so far include:
        sound - the sound the animal makes
    """


class Animal(ABC):
    """Abstract superclass for all animals"""

    @abstractmethod
    def sound(self):
        """is not implemented here,
        due to being abstract"""
        ...


class Dog(Animal):
    """subclass for dogs"""
    def sound(self):
        """makes our dog bark"""
        return "Bark"


class Cat(Animal):
    """subclass for cats"""
    def sound(self):
        """makes our cat meow"""
        return "Meow"
