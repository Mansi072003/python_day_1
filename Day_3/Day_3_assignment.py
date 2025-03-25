# 1. Investigate Circular Imports
# Fix the circular import problem between module_a.py and module_b.py.
# module_a.py

def func_a():
    return "Function A"

def call_func_b():
    from module_b import func_b  # Import inside function
    return func_b()

# module_b.py
def func_b():
    return "Function B"

print(call_func_b())

#  2. Dynamic Module Loading
# Write a program that dynamically imports and executes a function from any module specified by the user.

# Get user input
module_name = input("Enter module name: ")  # Example: math
function_name = input("Enter function name: ")  # Example: sqrt
argument = input("Enter argument: ")  # Example: 25

# Dynamically import the module
try:
    module = importlib.import_module(module_name)  # Import the module
    func = getattr(module, function_name)  # Get the function
    result = func(float(argument))  # Convert argument to float and execute
    print("Output:", result)
except (ModuleNotFoundError, AttributeError, ValueError) as e:
    print("Error:", e)

# 3. Custom Module with Exception Handling
# Create a custom module calculator.py that handles division by zero and invalid inputs gracefully.

# calculator.py
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return f"Error: {e}"
# main.py
import calculator

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

   
    result = calculator.divide(num1, num2)
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter numbers.")

# 4. Advanced Import Strategies
import importlib

# Module and function to check
module_name = "math"
function_name = "sqrt"

try:
    # Dynamically import the module
    module = importlib.import_module(module_name)

    # Check if the function exists in the module
    if hasattr(module, function_name):
        func = getattr(module, function_name)
        result = func(16) 
        print(f"Result: {result}")
    else:
        print(f"Function '{function_name}' not found in module '{module_name}'.")
except ImportError:
    print(f"Module '{module_name}' could not be imported.")

# 5. Optimize Import Time
# Single import 

import time

start = time.time()
import math  # Import only the required module
end = time.time()

print(f"Single import time: {end - start:.6f} seconds")


# Import Everything (from module import *)

import time

start = time.time()
from math import *  # Importing all functions from the module
end = time.time()

print(f"Wildcard import time: {end - start:.6f} seconds")

# 6. Module Creation and Distribution
# Create a Python package structure with __init__.py.
# Write a setup.py to make it installable.
# Install your package locally.
# Import and test your package.


# 7. Investigate sys.path
# Explore sys.path and add a custom directory to import modules from an unconventional path.
# this question solution has been added in the calculator.py file

# 9. Import Side Effects
# created module.py
import my_module

# 10. Investigate Python’s Import Caching
# using module.py file only
import sys
# Check if the module is cached
print(sys.modules['my_module'])