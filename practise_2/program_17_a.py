import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["age"]) > 20:
            print(row)
