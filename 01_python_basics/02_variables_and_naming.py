"""
🐍 PYTHON BASICS - Variables and Naming Conventions
===================================================

Variables are like labeled boxes that store information.
Think of them as sticky notes with names that help you remember what's inside!
"""

# ✅ GOOD variable names (descriptive and clear)
student_name = "Alice"
student_age = 20
course_grade = 95.5
is_enrolled = True

# ❌ BAD variable names (avoid these!)
# a = "Alice"           # Too short, not descriptive
# studentName = "Alice" # Mixed case (not Python style)
# student-name = "Alice" # Hyphens not allowed
# 2name = "Alice"       # Can't start with numbers

# Python naming conventions:
# 1. Use snake_case for variables and functions
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

# 2. Use UPPER_CASE for constants (values that don't change)
PI = 3.14159
MAX_STUDENTS = 30
API_KEY = "your-secret-key"

# 3. Avoid using Python keywords as variable names
# Keywords are reserved words like: if, for, while, def, class, etc.
# You can check keywords with:
import keyword
print("Python keywords:", keyword.kwlist)

# Variable types and examples
print("=== Variable Examples ===")

# String (text)
message = "Hello, World!"
print(f"String: {message}")

# Integer (whole numbers)
count = 42
print(f"Integer: {count}")

# Float (decimal numbers)
price = 19.99
print(f"Float: {price}")

# Boolean (True or False)
is_active = True
is_completed = False
print(f"Boolean: {is_active}, {is_completed}")

# None (represents absence of value)
data = None
print(f"None: {data}")

# You can check the type of a variable
print(f"Type of message: {type(message)}")
print(f"Type of count: {type(count)}")
print(f"Type of price: {type(price)}")
print(f"Type of is_active: {type(is_active)}")

# Dynamic typing - Python variables can change type!
my_variable = 42
print(f"Initially: {my_variable} (type: {type(my_variable)})")

my_variable = "Now I'm a string!"
print(f"After change: {my_variable} (type: {type(my_variable)})")

my_variable = [1, 2, 3]  # Now it's a list!
print(f"Finally: {my_variable} (type: {type(my_variable)})")

"""
Variable Naming Rules:
1. Start with letter or underscore (_)
2. Can contain letters, numbers, and underscores
3. Case-sensitive (age ≠ Age)
4. Can't use Python keywords
5. Use descriptive names
6. Follow snake_case convention

Examples:
✅ Good: user_name, student_age, max_attempts
❌ Bad: n, a, x1, user-name, 2name, class
"""
