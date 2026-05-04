try:
    number = int(input("Enter a number (1-50): "))
    if number < 1 or number > 50:
        raise Exception("Number must be between 1 and 50")
    print("Number:", number)
except Exception as e:
    print("Error:", e)
