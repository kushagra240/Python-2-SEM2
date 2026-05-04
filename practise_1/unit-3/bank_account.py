def deposit(balance, amount):
    return balance + amount


def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount
    return balance


def check_balance(balance):
    return balance
