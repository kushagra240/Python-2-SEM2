class Employee:
    def __init__(self, name, employee_id, salary, department):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.department = department

    def display(self):
        print(self.name, self.employee_id, self.salary, self.department)

    def bonus(self):
        return self.salary * 0.1


employee = Employee("Ravi", 1, 50000, "IT")
employee.display()
print("Bonus:", employee.bonus())
