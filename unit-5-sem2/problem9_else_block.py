try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Error: Please enter a valid number")
else:
    print("Age recorded successfully")
