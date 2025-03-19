# 1. Investigate Circular Imports
# Fix the circular import problem between module_a.py and module_b.py.
def func_a():
    return "Function A"

def call_func_b():
    from module_b import func_b  # Import inside function
    return func_b()

print(call_func_b())


# 2. Dynamic Module Loading
# Write a program that dynamically imports and executes a function from any module specified by the user.

import importlib

# Get user input
module_name = input("Enter module name: ")  
function_name = input("Enter function name: ") 
argument = float(input("Enter argument: ")) 

try:
 
    module = importlib.import_module(module_name)

    func = getattr(module, function_name)
    
    # Execute function and print result
    result = func(argument)
    print("Output:", result)

except ModuleNotFoundError:
    print("Error: Module not found!")
except AttributeError:
    print("Error: Function not found in module!")
except Exception as e:
    print("Error:", e)

# 3. Custom Module with Exception Handling

