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

    def to_json(self, attrs=None):
        """converts the Student instance into
        a serializable json object.
        Only attributes listed in attrs should be used"""
        my_json_dict = {}
        if attrs is None:
            return self.__dict__
        else:
            for key in self.__dict__:
                if key in attrs:
                    my_json_dict[key] = self.__dict__[key]
            return my_json_dict
