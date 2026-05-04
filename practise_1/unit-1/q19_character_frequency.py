text = "banana"
frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

print(frequency)
