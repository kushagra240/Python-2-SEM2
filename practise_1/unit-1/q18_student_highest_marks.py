students = {"Asha": 89, "Ravi": 95, "Neha": 92}

topper = max(students, key=students.get)
print("Top student:", topper)
print("Marks:", students[topper])
