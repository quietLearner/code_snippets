import requests
from pathlib import Path


script_location = Path(__file__).absolute().parent
file_location = script_location / "python.png"

# https://httpbin.org/
# url = "https://httpbin.org/get"
url = "https://httpbin.org/post"


payload = {"username": "zhang3", "password": "123456"}
# response = requests.get(url, params=payload)
response = requests.post(url, data=payload)

print(response.text)
print(response.status_code)

print(response.ok)
print(response.url)

print(response.json())

r_json = response.json()
print(r_json["form"])
