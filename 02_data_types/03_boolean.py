"""
✅ DATA TYPES - Boolean (True/False)
===================================

Boolean values represent truth values: True or False
They're essential for making decisions in programming!

Think of booleans as light switches - they're either ON (True) or OFF (False).
"""

print("=== BOOLEAN BASICS ===")

# Boolean values
is_student = True
is_working = False
is_weekend = True

print(f"Is student: {is_student} (type: {type(is_student)})")
print(f"Is working: {is_working} (type: {type(is_working)})")
print(f"Is weekend: {is_weekend} (type: {type(is_weekend)})")

# Boolean conversion
print(f"\nBoolean conversion:")
print(f"bool(1): {bool(1)}")        # True
print(f"bool(0): {bool(0)}")        # False
print(f"bool(-1): {bool(-1)}")       # True (any non-zero number)
print(f"bool(0.0): {bool(0.0)}")     # False
print(f"bool('hello'): {bool('hello')}")  # True (non-empty string)
print(f"bool(''): {bool('')}")       # False (empty string)
print(f"bool([]): {bool([])}")       # False (empty list)
print(f"bool([1, 2]): {bool([1, 2])}")  # True (non-empty list)
print(f"bool(None): {bool(None)}")   # False

print("\n=== COMPARISON OPERATORS ===")

# These operators return boolean values
a = 10
b = 5
c = 10

print(f"a = {a}, b = {b}, c = {c}")
print(f"a == b: {a == b}")      # Equal to
print(f"a != b: {a != b}")      # Not equal to
print(f"a > b: {a > b}")        # Greater than
print(f"a < b: {a < b}")        # Less than
print(f"a >= c: {a >= c}")      # Greater than or equal
print(f"a <= c: {a <= c}")     # Less than or equal

# String comparisons
name1 = "Alice"
name2 = "Bob"
name3 = "Alice"

print(f"\nString comparisons:")
print(f"'{name1}' == '{name2}': {name1 == name2}")
print(f"'{name1}' == '{name3}': {name1 == name3}")
print(f"'{name1}' < '{name2}': {name1 < name2}")  # Alphabetical order

print("\n=== LOGICAL OPERATORS ===")

# AND operator (both must be True)
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(f"Age: {age}, Has license: {has_license}")
print(f"Can drive: {can_drive}")

# OR operator (at least one must be True)
is_weekend = True
is_holiday = False
can_rest = is_weekend or is_holiday
print(f"Is weekend: {is_weekend}, Is holiday: {is_holiday}")
print(f"Can rest: {can_rest}")

# NOT operator (reverses the boolean)
is_raining = True
is_sunny = not is_raining
print(f"Is raining: {is_raining}")
print(f"Is sunny: {is_sunny}")

# Complex logical expressions
score = 85
attendance = 90
is_passing = score >= 70 and attendance >= 80
print(f"Score: {score}, Attendance: {attendance}")
print(f"Is passing: {is_passing}")

print("\n=== TRUTH TABLES ===")

print("AND Truth Table:")
print("True  and True  =", True and True)
print("True  and False =", True and False)
print("False and True  =", False and True)
print("False and False =", False and False)

print("\nOR Truth Table:")
print("True  or True  =", True or True)
print("True  or False =", True or False)
print("False or True  =", False or True)
print("False or False =", False or False)

print("\nNOT Truth Table:")
print("not True  =", not True)
print("not False =", not False)

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Age verification
def can_vote(age, has_id):
    """Check if person can vote"""
    return age >= 18 and has_id

voter_age = 20
has_id = True
print(f"Age: {voter_age}, Has ID: {has_id}")
print(f"Can vote: {can_vote(voter_age, has_id)}")

# Example 2: Password validation
def is_valid_password(password):
    """Check if password meets requirements"""
    has_length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    return has_length and has_upper and has_lower and has_digit

password = "MyPassword123"
print(f"Password: '{password}'")
print(f"Is valid: {is_valid_password(password)}")

# Example 3: Weather conditions
def should_wear_jacket(temperature, is_raining, is_windy):
    """Decide if jacket is needed"""
    return temperature < 15 or is_raining or is_windy

temp = 12
raining = False
windy = True
print(f"Temperature: {temp}°C, Raining: {raining}, Windy: {windy}")
print(f"Should wear jacket: {should_wear_jacket(temp, raining, windy)}")

# Example 4: Grade classification
def get_grade(score):
    """Get letter grade based on score"""
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

scores = [95, 85, 75, 65, 55]
for score in scores:
    grade = get_grade(score)
    print(f"Score: {score} → Grade: {grade}")

print("\n=== SHORT-CIRCUIT EVALUATION ===")

# Python stops evaluating as soon as it knows the result
def expensive_operation():
    print("This is expensive!")
    return True

# With AND: if first is False, second won't be evaluated
result1 = False and expensive_operation()  # expensive_operation() won't run
print(f"False and expensive: {result1}")

# With OR: if first is True, second won't be evaluated
result2 = True or expensive_operation()  # expensive_operation() won't run
print(f"True or expensive: {result2}")

# This will run expensive_operation()
result3 = True and expensive_operation()
print(f"True and expensive: {result3}")

print("\n=== BOOLEAN IN CONDITIONS ===")

# Boolean values in if statements
user_logged_in = True
is_premium = False

if user_logged_in:
    print("Welcome back!")
    if is_premium:
        print("Enjoy premium features!")
    else:
        print("Upgrade to premium for more features!")
else:
    print("Please log in.")

# Using boolean variables to control program flow
game_running = True
score = 0

print(f"Game running: {game_running}")
print(f"Score: {score}")

# Simulate game loop
if game_running:
    print("Playing game...")
    score += 100
    print(f"New score: {score}")

"""
Key Points to Remember:
1. Boolean has only two values: True and False
2. Comparison operators (==, !=, <, >, <=, >=) return booleans
3. Logical operators: and, or, not
4. Truthy values: non-zero numbers, non-empty strings/lists
5. Falsy values: 0, 0.0, '', [], None, False
6. Use bool() to convert to boolean
7. Short-circuit evaluation saves computation
8. Booleans are essential for decision-making in programs
"""
