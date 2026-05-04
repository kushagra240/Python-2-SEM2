word = input("Enter word to search: ")
count = 0

with open("sample.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        count += line.count(word)

print("Occurrences:", count)
