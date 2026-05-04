def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


def is_palindrome(text):
    text = str(text)
    return text == text[::-1]
