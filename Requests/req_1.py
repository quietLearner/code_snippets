import requests
from pathlib import Path


script_location = Path(__file__).absolute().parent
file_location = script_location / "python.png"

# url = "https://xkcd.com/353/"
url_image = "https://imgs.xkcd.com/comics/python.png"
response = requests.get(url_image)

# what attributes and methods does the response object have?
# print(dir(response))

# print(help(response))

with open(file_location, "wb") as file:
    file.write(requests.get(url_image).content)


print(response.headers)
print(response.status_code)
print(response.ok)
print(response.reason)

#
# https://httpbin.org/
