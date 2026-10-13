"""Mini Project (W2):
“Student Management System”
● Store student data (name, marks, roll number) in a CSV file
● Add/Delete/Search functions
● Save changes permanently to file"""

import csv
import os

FILE_NAME = "students.csv"

# Create CSV file if it does not exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll Number", "Name", "Marks"])


# Add a student
def add_student():
    roll = input("Enter roll number: ")

    # Check for duplicate roll number
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for student in reader:
            if student["Roll Number"] == roll:
                print("Roll number already exists!")
                return

    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])

    print("Student added successfully!")


# Display all students
def display_students():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        students = list(reader)

    if not students:
        print("No student records found.")
        return

    for student in students:
        print(student)


# Search for a student
def search_student():
    roll = input("Enter roll number to search: ")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for student in reader:
            if student["Roll Number"] == roll:
                print("Student found:", student)
                return

    print("Student not found!")


# Delete a student
def delete_student():
    roll = input("Enter roll number to delete: ")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        students = list(reader)

    updated_students = [
        student for student in students
        if student["Roll Number"] != roll
    ]

    if len(updated_students) == len(students):
        print("Student not found!")
        return

    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["Roll Number", "Name", "Marks"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_students)

    print("Student deleted successfully!")


# Main menu
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting Student Management System.")
        break
    else:
        print("Invalid choice! Please try again.")
