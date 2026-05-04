items = [10, 20, 30]
print("Original list:", items)
print("First element:", items[0])

items.append(40)
items.insert(1, 15)
print("After add:", items)

items.remove(20)
del items[-1]
print("After remove:", items)
