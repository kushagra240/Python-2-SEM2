import csv

with open("data.csv", "r") as file:
    reader = list(csv.reader(file))

reader[1] = ["John", "25", "100"]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(reader)

print("Row updated")
