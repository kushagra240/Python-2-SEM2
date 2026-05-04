def add_student_details(name, marks):
    return {"name": name, "marks": marks}


def calculate_average_marks(marks):
    return sum(marks) / len(marks)


def determine_grade(average_marks):
    if average_marks >= 90:
        return "A"
    if average_marks >= 75:
        return "B"
    if average_marks >= 60:
        return "C"
    return "D"
