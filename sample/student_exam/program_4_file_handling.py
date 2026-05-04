import csv
import json


students = [{"name": "Asha", "age": 20, "marks": 85}]


with open("student.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "marks"])
    writer.writeheader()
    writer.writerows(students)

try:
    with open("student.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print(list(reader))
except FileNotFoundError:
    print("CSV file not found")

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=2)

try:
    with open("student.json", "r", encoding="utf-8") as file:
        print(json.load(file))
except FileNotFoundError:
    print("File not found")