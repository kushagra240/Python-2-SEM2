from package.student_module import Student


try:
    student = Student(input("Name: "), int(input("Age: ")), float(input("Marks: ")))
    student.display()
except ValueError:
    print("Invalid input")