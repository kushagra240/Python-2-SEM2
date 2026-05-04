numbers = [1, 2, 2, 3]
numbers.append(4)
numbers.extend([3, 5, 5])

unique_numbers = list(dict.fromkeys(numbers))

print("Original:", numbers)
print("Without duplicates:", unique_numbers)
