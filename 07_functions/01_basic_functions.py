"""
🔧 FUNCTIONS - Basic Functions
=============================

Functions are reusable blocks of code that perform specific tasks.
They're like mini-programs within your program! 🛠️
"""

print("=== WHAT ARE FUNCTIONS? ===")

# Functions help you:
# 1. Organize code into logical chunks
# 2. Avoid repeating code (DRY principle)
# 3. Make code more readable and maintainable
# 4. Test individual parts of your program

print("Functions are like recipes - you write them once and use them many times!")

print("\n=== BASIC FUNCTION SYNTAX ===")

# Function definition
def greet():
    """Simple function that greets the user"""
    print("Hello, World!")
    print("Welcome to Python functions!")

# Function call
print("Calling greet() function:")
greet()

# Function with parameters
def greet_person(name):
    """Function that greets a specific person"""
    print(f"Hello, {name}!")
    print(f"Nice to meet you, {name}!")

# Call function with argument
print("\nCalling greet_person() function:")
greet_person("Alice")
greet_person("Bob")

# Function with multiple parameters
def introduce(name, age, city):
    """Function that introduces a person"""
    print(f"Hi! I'm {name}")
    print(f"I'm {age} years old")
    print(f"I live in {city}")

# Call function with multiple arguments
print("\nCalling introduce() function:")
introduce("Charlie", 25, "New York")

print("\n=== FUNCTIONS WITH RETURN VALUES ===")

# Function that returns a value
def add_numbers(a, b):
    """Add two numbers and return the result"""
    result = a + b
    return result

# Use the returned value
sum_result = add_numbers(5, 3)
print(f"5 + 3 = {sum_result}")

# Function that returns multiple values
def get_name_and_age():
    """Return name and age"""
    name = "David"
    age = 30
    return name, age

# Unpack multiple return values
person_name, person_age = get_name_and_age()
print(f"Name: {person_name}, Age: {person_age}")

# Function with conditional return
def get_grade(score):
    """Return grade based on score"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test grade function
scores = [95, 85, 75, 65, 55]
for score in scores:
    grade = get_grade(score)
    print(f"Score {score}: Grade {grade}")

print("\n=== FUNCTION PARAMETERS ===")

# Default parameters
def greet_with_default(name="World"):
    """Greet with default name"""
    print(f"Hello, {name}!")

# Call with and without arguments
greet_with_default()  # Uses default
greet_with_default("Python")  # Uses provided argument

# Multiple default parameters
def create_profile(name, age=18, city="Unknown"):
    """Create user profile with defaults"""
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

# Test different combinations
create_profile("Alice")
create_profile("Bob", 25)
create_profile("Charlie", 30, "Boston")

# Keyword arguments
def describe_pet(name, animal_type, age):
    """Describe a pet"""
    print(f"I have a {animal_type} named {name}")
    print(f"{name} is {age} years old")

# Use keyword arguments
describe_pet(name="Fluffy", animal_type="cat", age=3)
describe_pet(animal_type="dog", name="Buddy", age=5)

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Calculator functions
def calculator(operation, a, b):
    """Basic calculator function"""
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operation!"

# Test calculator
operations = ["+", "-", "*", "/"]
a, b = 10, 3

for op in operations:
    result = calculator(op, a, b)
    print(f"{a} {op} {b} = {result}")

# Example 2: String processing
def process_text(text, operation="count"):
    """Process text with different operations"""
    if operation == "count":
        return len(text)
    elif operation == "upper":
        return text.upper()
    elif operation == "lower":
        return text.lower()
    elif operation == "reverse":
        return text[::-1]
    else:
        return "Invalid operation!"

# Test text processing
text = "Hello, World!"
operations = ["count", "upper", "lower", "reverse"]

for op in operations:
    result = process_text(text, op)
    print(f"Text '{text}' - {op}: {result}")

# Example 3: Data validation
def validate_user_input(name, age, email):
    """Validate user input data"""
    errors = []
    
    # Validate name
    if not name or len(name) < 2:
        errors.append("Name must be at least 2 characters long")
    
    # Validate age
    if not isinstance(age, int) or age < 0:
        errors.append("Age must be a positive integer")
    
    # Validate email
    if not email or "@" not in email:
        errors.append("Email must contain @ symbol")
    
    if errors:
        return False, errors
    else:
        return True, "All data is valid!"

# Test validation
test_cases = [
    ("Alice", 25, "alice@example.com"),
    ("", 30, "bob@example.com"),
    ("Charlie", -5, "charlie@example.com"),
    ("David", 35, "invalid-email")
]

for name, age, email in test_cases:
    is_valid, message = validate_user_input(name, age, email)
    print(f"Name: {name}, Age: {age}, Email: {email}")
    print(f"Valid: {is_valid}, Message: {message}")
    print()

print("\n=== FUNCTION DOCUMENTATION ===")

# Docstrings - documentation for functions
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle
    
    Returns:
    float: The area of the rectangle
    """
    return length * width

# Access function documentation
print("Function documentation:")
print(calculate_area.__doc__)

# Test the function
area = calculate_area(5, 3)
print(f"Area of rectangle 5x3: {area}")

print("\n=== LOCAL VS GLOBAL VARIABLES ===")

# Global variable
global_var = "I'm global!"

def demonstrate_scope():
    """Demonstrate variable scope"""
    # Local variable
    local_var = "I'm local!"
    
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")
    
    # Modify global variable
    global global_var
    global_var = "Modified global!"

# Test scope
print(f"Before function - Global: {global_var}")
demonstrate_scope()
print(f"After function - Global: {global_var}")

print("\n=== FUNCTION BEST PRACTICES ===")

print("""
Function Best Practices:
1. Use descriptive function names
2. Write clear docstrings
3. Keep functions small and focused
4. Use meaningful parameter names
5. Return values instead of printing
6. Handle edge cases
7. Use default parameters wisely
8. Test your functions thoroughly
9. Avoid global variables when possible
10. Use type hints for clarity
""")

# Example of good function design
def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).
    
    Parameters:
    weight (float): Weight in kilograms
    height (float): Height in meters
    
    Returns:
    tuple: (bmi_value, category)
    """
    if weight <= 0 or height <= 0:
        return None, "Invalid input"
    
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return round(bmi, 1), category

# Test BMI calculator
test_cases = [
    (70, 1.75),  # Normal weight
    (50, 1.60),  # Underweight
    (90, 1.70),  # Overweight
    (0, 1.75),   # Invalid input
]

for weight, height in test_cases:
    bmi, category = calculate_bmi(weight, height)
    print(f"Weight: {weight}kg, Height: {height}m")
    print(f"BMI: {bmi}, Category: {category}")
    print()

"""
Key Points to Remember:
1. Functions are reusable blocks of code
2. Use def keyword to define functions
3. Functions can take parameters and return values
4. Use docstrings to document functions
5. Keep functions small and focused
6. Use meaningful names for functions and parameters
7. Test your functions with different inputs
8. Use default parameters for optional arguments
9. Return values instead of printing when possible
10. Practice with real-world examples
"""
