try:
    number = int(input("Enter a number: "))
    if number < 0:
        raise Exception("Negative number not allowed")
    print("Number is:", number)
except Exception as e:
    print("Error:", e)
