try:
    char = input("Enter a character: ")
    if char.lower() not in "aeiou":
        raise Exception("Character must be a vowel")
    print("Character is a vowel")
except Exception as e:
    print("Error:", e)
