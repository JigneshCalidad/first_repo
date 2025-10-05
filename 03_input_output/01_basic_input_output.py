"""
💬 INPUT/OUTPUT - Basic Input and Output
=======================================

Input/Output (I/O) is how your program communicates with the user.
- Input: Getting data from the user
- Output: Displaying data to the user

Let's learn how to make interactive programs! 🎯
"""

print("=== BASIC OUTPUT ===")

# print() function - displays text
print("Hello, World!")
print("Welcome to Python programming!")

# Print multiple items
name = "Alice"
age = 25
print("Name:", name, "Age:", age)

# Print with formatting
print(f"Hello, {name}! You are {age} years old.")

# Print on same line (end parameter)
print("Loading", end="...")
print("Complete!")

# Print with separator
print("Python", "is", "awesome", sep="-")

print("\n=== BASIC INPUT ===")

# input() function - gets text from user
# Note: input() always returns a string!
print("Let's get some user input:")

# Simple input
user_name = input("What's your name? ")
print(f"Nice to meet you, {user_name}!")

# Input with prompt
age_input = input("How old are you? ")
print(f"You entered: {age_input} (type: {type(age_input)})")

# Convert input to number
age_number = int(age_input)
print(f"Your age as number: {age_number} (type: {type(age_number)})")

print("\n=== INPUT VALIDATION ===")

# Safe input conversion with error handling
def get_number(prompt):
    """Safely get a number from user"""
    while True:
        try:
            value = input(prompt)
            return int(value)
        except ValueError:
            print("Please enter a valid number!")

# Example usage
user_age = get_number("Enter your age: ")
print(f"Your age is: {user_age}")

print("\n=== MULTIPLE INPUTS ===")

# Getting multiple values
print("Let's get your personal information:")
first_name = input("First name: ")
last_name = input("Last name: ")
email = input("Email: ")

print(f"\nYour information:")
print(f"Name: {first_name} {last_name}")
print(f"Email: {email}")

# Input with default values
def get_input_with_default(prompt, default=""):
    """Get input with optional default value"""
    user_input = input(f"{prompt} (default: {default}): ")
    return user_input if user_input else default

city = get_input_with_default("Enter your city", "New York")
print(f"City: {city}")

print("\n=== FORMATTED OUTPUT ===")

# Different ways to format output
name = "Python"
version = 3.9
rating = 4.8

# Method 1: f-strings (recommended)
print(f"Language: {name}, Version: {version}, Rating: {rating}")

# Method 2: .format() method
print("Language: {}, Version: {}, Rating: {}".format(name, version, rating))

# Method 3: % formatting
print("Language: %s, Version: %.1f, Rating: %.1f" % (name, version, rating))

# Formatting numbers
price = 19.99
print(f"Price: ${price:.2f}")  # 2 decimal places
print(f"Price: ${price:>8.2f}")  # Right-aligned, 8 characters wide

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Simple calculator
def simple_calculator():
    """Basic calculator"""
    print("=== Simple Calculator ===")
    
    try:
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero!")
                return
        else:
            print("Invalid operation!")
            return
            
        print(f"Result: {num1} {operation} {num2} = {result}")
        
    except ValueError:
        print("Please enter valid numbers!")

# Uncomment to run calculator
# simple_calculator()

# Example 2: User registration
def user_registration():
    """Simple user registration"""
    print("=== User Registration ===")
    
    username = input("Choose a username: ")
    
    # Check if username is valid
    if len(username) < 3:
        print("Username must be at least 3 characters long!")
        return
    
    password = input("Choose a password: ")
    
    # Check password strength
    if len(password) < 6:
        print("Password must be at least 6 characters long!")
        return
    
    confirm_password = input("Confirm password: ")
    
    if password != confirm_password:
        print("Passwords don't match!")
        return
    
    print(f"Registration successful!")
    print(f"Username: {username}")
    print(f"Password: {'*' * len(password)}")

# Uncomment to run registration
# user_registration()

# Example 3: Quiz program
def simple_quiz():
    """Simple quiz with questions"""
    print("=== Python Quiz ===")
    
    questions = [
        ("What is the capital of France?", "Paris"),
        ("What is 2 + 2?", "4"),
        ("What is the largest planet?", "Jupiter")
    ]
    
    score = 0
    total = len(questions)
    
    for i, (question, answer) in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question}")
        user_answer = input("Your answer: ")
        
        if user_answer.lower() == answer.lower():
            print("Correct! ✅")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer} ❌")
    
    print(f"\nQuiz completed!")
    print(f"Your score: {score}/{total}")
    print(f"Percentage: {(score/total)*100:.1f}%")

# Uncomment to run quiz
# simple_quiz()

print("\n=== INPUT/OUTPUT TIPS ===")

print("""
Tips for Input/Output:
1. Always validate user input
2. Use try/except for error handling
3. Provide clear prompts to users
4. Use f-strings for formatting (modern way)
5. Convert input to appropriate types
6. Handle edge cases (empty input, invalid data)
7. Make your programs user-friendly
8. Test with different inputs
""")

# Example of input validation
def get_positive_number(prompt):
    """Get a positive number from user"""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number!")
        except ValueError:
            print("Please enter a valid number!")

# Test the function
print("\nTesting input validation:")
# number = get_positive_number("Enter a positive number: ")
# print(f"You entered: {number}")

"""
Key Points to Remember:
1. print() displays output to the user
2. input() gets text input from the user
3. input() always returns a string
4. Convert input to numbers with int() or float()
5. Use try/except for error handling
6. Validate user input before using it
7. Use f-strings for formatting (f"Hello {name}")
8. Make your programs interactive and user-friendly
9. Always handle edge cases and errors
10. Test your programs with different inputs
"""
