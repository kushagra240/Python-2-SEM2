try:
    value = int(input("Enter an integer: "))
    print("Integer:", value)
except ValueError:
    print("Error: Please enter a valid integer")
