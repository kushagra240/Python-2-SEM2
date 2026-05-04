class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city


class Teacher(Person):
    def __init__(self, name, city, subject, salary):
        super().__init__(name, city)
        self.subject = subject
        self.salary = salary

    def display(self):
        print(self.name, self.city, self.subject, self.salary)


Teacher("Asha", "Pune", "Maths", 40000).display()
