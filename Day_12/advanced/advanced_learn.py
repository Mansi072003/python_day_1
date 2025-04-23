
# advanced 


# Log File Analyzer

input_file = 'server.log'
output_file = 'errors_only.log'

with open(input_file, 'r') as file:
    error_lines = [line for line in file if "ERROR" in line]

with open(output_file, 'w') as file:
    file.writelines(error_lines)

print(f"error occurrences: {len(error_lines)}")


# Word Frequency Counter
with open("story.txt", "r") as f:
    text = f.read()


words = text.lower().split()

freq = {}
for word in words:
    word = word.strip(".,!?") 
    freq[word] = freq.get(word, 0) + 1 


with open("frequency.txt", "w") as f:
    for word in freq:
        f.write(word + ": " + str(freq[word]) + "\n")

print("Done! Word frequencies are saved in frequency.txt.")


# CSV Reader + Filter
import csv

with open("sales.csv", "r") as infile, open("high_sales.csv", "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)  # Read header
    writer.writerow(header)  # Write header to output
    print("Sales above ₹10,000:")

    for row in reader:
        amount = int(row[2])
        if amount > 10000:
            print(row)
            writer.writerow(row)

print("Filtered sales saved to high_sales.csv")


# Merge Multiple Files

files = ["chapter1.txt", "chapter2.txt", "chapter3.txt"]

# Open the output file in write mode
with open("full_book.txt", "w") as outfile:
    for file_name in files:
        with open(file_name, "r") as infile:
            content = infile.read()
            outfile.write(content + "\n")  

print("All chapters merged into full_book.txt")



# Directory File Scanner
import os
counttxt =0
countcsv =0
folder_path = "C:/Users/LENOVO/OneDrive/Documents/GitHub/python_day_1/Day_12/advanced"
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        counttxt +=1
    elif filename.endswith('.csv'):
        countcsv +=1
print(f"Number of .txt files: {counttxt}\nNumber of .csv files: {countcsv}")

# bonus
# Auto Backup System
import datetime
import os


date = datetime.datetime.now().strftime("%Y-%m-%d")


os.makedirs("backup", exist_ok=True)


src = "data.csv"
dest = f"backup/data_backup_{date}.csv"


with open(src, "r") as f1, open(dest, "w") as f2:
    f2.write(f1.read())

print("Backup completed:", dest)


#  2. Text Formatter


with open("raw_text.txt", "r") as infile:
    lines = infile.readlines()

with open("raw_text.txt", "w") as outfile:
    for line in lines:
        cleaned = line.strip().replace("\t", "    ")  
        outfile.write(cleaned + "\n")

print("Text formatted successfully.")


# Chat History Logger

import datetime

print(" Type 'exit' to end the chat.\n")

with open("chat_log.txt", "a") as log:
    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            print("Chat ended. ✅ Messages saved to chat_log.txt")
            break
      
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] You: {msg}\n")

