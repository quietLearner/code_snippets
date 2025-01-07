import re


def print_matches(search, text):

    pattern = re.compile(search, re.IGNORECASE)

    matches = pattern.finditer(text)
    for m in matches:
        print(m)


text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""

sentence = "Start a sentence and then bring it to an end"

# r stands for raw string, search for abc in the sentence
print_matches(r"abc", text_to_search)

print_matches(r"\bHa", text_to_search)


print_matches(r"^Start", sentence)

print_matches(r"end$", sentence)


# match phone numbers
print_matches(r"\d{3}.\d{3}.\d{4}", text_to_search)

# match Mr. and Mrs. names
print_matches(r"M[rs]\.?\s[A-Z]\w*", text_to_search)
