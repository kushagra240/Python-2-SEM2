import csv

user_id = input("Enter User ID: ")
product = input("Enter Product: ")
price = input("Enter Price: ")

with open("sales.csv", "a", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([user_id, product, price])

print("New row added to sales.csv")

with open("sales.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
