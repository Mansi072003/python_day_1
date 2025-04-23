# Create a function welcome() that prints "Welcome to Python!" and call it three times.

def welcome():
  for i in range(3):
     print("Welcome to Python!")
    
welcome()


# Write a function square(n) that takes a number n and returns its square.

def square(n):
   print(n*n)
square(4)


# Write a function is_even(num) that returns True if a number is even, else False.

def is_even(num):
    if num % 2 == 0:
        print(True)
    else:
        print(False)

is_even(4)
    

# Define a function full_name(first, last) that returns the full name as a string.

def full_name(first,last):
   return first + " " + last

# Create a function circle_area(radius) that returns the area of a circle using πr². Use pi = 3.14.

def circle_area(radius):
    pi = 3.14
    return pi * radius * radius
