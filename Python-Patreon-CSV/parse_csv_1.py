import csv
from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "test.csv"

# Open the CSV file
with open(file_location, "r") as file:
    # Create a CSV reader
    reader = csv.reader(file)

    next(reader)  # Skip the header row

    # Loop through each row in the CSV
    for row in reader:
        print(row)

# writing to a csv file
new_file_location = script_location / "new_test.csv"
with open(file_location, "r") as file:
    print(__name__)
    reader = csv.reader(file)

    # https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
    with open(new_file_location, "w", newline="") as new_file:
        writer = csv.writer(new_file, delimiter="|")

        for row in reader:
            writer.writerow(row)

print(__name__)  # __main__ if run directly, otherwise the module(file) name

if __name__ == "__main__":
    print("直接执行")
else:
    print("被导入执行")
