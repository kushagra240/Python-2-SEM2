import json

data = {"name": "Ravi", "age": 22, "city": "Delhi"}

with open("data.json", "w") as file:
    json.dump(data, file)

print("Dictionary saved to JSON")
