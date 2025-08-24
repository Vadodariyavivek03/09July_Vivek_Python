students = {}

def add_stud():
    name = input("Enter student name : ")
    grade = float(input("Enter student grade (0-100) : "))
    students[name] = grade
    print(f"\n'{name}' added successfully!!\n")

# ----------------------------------------------------------------------- #

def display_stud():
    if not students:
        print("No students in the system yet.\n")
    else:
        print("\n--- Student Grades ---")
        for name, grade in students.items():
            print(f"\n{name} : {grade}")
        print()

# ----------------------------------------------------------------------- #

def calculate_avg():
    if not students:
        print("No grades to calculate average.\n")
    else:
        avg = sum(students.values()) / len(students)
        print(f"\nClass Average : {avg:.2f}\n")

# ----------------------------------------------------------------------- #

def check_pass_fail():
    name = input("Enter student name : ")
    if name in students:
        grade = students[name]
        if grade >= 45:
            print(f"\n{name} PASSED with {grade}\n")
        else:
            print(f"\n{name} FAILED with {grade}\n")
    else:
        print("Student not found.\n")

# ----------------------------------------------------------------------- #

while True:
    print("\n===== Grade Management System ===== \n")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Calculate Average Grade")
    print("4. Check Pass/Fail")
    print("5. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        add_stud()
    elif choice == "2":
        display_stud()
    elif choice == "3":
        calculate_avg()
    elif choice == "4":
        check_pass_fail()
    elif choice == "5":
        print("Thank You... Goodbye!")
        break
    else:
        print("Error: Invalid choice.... Try again!!\n")

# ----------------------------------------------------------------------- #
