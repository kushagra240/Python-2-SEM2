import csv
import json

from student_backend import Student, add_student, display_students, remove_student, reverse_students, students, update_student


CSV_FILE = "student_records.csv"
JSON_FILE = "student_records.json"


def save_data():
    records = [student.to_dict() for student in students]
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age", "roll_no", "branch", "marks"])
        writer.writeheader()
        writer.writerows(records)
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=2)
    print("Saved")


def load_data():
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            records = json.load(file)
    except FileNotFoundError:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
            records = list(csv.DictReader(file))
    students.clear()
    for record in records:
        add_student(record["name"], int(record["age"]), record["roll_no"], record["branch"], float(record["marks"]))
    print("Loaded")


def main():
    while True:
        print("\n1.Add 2.Remove 3.Update 4.Reverse 5.Display 6.Save 7.Load 8.Exit")
        choice = input("Enter choice: ")
        try:
            if choice == "1":
                add_student(input("Name: "), int(input("Age: ")), input("Roll No: "), input("Branch: "), float(input("Marks: ")))
            elif choice == "2":
                print("Removed" if remove_student(input("Roll No to remove: ")) else "Not found")
            elif choice == "3":
                print("Updated" if update_student(input("Roll No to update: "), input("New Name: ")) else "Not found")
            elif choice == "4":
                reverse_students()
            elif choice == "5":
                display_students()
            elif choice == "6":
                save_data()
            elif choice == "7":
                load_data()
            elif choice == "8":
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input")
        except FileNotFoundError:
            print("File not found")
        except Exception as error:
            print("Error:", error)


if __name__ == "__main__":
    main()