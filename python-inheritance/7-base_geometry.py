#!/usr/bin/python3
"""
Defines the class BaseGeometry with public instance methods for:
1. Raising an exception for area (intended to be implemented by subclasses).
2. Validating that a value is a positive integer greater than 0.
"""

class BaseGeometry:
    """
    A base class for geometric shapes that provides methods for:
    1. Raising an exception if the area method is not implemented.
    2. Validating that a given value is an integer and greater than 0.
    """
    
    def area(self):
        """
        Raises an exception to indicate that the area method has not been 
        implemented in this base class. Subclasses are expected to implement
        the area method.

        Raises:
            Exception: Always raises an exception with the message 
                       "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer greater than 0.

        Args:
            name (str): The name of the parameter being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.

        Example:
            >>> bg = BaseGeometry()
            >>> bg.integer_validator("width", 5)  # No exception
            >>> bg.integer_validator("width", -5)  # Raises ValueError
            >>> bg.integer_validator("width", "five")  # Raises TypeError
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

