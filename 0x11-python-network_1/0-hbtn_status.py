#!/usr/bin/python3
"""
 Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
   from urllib.request import urlopen

   with urlopen("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()
        print(f"""Body response:
\t- type: {type(body)}
\t- content: {body}
\t- utf8 content: {body.decode('utf-8')} """)
