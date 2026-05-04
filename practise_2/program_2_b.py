try:
    marks = float(input("Enter marks: "))
    if marks < 0 or marks > 100:
        raise Exception("Marks must be between 0 and 100")
    print("Marks are:", marks)
except Exception as e:
    print("Error:", e)
