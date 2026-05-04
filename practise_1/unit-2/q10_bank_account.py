class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def check_balance(self):
        print("Balance:", self.balance)


account = BankAccount("123456", 1000)
account.deposit(500)
account.withdraw(200)
account.check_balance()
