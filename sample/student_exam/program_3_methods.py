students = [
    {"name": "Asha", "age": 20},
    {"name": "Ravi", "age": 19},
]


def update_student():
    students[0]["name"] = "Asha Kumar"


def sort_students():
    students.sort(key=lambda student: student["name"])


update_student()
sort_students()
print(students)