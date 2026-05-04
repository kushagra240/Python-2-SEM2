import csv
import json

books=[{"title":"abcd","author":"qwerty"},{"title":"xyz","author":"hey"}]

with open("books.csv","w", newline="",encoding="utf-8") as file:
    writer=csv.DictWriter(file, fieldnames=["title","author"])
    writer.writeheader()
    writer.writerows(books)

with open("books.json","w", encoding="utf-8") as file:
    json.dump(books, file, indent=2)

try:
    with open("books.csv","r",encoding="utf-8") as file:
        reader=csv.DictReader(file)
        print(list(reader))
except FileNotFoundError:
    print("csv file not found")

try:
    with open("books.json","r", encoding="utf-8") as file:
        print(json.load(file))
except FileNotFoundError:
    print("json file not found")
    
    
     

                                           