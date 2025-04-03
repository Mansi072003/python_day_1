from datetime import date, timedelta

employees = []  # List to store employee data
emp_id_counter = 1000  # Starting Employee ID


def add_employee(name):
  
    global emp_id_counter
    today = date.today()
    
    # Default attendance for last 7 days
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
            for date in emp["Attendance"]:
                status = input(f"Enter attendance for {date} (p/a): ").strip().lower()
                emp["Attendance"][date] = "p" if status == "p" else "a"
            print("Attendance updated!")
            return
    print("Employee Not Found!")


def view_attendance(emp_id):

    for emp in employees:
        if emp["ID"] == emp_id:
            print(f"Attendance for {emp['Name']}:")
            for date, status in emp["Attendance"].items():
                print(f"{date}: {'Present' if status == 'p' else 'Absent'}")
            return
    print("Employee Not Found!")


def delete_employee(emp_id):
   
    global employees
    employees = [emp for emp in employees if emp["ID"] != emp_id]
    print("Employee deleted successfully!")
