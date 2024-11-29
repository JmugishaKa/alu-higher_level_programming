#!/usr/bin/python3
"""Fetch a url"""

import requests


if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    print("Body response:\n\t- type: {}\n\t- content: {}".format(type(response.text), 
        "OK" if response.status_code == 200 
        else response.text))
