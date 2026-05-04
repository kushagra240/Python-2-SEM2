set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

common = set1 & set2
set1 = set1 - common
set2 = set2 - common

print("Set 1:", set1)
print("Set 2:", set2)
