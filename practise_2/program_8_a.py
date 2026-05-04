with open("sample.txt", "r") as file:
    words = file.read().split()
    longest = max(words, key=len)
    print("Longest word:", longest)
