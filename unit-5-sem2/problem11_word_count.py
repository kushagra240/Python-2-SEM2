try:
    f = open("data.txt", "r")
    text = f.read()
    words = text.split()
    word_count = len(words)
    print("Total words:", word_count)
except FileNotFoundError:
    print("Error: data.txt not found")
finally:
    print("File has been closed")
