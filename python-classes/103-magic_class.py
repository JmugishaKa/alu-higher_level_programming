#!/usr/bin/python3
"""Defines a MagicClass."""

import math


class MagicClass:
    """Represents a magic class."""

    def __init__(self, radius=0):
        """Initializes the MagicClass instance."""
        self._MagicClass__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self._MagicClass__radius = radius

    def area(self):
        """Calculates the area of the MagicClass instance."""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of the MagicClass instance."""
        return 2 * math.pi * self._MagicClass__radius
