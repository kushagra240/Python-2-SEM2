try:
    text = input("Enter a string: ")
    reversed_text = text[::-1]
    print("Reversed:", reversed_text)
except Exception as e:
    print("Error:", e)
