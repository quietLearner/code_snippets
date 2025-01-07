import os
from pathlib import Path

script_dir = Path(__file__).parent.resolve()
print(script_dir)
my_file = script_dir / "my_file.txt"

print(locals())

try:
    f = open(my_file, "r")
    print(f.read())

    print(locals())

except FileNotFoundError:
    print(f"File {my_file} not found")
except IOError as e:
    print(f"File can not be accessed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    f.close() if "f" in locals() else None
