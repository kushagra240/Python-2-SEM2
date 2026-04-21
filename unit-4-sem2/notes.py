count = 0

with open("notes.txt", "r") as f:
	for line in f:
		if line.startswith("A"):
			count = count + 1

print("Lines starting with A:", count)
