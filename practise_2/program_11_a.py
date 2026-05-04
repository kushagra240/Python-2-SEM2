with open("sample.txt", "r") as file:
    content = file.read()
    words = len(content.split())
    characters = len(content)
    lines = len(content.split("\n"))
    print("Words:", words, "Characters:", characters, "Lines:", lines)
