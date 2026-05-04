with open("user_input.txt", "w") as file:
    print("Enter lines (type 'quit' to stop):")
    while True:
        line = input()
        if line == "quit":
            break
        file.write(line + "\n")

print("File created with user input")
