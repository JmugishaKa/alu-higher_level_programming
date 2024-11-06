#!/usr/bin/python3
"""define the square"""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initializes a square with a given size."""
        self.size = size

    @property
    def size(self):
        """Getter method for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Defines equality comparison."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Defines inequality comparison."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Defines less than comparison."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Defines less than or equal to comparison."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False

    def __gt__(self, other):
        """Defines greater than comparison."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Defines greater than or equal to comparison."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False
