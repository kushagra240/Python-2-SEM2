try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print("Result:", result)
except ValueError:
    print("Error: Please enter valid numbers")
finally:
    print("Execution Complete")
