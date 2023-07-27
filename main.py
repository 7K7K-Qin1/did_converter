from core import Core
import csv

input_file = "data/input.csv"

# Read the data from the CSV file
input_data = []
with open(input_file, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row
    for row in csvreader:
        input_data.append(row[0])

    username = "Tom"

    core = Core()
    core.execute(input_data, username)
