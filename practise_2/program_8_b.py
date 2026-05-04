class FileError(Exception):
    pass

try:
    filename = input("Enter filename: ")
    if not filename:
        raise FileError("Filename cannot be empty")
    print("File:", filename)
except FileError as e:
    print("Error:", e)
