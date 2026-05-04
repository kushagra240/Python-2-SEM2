try:
    items = []
    if len(items) == 0:
        raise Exception("List is empty")
    print(items[0])
except Exception as e:
    print("Error:", e)
