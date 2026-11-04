
# Day 2 Assignment - Student Grade Manager

students = []


# Calculate grade based on marks
def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


# Add student details
def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Error: Student name cannot be empty.")
        return

    while True:
        try:
            mark = float(input("Enter marks (0-100): "))

            if not 0 <= mark <= 100:
                print("Error: Marks must be between 0 and 100.")
                continue

            break

        except ValueError:
            print("Error: Please enter a valid number.")

    grade = calculate_grade(mark)

    student = {
        "name": name,
        "mark": mark,
        "grade": grade
    }

    students.append(student)

    print(f"\nStudent {name} added successfully!")


# Display student results
def show_results():
    if not students:
        print("\nNo student records available.")
        return

    print("\n========== STUDENT RESULTS ==========")

    print(f"{'Name':<20}{'Mark':<10}{'Grade':<10}")
    print("-" * 40)

    for student in students:
        print(
            f"{student['name']:<20}"
            f"{student['mark']:<10.2f}"
            f"{student['grade']:<10}"
        )

    print("-" * 40)

    marks = [student["mark"] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print(f"Class Average : {average:.2f}")
    print(f"Highest Mark  : {highest:.2f}")
    print(f"Lowest Mark   : {lowest:.2f}")


# Main menu
def main():
    while True:
        print("\n===== STUDENT GRADE MANAGER =====")
        print("1. Add Student")
        print("2. Show Results")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            show_results()

        elif choice == "3":
            print("\nThank you for using Student Grade Manager!")
            break

        else:
            print("Invalid choice! Please enter 1, 2 or 3.")


# Start the program
if __name__ == "__main__":
    main()
