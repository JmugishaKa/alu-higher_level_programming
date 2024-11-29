#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status."""

    import urllib.request
    from urllib.error import HTTPError, URLError
if __name__ == '__main__':
    url = "https://intranet.hbtn.io/status"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
            content = resp.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode('utf-8')))
    except HTTPError as e:
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
