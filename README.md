# Student Grading System

## Objective
This program is designed to manage student records and calculate grades. It allows users to add, update, view, and delete records efficiently.

## Features
- Add student records with grades for multiple subjects.
- View student records with calculated averages and letter grades.
- Update or delete specific student records.
- Sort records by student name or average grade.
- Automatically save and load records from a file.

## How to Run
### Prerequisites
- Python 3.6 or higher must be installed on your system.

### Steps
1. Clone or download the project files to your computer.
2. Open a terminal and navigate to the project folder.
3. Run the program:
   ```bash
   python student_grading_system.py

## Menu Options
1. Add New Student: Input a student’s name and grades.
2. View All Student Grades: Display all records with sorting options.
3. Update Student Grades: Modify the grades of an existing student.
4. Delete Student Record: Remove a specific student from the records.
5. Delete Save File: Remove all stored data and reset the program.
6. Save and Exit: Save changes and exit the program.

## Components
### Key Concepts
- File Management: Stores data in a CSV file and retrieves it on program start.
- Error Handling: Manages invalid inputs and missing files.
- Data Structures: Uses dictionaries to organize student records.
- Sorting: Allows sorting by name or calculated averages.

## Limitations
- The program uses a text-based interface.
- Subject names cannot be edited after setup.
- Data is not encrypted.


## Future Improvements
- Add a graphical interface for easier use.
- Include functionality to edit subject names.
- Develop reporting tools for exporting data.
- Implement a login system for managing access.



