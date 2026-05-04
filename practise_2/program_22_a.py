import json

with open("data.json", "r") as file:
    data = json.load(file)

extracted = {key: data[key] for key in ["name", "age"]}

with open("extracted.json", "w") as file:
    json.dump(extracted, file)

print("Fields extracted")
