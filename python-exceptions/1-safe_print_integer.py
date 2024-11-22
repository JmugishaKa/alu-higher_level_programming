#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

if __name__ == "__main__":
    # Example usage:
    value1 = 42
    value2 = "not_an_integer"

    if safe_print_integer(value1):
        print("Successfully printed an integer.")
    else:
        print("Failed to print an integer.")

    if safe_print_integer(value2):
        print("Successfully printed an integer.")
    else:
        print("Failed to print an integer.")
