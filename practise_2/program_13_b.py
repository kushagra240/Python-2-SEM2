try:
    print("Opening file")
    file = open("sample.txt", "r")
    print(file.read())
finally:
    file.close()
    print("File closed")
