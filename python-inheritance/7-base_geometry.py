#!/usr/bin/python3
'''Class Rectangle that inherits from BaseGeometry'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class that inherits the BaseGeometry '''

    def __init__(self, width, height):
        '''Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        '''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height
