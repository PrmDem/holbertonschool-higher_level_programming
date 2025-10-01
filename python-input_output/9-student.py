#!/usr/bin/python3

"""After creating a Student class, returns
a dictionary description for json serialization"""


class Student:
    """represents a student with full name and age"""
    def __init__(self, first_name, last_name, age):
        """defines a Student instance

        first_name (str): a student's first name
        last_name (str): a student's last name
        age (int): a student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """converts the Student instance into
        a serializable json object"""
        return self.__dict__
