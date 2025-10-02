#!/usr/bin/python3

"""Custom object serialization module.

This module defines the `CustomObject` class, which demonstrates
object-oriented programming concepts such as initialization, displaying
attributes, and persistence through serialization and deserialization.

Features:
    - Create a `CustomObject` with a name, age, and student status.
    - Serialize an object to a file using the `pickle` module.
    - Deserialize an object from a file.
    - Handle file-related and pickle-related errors gracefully.

Example:
    >>> obj = CustomObject("Alice", 25, True)
    >>> obj.serialize("object.pkl")
    True
    >>> loaded = CustomObject.deserialize("object.pkl")
    >>> loaded.display()
    Name: Alice
    Age: 25
    Is Student: True
"""
import pickle


class CustomObject:
    """A simple class that represents a custom object with basic attributes.

    This class supports displaying attributes, as well as serializing
    and deserializing instances using the `pickle` module.
    """

    def __init__(self, name, age, is_student):
        """Initializes a CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the attributes of the object.

        Prints the name, age, and student status to the console.
        """
        print(f"Name: {self.name}\n"
              "Age: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current object to a file using pickle.

        Args:
            filename (str): The path of the file
                where the object will be saved.

        Returns:
            bool: True if serialization succeeds, False if it fails.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            return True
        except (OSError, pickle.PickleError):
            return False

    @classmethod
    def deserialize(cls, filename):
        """Deserializes an object from a file using pickle.

        Args:
            filename (str): The path of the file to load the object from.

        Returns:
            CustomObject | None: The deserialized object if successful,
            or None if deserialization fails.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (OSError, pickle.PickleError, EOFError):
            return None
