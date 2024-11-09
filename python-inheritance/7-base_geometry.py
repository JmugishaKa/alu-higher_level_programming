#!/user/bin/python3
class BaseGeometry:
    """
    A base class for geometric shapes that provides methods for 
    calculating areas and validating integer input.
    """

    def area(self):
        """
        Raises an exception because the area() method is not implemented 
        in the base class. This should be overridden by subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is an integer greater than 0.

        Parameters:
        - name: The name of the parameter being validated (str).
        - value: The value to be validated (int).

        Raises:
        - TypeError: If 'value' is not an integer.
        - ValueError: If 'value' is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

