try:
    salary = float(input("Enter salary: "))
    if salary < 10000:
        raise Exception("Salary must be at least 10,000")
    print("Salary is:", salary)
except Exception as e:
    print("Error:", e)
