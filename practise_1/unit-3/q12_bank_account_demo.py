import bank_account as ba


balance = float(input("Enter initial balance: "))
choice = int(input("Enter choice (1-deposit, 2-withdraw, 3-check balance): "))

if choice == 1:
	amount = float(input("Enter deposit amount: "))
	balance = ba.deposit(balance, amount)
elif choice == 2:
	amount = float(input("Enter withdraw amount: "))
	balance = ba.withdraw(balance, amount)

print(ba.check_balance(balance))
