class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A"
        if self.marks >= 75:
            return "B"
        if self.marks >= 60:
            return "C"
        return "D"

    def display(self):
        print(self.name, self.roll_number, self.marks, self.grade())


Student("Neha", 102, 84).display()
