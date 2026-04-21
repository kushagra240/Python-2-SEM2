colors = ["Red", "Blue", "Green", "Yellow", "Orange"]

try:
    index = int(input("Enter index (0-4): "))
    print("Color:", colors[index])
except IndexError:
    print("Error: Index out of range. Choose 0-4")
except ValueError:
    print("Error: Please enter a valid number")
