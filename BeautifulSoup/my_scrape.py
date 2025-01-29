from bs4 import BeautifulSoup
import requests
import csv
import os
from pathlib import Path


script_location = Path(__file__).absolute().parent
file_location = script_location / "simple.html"

with open(file_location) as html_file:
    soup = BeautifulSoup(html_file, "lxml")

# why soup can be used outside the with block?

match = soup.title.text
print(match)

footer = soup.find("div", class_="footer")
print(footer)
