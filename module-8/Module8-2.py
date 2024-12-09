# Colton Kohler
# 12/8/2024
# Module 8.2 Assignment

import json
import tkinter
from tkinter import messagebox

# Load data from the JSON file
def load_students(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

# Print function for displaying the student list
def print_students(students, message):
    print(f"\n{message}")
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Update the student list
def add_student(students, l_name, f_name, student_id, email):
    new_student = {
        "L_Name": l_name,
        "F_Name": f_name,
        "Student_ID": student_id,
        "Email": email
    }
    students.append(new_student)

# Save updated data to the JSON file
def save_students(filename, students):
    with open(filename, 'w') as file:
        json.dump(students, file, indent=4)
    print(f"\nThe {filename} file was updated.")

# Main program
def main():
    filename = r"C:\Users\colko\Directories\CSD\csd-325\module-8\student.json"  # Full path to the JSON file
    
    # Step 1: Load the original student list
    students = load_students(filename)
    if not students:
        return

    # Step 2: Print the original list
    print_students(students, "This is the original Student list:")

    # Step 3: Add a new student
    add_student(students, "Kohler", "Colton", 58365, "ckohler@my365.bellevue.edu")

    # Step 4: Print the updated list
    print_students(students, "This is the updated Student list:")

    # Step 5: Prompt user with a system pop-up to save changes
    root = tkinter.Tk()
    root.withdraw()  # Hide the root window

    message = f"This file has been modified: {filename}\nWould you like to save?"
    choice = messagebox.askyesno("Save Changes", message)
    if choice:
        save_students(filename, students)
    else:
        print("\nChanges were not saved to the file.")

# Execute the main function
if __name__ == "__main__":
    main()
