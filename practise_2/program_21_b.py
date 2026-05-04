try:
    value = input("Enter value: ")
    number = int(value)
except ValueError:
    print("Invalid integer")
except Exception as e:
    print("General error:", e)
