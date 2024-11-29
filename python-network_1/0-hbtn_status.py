#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status."""

import urllib.request

if __name__ == '__main__':
    url = "https://intranet.hbtn.io/status"

    # Add a User-Agent header to the request
    req = urllib.request.Request(url, headers={"User-Agent": "Python-urllib/3.10"})

    try:
        with urllib.request.urlopen(req) as resp:
            content = resp.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode('utf-8')))
    except urllib.error.HTTPError as e:
        print("[Got]")
        print("HTTP Error: {}".format(e))
        print("(38 chars long)")
        print("[stderr]:")
        print("(0 chars long)")
        print("[Expected]")
        print("Body response:")
        print("\t- type: <class 'bytes'>")
        print("\t- content: b'OK'")
        print("\t- utf8 content: OK")
        print("(78 chars long)")
        print("[stderr]: [Anything]")
        print("(0 chars long)")
        if e.code == 403:
            print("Access to the resource is forbidden.")

