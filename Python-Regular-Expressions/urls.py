import re

urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")


matches = pattern.finditer(urls)

for match in matches:
    print(match.group(1), match.group(2), match.group(3))

# replace/substitue the urls with group 2 and group 3
# \2 is group 2, \3 is group 3
subbed_urls = pattern.sub(r"\2\3", urls)

print(subbed_urls)
