class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def bonus(self):
        return self.basic_salary * 0.2

    def total_salary(self):
        return self.basic_salary + self.bonus()


employee = Employee("Asha", 30000)
print("Bonus:", employee.bonus())
print("Total salary:", employee.total_salary())
