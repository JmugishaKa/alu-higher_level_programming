#!/usr/bin/python3
"""Fetch a url"""

import requests
    
if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text.strip()))

    # Extract "OK" from the response text
    if "OK" in response.text:
        print("\t- content: OK")
    else:
        print("\t- content: Not Found")
