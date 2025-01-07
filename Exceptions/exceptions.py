from pathlib import Path
import os

# https://docs.python.org/3/library/exceptions.html

# https://llego.dev/posts/properly-closing-files-python-even-exceptions/

script_location = Path(__file__).absolute().parent
file_location = script_location / "currupt_file.txt"


try:
    f = open(file_location, "r")
    # var = bad_var
    print(f.name)
    if os.path.basename(f.name) == "currupt_file.txt":
        raise Exception("This is a bad file")
except FileNotFoundError as e:
    print(e)
    print("First!")
except IOError as e:
    print(e)
    print("Secord!")
except Exception as e:
    print(e)
    print("Thrid")
else:
    print("outside exception block", f.read())
    # f.close()
finally:
    print("Executing Finally...")
    try:
        f.close()
    except:
        pass
    print("File Closed")
