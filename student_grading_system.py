import os
import csv

# Utility Functions
def print_header(title):
    print("\n" + "=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

# File Management
def save_to_file(file_name, data, subjects):
    try:
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name"] + subjects)  # Save subjects as the first row
            for student, grades in data.items():
                writer.writerow([student] + list(grades))
        print("Data saved successfully!")
    except Exception as e:
        print(f"Error saving to file: {e}")

def load_from_file(file_name):
    try:
        if not os.path.exists(file_name):
            return {}, []  # Return empty records and subjects if file doesn't exist
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            lines = list(reader)
            subjects = lines[0][1:]  # First row contains subjects
            data = {row[0]: tuple(map(int, row[1:])) for row in lines[1:]}
            return data, subjects
    except Exception as e:
        print(f"Error loading file: {e}")
        return {}, []

def delete_file(file_name):
    try:
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"{file_name} deleted successfully!")
        else:
            print(f"Error: {file_name} does not exist.")
    except Exception as e:
        print(f"Error deleting file: {e}")

# Grade Calculation
def calculate_letter_grade(average):
    if average >= 95:
        return '1.00'
    elif average >= 90:
        return '1.50'
    elif average >= 85:
        return '2.00'
    elif average >= 80:
        return '2.50'
    elif average >= 75:
        return '3.00'
    else:
        return '5.00'

# Display Functions
def display_grades(student_records, subjects):
    if not student_records:
        print_header("No Student Records Found")
        return

    print_header("STUDENT GRADES")
    header = f"{'Student Name':<15} " + " ".join(f"{subj:<10}" for subj in subjects) + "Average   Grade"
    print(header)
    print("-" * (15 + 10 * len(subjects) + 20))
    for student, grades in student_records.items():
        average = sum(grades) / len(grades)
        letter_grade = calculate_letter_grade(average)
        grades_str = " ".join(f"{grade:<10}" for grade in grades)
        print(f"{student:<15} {grades_str} {average:<10.2f} {letter_grade}")

# Input Validation Functions
def validate_name(name):
    return all(char.isalpha() or char.isspace() for char in name)

def input_grades(subjects):
    grades = []
    for subject in subjects:
        while True:
            try:
                grade = int(input(f"Enter grade for {subject} (0-100): "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a numeric grade.")
    return tuple(grades)

# Main Program
def main():
    file_name = "student_records.csv"

    # Load existing student records and subjects
    student_records, subjects = load_from_file(file_name)

    # Initialize subjects if not loaded
    if not subjects:
        while True:
            try:
                num_subjects = int(input("Enter the number of subjects: "))
                if num_subjects > 0:
                    break
                else:
                    print("The number of subjects must be a positive number.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        subjects = []
        for i in range(num_subjects):
            while True:
                subject = input(f"Enter name for subject {i + 1}: ").strip()
                if subject and subject not in subjects:
                    subjects.append(subject)
                    break
                print("Invalid or duplicate subject name. Try again.")

    while True:
        print_header("STUDENT GRADING SYSTEM")
        print("1. Add New Student")
        print("2. View All Student Grades")
        print("3. Update Student Grades")
        print("4. Delete Student Record")
        print("5. Delete Save File")
        print("6. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ").strip()
            if not validate_name(name):
                print("Invalid name! Use only letters and spaces.")
            elif name in student_records:
                print("Student already exists!")
            else:
                print(f"Enter grades for {name}:")
                grades = input_grades(subjects)
                student_records[name] = grades
                print(f"{name} added successfully!")

        elif choice == "2":
            print("1. Sort by Name")
            print("2. Sort by Average Grade")
            sort_choice = input("Enter your choice: ")
            if sort_choice == "1":
                sorted_records = dict(sorted(student_records.items(), key=lambda x: x[0]))
                display_grades(sorted_records, subjects)
            elif sort_choice == "2":
                sorted_records = dict(sorted(student_records.items(), key=lambda x: sum(x[1]) / len(x[1]), reverse=True))
                display_grades(sorted_records, subjects)
            else:
                print("Invalid choice. Returning to Main Menu.")

        elif choice == "3":
            name = input("Enter the student name to update grades: ").strip()
            if name in student_records:
                print(f"Enter new grades for {name}:")
                grades = input_grades(subjects)
                student_records[name] = grades
                print(f"{name}'s grades updated successfully!")
            else:
                print("Student not found!")

        elif choice == "4":
            name = input("Enter the student name to delete: ").strip()
            if name in student_records:
                del student_records[name]
                print(f"{name} deleted successfully!")
            else:
                print("Student not found!")

        elif choice == "5":
            delete_confirmation = input(f"Are you sure you want to delete {file_name}? (yes/no): ").lower()
            if delete_confirmation == 'yes':
                delete_file(file_name)
                student_records.clear()
                print("All records have been deleted!")

        elif choice == "6":
            save_to_file(file_name, student_records, subjects)
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
