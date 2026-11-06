# Task 9: Student Record Management System
# Records are stored in a list of dictionaries during program execution.

students = []

def add_student():
    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()
    branch = input("Enter branch: ").strip()

    if not name or not roll_no or not branch:
        print("All fields are required.")
        return

    if any(student["roll_no"].lower() == roll_no.lower() for student in students):
        print("A student with this roll number already exists.")
        return

    students.append({
        "name": name,
        "roll_no": roll_no,
        "branch": branch
    })
    print("Student record added successfully.")

def display_students():
    if not students:
        print("No student records found.")
        return

    print("\n========== STUDENT RECORDS ==========")
    for index, student in enumerate(students, start=1):
        print(f"{index}. Name: {student['name']} | "
              f"Roll No: {student['roll_no']} | Branch: {student['branch']}")
    print("=====================================")

def search_student():
    search_name = input("Enter the name to search: ").strip().lower()
    matches = [student for student in students
               if search_name in student["name"].lower()]

    if matches:
        print("\nMatching student record(s):")
        for student in matches:
            print(f"Name: {student['name']}, Roll No: {student['roll_no']}, "
                  f"Branch: {student['branch']}")
    else:
        print("Student not found.")

def delete_student():
    roll_no = input("Enter the roll number of the student to delete: ").strip()
    for student in students:
        if student["roll_no"].lower() == roll_no.lower():
            students.remove(student)
            print("Student record deleted successfully.")
            return
    print("No student found with that roll number.")

def main():
    while True:
        print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search student by name")
        print("4. Delete student by roll number")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Thank you for using the Student Record Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
