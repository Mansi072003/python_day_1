# For Loop Basics: Write a for loop to print numbers from 1 to 10.

for i in range(10):
 print(i)


#  String Iteration: Write a program that counts vowels in a string.

vowels = "aeiouAEIOU" 
count = 0 

string = input("Enter a string: ") 

for char in string: 
    if char in vowels: 
        count += 1 

print(count)


# Accumulator Pattern: Calculate the sum of squares from 1 to 100.

sum_squares = 0  

for i in range(1, 101): 
    sum_squares += i ** 2 

print("Sum of squares from 1 to 100:", sum_of_squares)

# Nested Loops: Create a multiplication table up to 10x10.

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:3}", end=" ") 
    print()  



