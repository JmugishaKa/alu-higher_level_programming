#!/usr/bin/python3
"""Script to fetch a URL and handle restricted access."""

from urllib import request, error

if __name__ == '__main__':
    url = "https://intranet.hbtn.io/status"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://intranet.hbtn.io/",
    }
    req = request.Request(url, headers=headers)

    try:
        with request.urlopen(req) as response:
            content = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode('utf-8')))
    except error.HTTPError as e:
        print(f"HTTP Error: {e}")
    except error.URLError as e:
        print(f"URL Error: {e}")

