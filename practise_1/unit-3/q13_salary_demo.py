import salary as sal


basic = float(input("Enter basic salary: "))
hra = float(input("Enter HRA: "))
da = float(input("Enter DA: "))
print(sal.gross_salary(basic, hra, da))
print(sal.deductions(basic))
print(sal.net_salary(basic, hra, da))
