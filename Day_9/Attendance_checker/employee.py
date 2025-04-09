from datetime import date, timedelta

employees = []  # List to store employee data
emp_id_counter = 1000  # Starting Employee ID


def add_employee(name):
   
    today = date.today()
    
    attendance = {str(today - timedelta(days=i)): "a" for i in range(7)}

    employee = {"ID": emp_id_counter, "Name": name, "Attendance": attendance}
    employees.append(employee)
    
    print(f"Employee Added! ID: {emp_id_counter}")
    emp_id_counter += 1


def view_employees():
    if not employees:
        print("No employees found.")
        return
    for emp in employees:
        print(f"ID: {emp['ID']} | Name: {emp['Name']}")


def mark_attendance(emp_id):
    for emp in employees:
        if emp["ID"] == emp_id:
            for date_key in emp["Attendance"]:
                status = input(f"Enter attendance for {date_key} (p/a): ").strip().lower()
                emp["Attendance"][date_key] = "p" if status == "p" else "a"
            print("Attendance updated!")
            return
    print("Employee Not Found!")


def view_attendance(emp_id):
    for emp in employees:
        if emp["ID"] == emp_id:
            print(f"Attendance for {emp['Name']}:")
            for date_key, status in emp["Attendance"].items():
                print(f"{date_key}: {'Present' if status == 'p' else 'Absent'}")
            return
    print("Employee Not Found!")


def check_absent(emp):
    records = list(emp["Attendance"].values())
    max_streak = 0
    current_streak = 0

    for day in records:
        if day == "a":
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0

    return max_streak > 3



def attendance_report():
    if not employees:
        print("No employees to report.")
        return

    print("\nAttendance Report:")
    for emp in employees:
        status = "Needs Attention" if check_absent(emp) else "Good Attendance"
        print(f"ID: {emp['ID']} | Name: {emp['Name']} | Status: {status}")


def delete_employee(emp_id):
    global employees
    found = False
    employees = [emp for emp in employees if not (found := emp["ID"] == emp_id)]
    if found:
        print("Employee deleted successfully!")
    else:
        print("Employee not found.")
