#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status using urllib and displays response details."""

from urllib import request

url = "https://alu-intranet.hbtn.io/status"

if __name__ == "__main__":
    # Use `with` statement to manage the HTTP request
    with request.urlopen(url) as response:
        # Read the body of the response
        content = response.read()
        # Display the output as specified
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")

