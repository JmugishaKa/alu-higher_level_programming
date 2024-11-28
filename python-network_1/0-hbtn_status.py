#!/usr/bin/python3
"""
This script fetches the status of a URL using urllib
and displays details about the response.
"""

from urllib import request

url = "https://alu-intranet.hbtn.io/status"

if __name__ == "__main__":
    with request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print(f"    - type: {type(content)}")
        print(f"    - content: {content}")
        print(f"    - utf8 content: {content.decode('utf-8')}")

