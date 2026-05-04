import student_utils as su


name = input("Enter student name: ")
marks = [float(input("Enter mark 1: ")), float(input("Enter mark 2: ")), float(input("Enter mark 3: "))]
student = su.add_student_details(name, marks)
average = su.calculate_average_marks(student["marks"])
print(student["name"])
print(average)
print(su.determine_grade(average))
