# Variables, Statements, and Expression : A Learning task 

## 2.1 Introduction

In Python, variables, statements, and expressions form the foundation of programming. Understanding these concepts is crucial for writing efficient and readable code.

- Variables store data and can be reassigned dynamically.
- Expressions combine values and operators to produce new values.
- Statements are instructions that perform actions, such as assigning values or printing output.

## 2.1.1. Learning Goals

- **Understand the basics of variables, expressions, and statements in Python.**  
  Gain a foundational understanding of how variables store values, how expressions combine values and operators, and how statements execute actions in Python.

- **Differentiate between data types and apply type conversions.**  
  Recognize different data types such as integers, floats, strings, and booleans. Learn how to convert between types using built-in functions like `int()`, `float()`, `str()`, and `bool()`.

- **Properly name variables following Python conventions.**  
  Follow best practices for naming variables, including using descriptive names, adhering to snake_case, and avoiding reserved keywords.

- **Grasp the flow of execution through function calls and expressions.**  
  Understand how Python executes code sequentially, how function calls alter the flow of execution, and how expressions are evaluated.

- **Update and reassign variables effectively.**  
  Learn how to modify variable values by reassignment and understand how operations like `+=`, `-=`, `*=`, and `/=` update variables dynamically.

## 2.1.2. Objectives

- **Identify values and their data types.**  
  Recognize and distinguish between different types of values, such as integers, floats, strings, and booleans.

- **Perform operations using different operators.**  
  Apply arithmetic, comparison, logical, and assignment operators to manipulate data effectively.

- **Understand function calls and their role in expressions.**  
  Learn how function calls work, their syntax, and how they contribute to evaluating expressions in Python.

- **Explore Python's order of operations.**  
  Study the precedence and associativity rules that determine how expressions are evaluated in Python.

- **Practice variable reassignment and updating.**  
  Modify and update variable values dynamically using different assignment operations.

## 2.2. Values and Data Types

### 1 Research:

- **What is a value in Python?**  
  A value in Python is a fundamental unit of data that a program manipulates. It can be a number, text, or other data types.

- **Identify different data types in Python:**  
  Python has various data types, including:
  - **Integers (`int`)** – Whole numbers (e.g., `10`, `-5`).
  - **Floats (`float`)** – Decimal numbers (e.g., `3.14`, `-0.001`).
  - **Strings (`str`)** – Text enclosed in quotes (e.g., `'hello'`, `"Python"`).
  - **Booleans (`bool`)** – Represents `True` or `False` values.

### 2. Fun Fact:

- **Python is dynamically typed** – You don’t need to declare the type of a variable when you create one. The type is assigned at runtime based on the value stored.  

## 2.3. Operators and Operand

## 1. Research:

Operators in Python are symbols that perform operations on variables and values. The key types include:

## **Arithmetic Operators**  
Arithmetic operators perform basic mathematical operations on numbers. These include:
-  (Addition) – Adds two numbers.
-  (Subtraction) – Subtracts the right operand from the left.
-  (Multiplication) – Multiplies two numbers.
-  (Division) – Divides the left operand by the right, returning a float.

## **Comparison Operators**  
Comparison operators compare values and return a boolean (`True` or `False`). These include:
- (Equal) – Checks if two values are equal.
- (Not Equal) – Checks if two values are not equal.
- (Greater Than) – Checks if the left operand is greater than the right.
- (Less Than) – Checks if the left operand is smaller than the right.
- (Greater Than or Equal) – Checks if the left operand is greater than or equal to the right.
- (Less Than or Equal) – Checks if the left operand is less than or equal to the right.

## **Logical Operators**  
Logical operators are used to combine boolean expressions:
- `and` – Returns `True` if both conditions are `True`.
- `or` – Returns `True` if at least one condition is `True`.
- `not` – Returns the opposite boolean value.

## 2. Fun Fact:

- Python uses `//` for **floor division**, ensuring the result is always an integer.  
  Unlike regular division (`/`), which returns a float, **floor division rounds down** to the nearest whole number.  
  This makes it useful for calculations where only whole numbers are needed.

# 2.4.2. Functions are Objects; Parentheses Invoke Functions

## 1. Research:

In Python, **functions are first-class objects**, meaning they can be:
- Assigned to variables
- Passed as arguments to other functions
- Stored in data structures (e.g., lists, dictionaries)
- Returned from other functions

However, there is a key distinction:
- Writing `function_name` refers to the function object itself.
- Writing `function_name()` calls (or invokes) the function.

# 2.5. Data Types

## 1. Research:

### Python’s Dynamic Typing:
Python is **dynamically typed**, meaning:
- You don’t need to declare the data type of a variable.
- A variable’s type is determined at runtime based on its assigned value.
- The same variable can hold values of different types at different times.
# 2.6. Type Conversion Functions

## 1. Fun Fact:
- Python provides built-in functions to convert between different data types.
- Some common conversion functions:
  - `int()` → Converts to an integer.
  - `float()` → Converts to a floating-point number.
  - `str()` → Converts to a string.
  - `bool()` → Converts to a boolean (`True` or `False`).
  
# 2.7. Variables

## 1. Research:

### How Python Stores Variables in Memory:
- In Python, **variables are references** to objects in memory.
- When you assign a value to a variable, Python creates an object and stores it in memory.
- Variables act as **labels** pointing to memory locations.
- Python uses **garbage collection** to manage memory and remove unused objects.

# 2.10. Statements and Expressions

## 1. Research:

### Difference Between Statements and Expressions:
- **Expression**: A piece of code that produces a value.
  - Example: `5 + 3`
- **Statement**: A complete line of code that performs an action.
  - Example: `x = 5 + 3` (assignment statement)

## 2.11. Order of Operations

## 1. Fun Fact:

- Python follows **PEMDAS** rules for evaluating mathematical expressions:
  - **P** → Parentheses
  - **E** → Exponents
  - **MD** → Multiplication and Division (left to right)
  - **AS** → Addition and Subtraction (left to right)

# 2.12. Reassignment

## 2.12.1. Developing Your Mental Model of How Python Evaluates

### Understanding Reassignment:

- **Reassignment** means updating a variable's value after its initial assignment.
- The new value replaces the old value in memory.

# 2.13. Updating Variables

## Understanding Variable Updates:
- Variables can be updated using shorthand operators like `+=` and `-=`.
- These operators modify the existing value of a variable.

## 1. Exercise:

- Increment and decrement variables using `+=` and `-=`.

