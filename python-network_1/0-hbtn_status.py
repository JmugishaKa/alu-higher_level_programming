#!/usr/bin/python3
"""
Fetches https://alu-intranet.hbtn.io/status and handles potential HTTP errors.
"""

from urllib import request, error

url = "https://alu-intranet.hbtn.io/status"

if __name__ == "__main__":
    # Add a custom User-Agent header
    req = request.Request(url, headers={"User-Agent": "Python-urllib/3.10"})

    try:
        with request.urlopen(req) as response:
            content = response.read()
            print("Body response:")
            print(f"    - type: {type(content)}")
            print(f"    - content: {content}")
            print(f"    - utf8 content: {content.decode('utf-8')}")
    except error.HTTPError as e:
        print(f"HTTP Error: {e}")
    except error.URLError as e:
        print(f"URL Error: {e}")

