import json

data = {"name": "Asha", "age": 20, "city": "Pune"}

with open("data.json", "w") as file:
    json.dump(data, file)

print("Dictionary saved to JSON")
