import csv
import json


players = [{"name": "Virat", "age": 36, "team": "RCB", "runs": 7000}]


with open("players.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "team", "runs"])
    writer.writeheader()
    writer.writerows(players)

with open("players.json", "w", encoding="utf-8") as file:
    json.dump(players, file, indent=2)

try:
    with open("players.json", "r", encoding="utf-8") as file:
        print("JSON Data:")
        print(json.load(file))
except FileNotFoundError:
    print("File not found")

try:
    with open("players.csv", "r", encoding="utf-8") as file:
        print("\nCSV Data:")
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File not found")