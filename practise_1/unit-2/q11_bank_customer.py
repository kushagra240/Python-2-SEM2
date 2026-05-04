class BankCustomer:
    def __init__(self, customer_name, account_type, balance):
        self.customer_name = customer_name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def display_balance(self):
        print(self.customer_name, self.account_type, self.balance)


customer = BankCustomer("Ravi", "Savings", 2000)
customer.deposit(300)
customer.display_balance()
