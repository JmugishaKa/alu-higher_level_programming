#!/usr/bin/python3
""" This function 'add_integer' takes in two arguments """
""" and returns the sum of the two."""

# Check if required files are present
try:
    with open("tests/0-add_integer.txt", "r"):
        pass
except FileNotFoundError:
    print("Missing: tests/0-add_integer.txt")

try:
    with open("0-add_integer.py", "r"):
        pass
except FileNotFoundError:
    print("Missing: 0-add_integer.py")


def add_integer(a, b=98):
    """ Should the conditions be met, Raising the type error message """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
