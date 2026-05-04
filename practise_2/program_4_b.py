try:
    a = float(input("Enter dividend: "))
    b = float(input("Enter divisor: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
