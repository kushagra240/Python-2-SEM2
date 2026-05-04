students = []


def add_student():
    name = input("Name: ")
    students.append(name)


def remove_student():
    name = input("Name to remove: ")
    if name in students:
        students.remove(name)
        print("Removed")
    else:
        print("Not found")


def reverse_students():
    students.reverse()


add_student()
remove_student()
reverse_students()
print(students)