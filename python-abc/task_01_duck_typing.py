#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Calculates the area of the shape.

        Returns:
            float: Area of the shape.
        """
        ...

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape.

        Returns:
            float: Perimeter of the shape.
        """
        ...


class Circle(Shape):
    """Represents a circle."""

    def __init__(self, radius):
        """Initializes a circle with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Calculates the area of the circle.

        Returns:
            float: Area of the circle.
        """
        return pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates the perimeter (circumference) of the circle.

        Returns:
            float: Perimeter of the circle.
        """
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Represents a rectangle."""

    def __init__(self, width, height):
        """Initializes a rectangle with width and height.

        Args:
            width (float): Width of the rectangle.
            height (float): Height of the rectangle.
        """
        self.height = height
        self.width = width

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            float: Area of the rectangle.
        """
        return self.height * self.width

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            float: Perimeter of the rectangle.
        """
        return (self.height + self.width) * 2


def shape_info(my_shape):
    """Displays the shape's area and perimeter.

    Args:
        my_shape (Shape): An instance of Shape or one of its subclasses.
    """
    print(f"Area: {my_shape.area()}")
    print(f"Perimeter: {my_shape.perimeter()}")
