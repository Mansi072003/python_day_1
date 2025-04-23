# 3. Custom Module with Exception Handling

# here defining calculator.py

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return f"Error: {e}"


import sys
print(sys.path)

sys.path.append('C:\Users\LENOVO\OneDrive\Documents\GitHub\python_day_1\Day_3\calculator.py') 
import calculator

print("Multiplication:", calculator.multiply(10, 5))