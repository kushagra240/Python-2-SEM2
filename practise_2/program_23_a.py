with open("source.txt", "r") as source:
    content = source.read()

with open("destination.txt", "w") as dest:
    dest.write(content)

print("File copied")
