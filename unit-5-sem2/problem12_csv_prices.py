import csv

total = 0
valid_count = 0

try:
    with open("prices.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            try:
                cost = float(row["Cost"])
                total = total + cost
                valid_count = valid_count + 1
            except ValueError:
                print("Error: Invalid cost for", row["Product"])
except FileNotFoundError:
    print("Error: prices.csv not found")
else:
    print("Total cost of valid products:", total)
    print("Valid products counted:", valid_count)
