def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for character in text if character in vowels)


def reverse_string(text):
    return text[::-1]


def is_palindrome(text):
    return text == text[::-1]
