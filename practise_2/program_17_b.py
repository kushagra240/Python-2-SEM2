try:
    items = int(input("Enter list size: "))
    if items > 10:
        raise Exception("List cannot exceed 10 elements")
    print("List size:", items)
except Exception as e:
    print("Error:", e)
