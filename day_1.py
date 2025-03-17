#Exercise 1
x = 42        # Integer
y = 3.14      # Float
z = 'Hello'   # String
a = True      # Boolean


print(type(x))
print(type(y))
print(type(z))
print(type(a))

#exercise 2
# Arithmetic Operations
a = 15
b = 4
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Comparison Operations
x = 10
y = 20
print("Equal:", x == y)
print("Not Equal:", x != y)

# Logical Operations
p = True
q = False
print("AND Operation:", p and q)
print("OR Operation:", p or q)
print("NOT Operation:", not p)


# 2. Function Calls in Expressions:


# Arithmetic expressions

def multiply(a, b):
    return a * b

print(multiply(4, 3) + 2)  

# Comparison expressions

def double(n):
    return n * 2

print(double(5) > 8)  



# 3. Fun Fact:

def greet():
    return "Hello!"

say_hello = greet
print(say_hello())  

# Passed as arguments to other functions

def execute(func):
    return func()

print(execute(greet)) 

#Exercise 3

# List of numbers
numbers = [5, 3, 8, 1]
result = max(numbers) - min(numbers)
print(result)

#Exercise 4
# Defining a function
def say_hello():
    return "Hello, World!"

greet = say_hello
print(greet())


# Python program demonstrating different data types

# Creating variables of different types
a = 10        # Integer
b = 'Python'  # String
c = 3.14      # Float
d = True      # Boolean
e = [1, 2, 3] # List
f = (4, 5, 6) # Tuple
g = {7, 8, 9} # Set
h = {'name': 'Alice', 'age': 25} # Dictionary

# Printing the type of each variable
print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h))

#Exercise 5
# Python program demonstrating type conversion

# Defining a string containing a number
num = '123'

# Converting string to integer
converted_num = int(num)

# Printing the converted value and its type
print(converted_num, type(converted_num))

# Additional conversions
float_num = float(num)  # Convert to float
string_num = str(converted_num)  # Convert back to string

print(float_num, type(float_num))
print(string_num, type(string_num))

#exercise 6
# Assigning values to variables
x = 10
y = "Python"
z = 3.14

# Printing initial values
print("Initial values:", x, y, z)

# Reassigning variables
x = 20
y = "Programming"
z = 6.28

# Printing updated values
print("Updated values:", x, y, z)

#Exercise 7

import keyword

# Printing all Python reserved keywords
print("Python Reserved Keywords:")
print(keyword.kwlist)

# Attempting to use a reserved keyword as a variable name (This will cause an error)
# if = 10  # Uncommenting this line will raise a SyntaxError

# Correct variable naming
valid_variable = 10
print("Valid variable:", valid_variable)

# Unclear variable names
x = 100  # Represents total price
y = 0.18  # Represents tax rate
z = x * y  # Represents tax amount

print("Total Price:", x)
print("Tax Rate:", y)
print("Tax Amount:", z)

# Improved variable names
total_price = 100
tax_rate = 0.18
tax_amount = total_price * tax_rate

print("Total Price:", total_price)
print("Tax Rate:", tax_rate)
print("Tax Amount:", tax_amount)

#Exercise 8
# Expression: 5 + 3 
x = 5 + 3  # Statement: Assignment

# Statement: Function call
print("The value of x is:", x)

#Exercise 9
# Expression following PEMDAS rule
result = (10 + 5) * 2 - 3 ** 2 / 3

# Printing the result
print("Result of the expression:", result)

#Exercise 10
# Initial assignment
value = 50
print("Initial value:", value)

# Reassigning the variable
value = value + 25
print("Updated value:", value)

# Further reassignment
value = value * 2
print("Final value:", value)

#Exercise 11
# Initial value assignment
balance = 500
print("Initial balance:", balance)

# Adding a deposit
balance += 200
print("After depositing 200:", balance)

# Subtracting a withdrawal
balance -= 150
print("After withdrawing 150:", balance)
