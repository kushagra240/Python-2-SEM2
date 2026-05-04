class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, branch, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.branch = branch
        self.marks = marks

    def to_dict(self):
        return {"name": self.name, "age": self.age, "roll_no": self.roll_no, "branch": self.branch, "marks": self.marks}


students = []


def add_student(name, age, roll_no, branch, marks):
    students.append(Student(name, age, roll_no, branch, marks))


def remove_student(roll_no):
    for student in students:
        if student.roll_no == roll_no:
            students.remove(student)
            return True
    return False


def update_student(roll_no, new_name):
    for student in students:
        if student.roll_no == roll_no:
            student.name = new_name
            return True
    return False


def reverse_students():
    students.reverse()


def display_students():
    for student in students:
        print(student.to_dict())