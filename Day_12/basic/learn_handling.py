import os


# Open and Read File
# Write a Python program to read a file notes.txt and print its contents line-by-line.
#  Concept tested: File opening, reading, and loop.

print("Contents of notes.txt:")
with open("notes.txt", "r") as file:
    for line in file:
        print(line, end='')


# Count Lines in a File
# Count how many lines exist in a file poem.txt.

with open("poem.txt", "r") as file:
    lines = file.readlines()
    print("\nNumber of lines in poem.txt:", len(lines))


# Write to a File
# Create a new file reminder.txt and write 5 tasks to it, one per line.

tasks = ["Wake up", "Do assignment", "Call friend", "Exercise", "Read book"]
with open("reminder.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")


# Append to a File
# Add a new task to reminder.txt without deleting existing ones.
with open("reminder.txt", "a") as file:
    file.write("Walk the dog\n")


# Check File Exists
# Use os.path.exists() to check if data.txt exists before opening.

if os.path.exists("data.txt"):
    with open("data.txt", "r") as file:
        print("\nContents of data.txt:")
        print(file.read())
else:
    print("\ndata.txt does not exist.")


# intermediate 

# Remove Blank Lines
# Write a program that reads input.txt and creates cleaned.txt with no empty lines.
with open("input.txt","r")as file, open("cleaned.txt","w")as file1:
    for line in file:
        if line.strip():
           file1.write(line)


# Find and Replace
# Search and replace the word “Python” with “PYTHON” in article.txt.
with open("article.txt", "r") as file:
    content = file.read()

up_content = content.replace("Python", "PYTHON")

with open("article.txt", "w") as file:
    file.write(up_content)



# Uppercase Writer
# Read a file and write its contents in all uppercase to output.txt.

with open("input.txt","r")as file,open("output.txt","w") as file1:
    for line in file:
        file1.write(line.upper())



# Student Report Generator
# Read students.txt containing Name,Marks, calculate and save the pass/fail status in report.txt (Pass if Marks ≥ 50).

with open("students.txt", "r") as file, open("report.txt", "w") as file1:
    for line in file:
        name, marks = line.strip().split(",")
        status = "Pass" if int(marks) >= 50 else "Fail"
        file1.write(f"{name},{marks} - {status}\n")


# Reverse File Lines
# Reverse the order of lines in quotes.txt and write to reversed_quotes.txt.

with open("quotes.txt","r")as file:
    lines=file.readlines()

with open("reversed_quotes.txt", "w") as file:
    for line in reversed(lines):
        file.write(line[::-1])
        print(line)

