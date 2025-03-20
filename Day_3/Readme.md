# Investigate Circular Imports
A circular import happens when two Python files depend on each other, causing an infinite loop where Python doesn’t know which file to load first.

## Solution: Function-Level Import (Lazy Importing)
Instead of importing the module at the top, import it inside a function where it is actually needed.

---

# Dynamic Module Loading
Dynamic module loading means importing a module at runtime instead of writing a fixed import statement in the code. This allows a program to load and use modules flexibly based on user input, configuration files, or specific conditions.

---

# Custom Module with Exception Handling
- Define a function `divide(a, b)`.
- If `b = 0`, catch the `ZeroDivisionError` and return "Cannot divide by zero."
- If any other error occurs (e.g., invalid inputs like text instead of numbers), catch the general exception and return "Error: <error_message>".

---

# Advanced Import Strategies
Advanced import strategies help in dynamically loading modules, handling missing functions, and improving code organization.

---

# Module Creation and Distribution
1. Create a package folder and module files (`math_operations.py`).
2. Add `__init__.py` to make it a package.
3. Write `setup.py` for installation.
4. Install locally using `pip install .`.
5. Import and test the package.

---

# Investigate sys.path
- `sys.path.append()` - Temporary, valid for the current session.
- Modify `PYTHONPATH` - Permanent solution for custom imports (add the path to `PYTHONPATH` in your system’s environment variables).
- Check `sys.path` - Debug import issues.

---

# Mocking Modules for Testing
Mocking is a technique used in testing to replace real dependencies with fake ones. This helps isolate the function being tested and control its behavior.

---

# Import Side Effects
Import side effects occur when a module automatically executes code as soon as it is imported, rather than just defining functions, classes, or variables. This can be useful for setting up configurations, logging, or initializing resources but can also cause unexpected behavior.

## Examples:
### Logging & Configuration
```python
import logging
print("Setting up logging...")
logging.basicConfig(level=logging.DEBUG)
```

### Database Connections or Setup
```python
import sqlite3
print("Connecting to database...")
conn = sqlite3.connect("my_database.db")
```

### Preventing Automatic Execution
```python
def greet():
    return "Hello from my_module!"

if __name__ == "__main__":
    print("This runs only when executed directly!")
```

---

# Investigate Python’s Import Caching
When you import a module in Python, it is cached in `sys.modules` to avoid redundant imports and improve performance. This means that subsequent imports of the same module do not reload it—Python just reuses the cached version.

## How to Reload a Module
```python
import importlib
import mymodule
importlib.reload(mymodule)
```

## Inspect All Loaded Modules
```python
import sys
print(sys.modules.keys())
```
