with open("input.txt", "r") as file:
    lines = [line for line in file if line.strip()]

with open("output.txt", "w") as file:
    file.writelines(lines)

print("Blank lines removed")
