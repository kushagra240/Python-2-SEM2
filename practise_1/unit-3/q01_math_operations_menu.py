import math_operations as mo


choice = int(input("Enter choice (1-add, 2-subtract, 3-multiply, 4-divide): "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print(mo.add(a, b))
elif choice == 2:
    print(mo.subtract(a, b))
elif choice == 3:
    print(mo.multiply(a, b))
else:
    print(mo.divide(a, b))
