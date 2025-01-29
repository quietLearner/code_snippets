import os
from dotenv import load_dotenv

# take the environment variables from the .env file, instead of the system environment variables
load_dotenv(override=False)

API_KEY = os.getenv("API_KEY")

print(API_KEY)


USER = os.getenv("USER")
print(USER)

# WARNING: This will print the system environment variables, not the .env file
PATH = os.getenv("PATH")
print(PATH)


ADDR = os.getenv("ADDR")
print(ADDR)


COMMENT = os.getenv("COMMENT")
print(COMMENT)

EMAIL = os.getenv("EMAIL")
print(EMAIL)
