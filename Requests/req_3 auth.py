import requests
from pathlib import Path


script_location = Path(__file__).absolute().parent
file_location = script_location / "python.png"

# https://httpbin.org/
url = "https://httpbin.org/basic-auth/zhang3/123456"


response = requests.get(url, auth=("zhang3", "123456"))

print(response.text)
print(response.status_code)
print(response.ok)
print(response.url)
