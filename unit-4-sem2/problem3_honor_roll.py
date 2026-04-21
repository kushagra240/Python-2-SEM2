import csv

with open("students.csv", "r", newline="") as csv_file:
    reader = csv.DictReader(csv_file)

    with open("honor_roll.txt", "w") as output_file:
        for row in reader:
            if float(row["Score"]) > 80:
                output_file.write(row["Name"] + "\n")

print("honor_roll.txt created")
with open("honor_roll.txt", "r") as f:
    print(f.read())
