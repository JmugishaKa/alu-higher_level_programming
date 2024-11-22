#!/usr/bin/python3
def raise_exception_msg(message=""):
    raise NameError(message)

if __name__ == "__main__":
    custom_message = "This is a custom name exception"
    try:
        raise_exception_msg(custom_message)
    except NameError as e:
        print("Exception caught: ", e)
