class AgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise AgeError("Age must be at least 18")
    print("Age:", age)
except AgeError as e:
    print("Error:", e)
