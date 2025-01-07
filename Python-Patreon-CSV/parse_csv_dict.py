import csv
from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "test.csv"

# Open the CSV file
with open(file_location, "r") as file:
    reader = csv.DictReader(file)

    # Loop through each row in the CSV
    for row in reader:
        print(row)
        print(row["Email"])


# writing to a csv file
with open(file_location, "r") as file:
    reader = csv.DictReader(file)
    new_file_location = script_location / "new_test_dict.csv"

    # https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
    with open(new_file_location, "w", newline="") as new_file:
        # fieldnames = reader.fieldnames
        fieldnames = [
            "FirstName",
            "LastName",
            "Email",
            # "Pledge",
            # "Lifetime",
            # "Status",
            # "Country",
            # "Start",
        ]

        writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter="|")

        # Write the header, otherwise it will be missing
        writer.writeheader()

        for row in reader:
            del row["Pledge"]
            del row["Lifetime"]
            del row["Status"]
            del row["Country"]
            del row["Start"]

            writer.writerow(row)
