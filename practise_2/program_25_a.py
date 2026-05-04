import csv

total = 0
count = 0

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total += float(row["value"])
        count += 1

print("Average:", total / count)
