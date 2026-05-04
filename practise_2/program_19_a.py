import json

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

linked_list = [1, 2, 3, 4, 5]

with open("linked_list.json", "w") as file:
    json.dump(linked_list, file)

with open("linked_list.json", "r") as file:
    data = json.load(file)

print("Linked list serialized and deserialized:", data)
