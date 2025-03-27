# 1. Error Classification
# a) syntax error:here colon is missing
for i in range(5):
    print(i)

# b)Zero division error or runtime error ,to avoid this error use try except block 
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

#c)Logical error: Correcting formula for area
def calculate_area(radius):
    return 3.14 * radius * radius  

#2. Debugging the complex function
# to avoid the Value Error using try-except block 

def process_data(data):
    total = 0
    count = 0
    
    for item in data:
        try:
            total += int(item)  # Convert item to int
            count += 1  # Only count valid items
        except ValueError:
            print(f"Skip invalid data: {item}")  # Handle invalid data 

    if count == 0:  # Avoid division by zero
        return "Error: No valid numbers to process"

    return total / count 
print(process_data(['10', '20', 'abc', '30'])) 

# 3. Advanced Debugging Challenge
# ZeroDivisionError 
import random

def unreliable_function():
    try:
        number = random.choice([0, 1, 2])
        return 10 / number
    except ZeroDivisionError:
        return "Error: Division by zero occurred"

for i in range(10):
    print(unreliable_function())

# 4)This will raise a TypeError
# to avoid this using strip which remove  % symbol
def calculate_discount(price, discount):
    if isinstance(discount, str) and discount.endswith('%'):
        discount = float(discount.strip('%'))

    return price - (price * discount / 100)

print(calculate_discount(100, 10))     

# 5. Rubber Duck Debugging

# Step 1: Create a list of numbers
numbers = [1, 2, 3, 4, 5]  # This list contains the numbers we want to multiply together

# Step 2: Initialize a variable to store the product
result = 1  # We start with 1 because multiplying by 1 doesn't change the value

# Step 3: Loop through each number in the list
for num in numbers:  # 'num' will take each value from 'numbers' one by one
    result *= num  # Multiply 'result' by the current number and update 'result'
# Step 4: Print the final product
print("Product:", result)  # This prints the final result after multiplying all numbers

# 6. Advanced Challenge: Debug a Multi-threaded Program
#  Problem: Race Condition
#  using a threading.Lock ,lock ensures that only one thread at a time updates counter.

import threading

counter = 0
lock = threading.Lock()  # Create a lock

def increment():
    global counter
    for _ in range(100000) #this underscore bypass the value
        with lock:  # Lock the critical section
            counter += 1

# Create and start two threads
threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Counter:", counter)  

# 7. Activity: Debug with Breakpoints
# Problem: ZeroDivisionError
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed!"  # Handle the error gracefully
    result = a / b #Breakpoint here (but only if b ≠ 0)
    return result

a = 10
b = 0  # Still zero, but now handled safely
print(divide(a, b)) 

# 8. Memory Leaks and Performance Debugging
# Optimized Code (Using Generators)

# Instead of storing all values in a list, we can use a generator to yield values on demand, reducing memory usage.

# or
# we can also make list and can add to direct index 
import time

def inefficient_function():
    result = []
    for i in range(100000):
        result.append(i * 2)
    time.sleep(2)
    return result

print(len(inefficient_function()))

# 9. Unexpected None
# Problem: Function Returns None
# The function calculates the sum and stores it in result.However, it never returns result because there is no return statement.
def add(a, b):
    return a + b 

print(add(3, 4)) 


# 10. Silent Failures
#  Problem: Silent Failure in Exception Handling
# The except: catches all exceptions, including ZeroDivisionError, but the pass statement suppresses the error completely.
try:
    result = 10 / 0  # This will cause a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!") 
