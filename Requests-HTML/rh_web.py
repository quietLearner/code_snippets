import os
from pathlib import Path
from requests_html import HTML, HTMLSession


session = HTMLSession()
r = session.get("https://google.ca")

print(r.html.html)
