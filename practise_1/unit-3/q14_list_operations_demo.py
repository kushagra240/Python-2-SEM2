import list_operations as lo


numbers = [int(value) for value in input("Enter numbers separated by space: ").split()]
print(lo.find_maximum(numbers))
print(lo.find_minimum(numbers))
print(lo.sort_list(numbers))
print(lo.remove_duplicates(numbers))
