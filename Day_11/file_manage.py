import csv

def process_students_data():
    try:
        
        with open('students.txt', 'r') as file:
            lines = file.readlines()

        student_data = []
        for line in lines:
            name, mark = line.strip().split(',')
            student_data.append((name, int(mark)))

       g total = 0
        for student in students:
            name, mark = student
            total += mark
        average = total / len(students)


        with open('top_students.txt', 'w') as top_file:
            for name, mark in student_data:
                if mark > average_marks:
                    top_file.write(f"{name}\n")

   
        with open('students.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Name', 'Marks'])  
            for name, mark in student_data:
                writer.writerow([name, mark])

        print("Processing complete. Output saved to 'top_students.txt' and 'students.csv'.")

    except FileNotFoundError:
        print("Error: 'students.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

process_students_data()


