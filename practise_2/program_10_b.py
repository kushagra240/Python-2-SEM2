try:
    number = int(input("Enter a number: "))
    if number % 2 != 0:
        raise Exception("Number is not even")
    print("Number is even")
except Exception as e:
    print("Error:", e)
