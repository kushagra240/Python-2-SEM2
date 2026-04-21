import json

book = {
    "Title": "The Alchemist",
    "Author": "Paulo Coelho",
    "Year": 1988
}

with open("library.json", "w") as json_file:
    json.dump(book, json_file, indent=4)

print("library.json created")
