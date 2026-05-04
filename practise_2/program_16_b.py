try:
    price = float(input("Enter product price: "))
    if price < 0:
        raise Exception("Price cannot be negative")
    print("Price:", price)
except Exception as e:
    print("Error:", e)
