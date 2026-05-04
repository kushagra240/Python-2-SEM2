class NegativeNumberError(Exception):
    pass

try:
    number = int(input("Enter a number: "))
    if number < 0:
        raise NegativeNumberError("Number cannot be negative")
    print("Number:", number)
except NegativeNumberError as e:
    print("Error:", e)
