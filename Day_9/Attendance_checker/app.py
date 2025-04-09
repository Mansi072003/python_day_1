from employee import add_employee, view_employees, mark_attendance, view_attendance, delete_employee,attendance_report

while True:
    print("\nEmployee Attendance System")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Mark Attendance")
    print("4. View Attendance")
    print("5. Delete Employee")
    print("6. Attendance Report")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter employee name: ")
        add_employee(name)

    elif choice == "2":
        view_employees()

    elif choice == "3":
        try:
            emp_id = int(input("Enter Employee ID: "))
            mark_attendance(emp_id)
        except ValueError:
            print("Invalid ID! Enter a number.")

    elif choice == "4":
        try:
            emp_id = int(input("Enter Employee ID: "))
            view_attendance(emp_id)
        except ValueError:
            print("Invalid ID! Enter a number.")

    elif choice == "5":
        try:
            emp_id = int(input("Enter Employee ID: "))
            delete_employee(emp_id)
        except ValueError:
            print("Invalid ID! Enter a number.")
    
    elif choice == "6":
        attendance_report()

    elif choice == "7":
        print("Exiting... Have a great day!")
        break

    else:
        print("Invalid choice! Enter a number between 1-6.")
