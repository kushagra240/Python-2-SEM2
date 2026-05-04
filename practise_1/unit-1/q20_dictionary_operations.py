student1 = {"name": "Asha", "marks": 90}
student2 = {"city": "Pune", "grade": "A"}

student1.pop("marks")
merged = {**student1, **student2}

print("After removal:", student1)
print("Merged dictionary:", merged)