import os
from pathlib import Path
from requests_html import HTML


script_location = Path(__file__).absolute().parent
file_location = script_location / "simple.html"


with open(file_location, "r") as html_file:
    source = html_file.read()
    html = HTML(html=source)

print(html.html)
print(html.text)

match = html.find("title")
print(match[0].text, match[0].html)

match = html.find("#footer", first=True)
print(match.text)


article = html.find("div.article", first=True)
headline = article.find("h2", first=True)
summary = article.find("p", first=True)
print(headline.text, summary.text)
