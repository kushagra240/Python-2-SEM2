import currency_converter as cc


amount = float(input("Enter amount in USD: "))
choice = int(input("Enter choice (1-INR, 2-EUR, 3-GBP): "))

if choice == 1:
	print(cc.usd_to_inr(amount))
elif choice == 2:
	print(cc.usd_to_eur(amount))
else:
	print(cc.usd_to_gbp(amount))
