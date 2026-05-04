try:
    attendance = float(input("Enter attendance percentage: "))
    if attendance < 75:
        raise Exception("Attendance must be at least 75%")
    print("Attendance:", attendance)
except Exception as e:
    print("Error:", e)
