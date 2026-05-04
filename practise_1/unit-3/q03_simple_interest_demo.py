import simple_interest


principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

print(simple_interest.calculate_simple_interest(principal, rate, time))
