import json
import os

FILE_NAME = "students.json"

# Load existing data
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        students = json.load(file)
else:
    students = []


def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    name = input("Name: ")
    age = input("Age: ")
    grade = input("Grade: ")

    students.append({
        "name": name,
        "age": age,
        "grade": grade
    })

    save_data()
    print("Student added!")


def view_students():
    if not students:
        print("No students found.")
        return

    for i, s in enumerate(students, start=1):
        print(f"{i}. {s['name']} | Age: {s['age']} | Grade: {s['grade']}")


def search_student():
    name = input("Enter name to search: ")

    for s in students:
        if s["name"].lower() == name.lower():
            print(f"Found: {s['name']} | Age: {s['age']} | Grade: {s['grade']}")
            return

    print("Student not found.")


def delete_student():
    name = input("Enter name to delete: ")

    for s in students:
        if s["name"].lower() == name.lower():
            students.remove(s)
            save_data()
            print("Student deleted!")
            return

    print("Student not found.")


while True:
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
