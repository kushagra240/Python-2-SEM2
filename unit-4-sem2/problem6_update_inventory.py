import json

item_name = input("Enter item name to update: ")
new_quantity = int(input("Enter new quantity: "))

with open("inventory.json", "r") as json_file:
    inventory = json.load(json_file)

updated = False
for item in inventory:
    if item["Item"].lower() == item_name.lower():
        item["Quantity"] = new_quantity
        updated = True
        break

with open("inventory.json", "w") as json_file:
    json.dump(inventory, json_file, indent=4)

if updated:
    print("inventory.json updated")
else:
    print("Item not found. No change made.")
