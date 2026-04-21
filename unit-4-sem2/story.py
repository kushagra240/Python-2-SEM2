with open("story.txt", "r") as f:
	text = f.read()

with open("upper_story.txt", "w") as u:
	u.write(text.upper())

print("upper_story.txt created")

with open("upper_story.txt", "r") as g:
	print(g.read())