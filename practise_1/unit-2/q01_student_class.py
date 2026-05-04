class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        print(self.name, self.roll_number, self.marks)


student = Student("Asha", 101, 88)
student.display()
