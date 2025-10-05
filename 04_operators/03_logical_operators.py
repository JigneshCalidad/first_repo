"""
🔗 OPERATORS - Logical Operators
================================

Logical operators combine boolean values to make complex decisions.
They're like the "and", "or", "not" in everyday language! 🧠
"""

print("=== LOGICAL OPERATORS ===")

# Basic boolean values
is_sunny = True
is_warm = False
is_weekend = True

print(f"is_sunny = {is_sunny}")
print(f"is_warm = {is_warm}")
print(f"is_weekend = {is_weekend}")

# AND operator (&& in other languages)
# Both conditions must be True
perfect_weather = is_sunny and is_warm
print(f"Perfect weather (sunny AND warm): {perfect_weather}")

# OR operator (|| in other languages)
# At least one condition must be True
good_weather = is_sunny or is_warm
print(f"Good weather (sunny OR warm): {good_weather}")

# NOT operator (! in other languages)
# Reverses the boolean value
not_sunny = not is_sunny
print(f"Not sunny: {not_sunny}")

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

print("\n=== COMPLEX LOGICAL EXPRESSIONS ===")

# Multiple conditions
age = 25
has_license = True
has_insurance = False
is_weekend = True

print(f"Age: {age}, Has license: {has_license}")
print(f"Has insurance: {has_insurance}, Is weekend: {is_weekend}")

# Complex conditions
can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")

should_drive = can_drive and (has_insurance or is_weekend)
print(f"Should drive: {should_drive}")

# Parentheses for clarity
condition1 = (age >= 18) and (has_license and has_insurance)
condition2 = (age >= 18) and (has_license or is_weekend)
print(f"Condition 1 (license AND insurance): {condition1}")
print(f"Condition 2 (license OR weekend): {condition2}")

print("\n=== SHORT-CIRCUIT EVALUATION ===")

# Python stops evaluating as soon as it knows the result
def expensive_check():
    print("  Running expensive check...")
    return True

print("Short-circuit examples:")

# With AND: if first is False, second won't be evaluated
print("False and expensive_check():")
result1 = False and expensive_check()  # expensive_check() won't run
print(f"Result: {result1}")

# With OR: if first is True, second won't be evaluated
print("\nTrue or expensive_check():")
result2 = True or expensive_check()  # expensive_check() won't run
print(f"Result: {result2}")

# This will run expensive_check()
print("\nTrue and expensive_check():")
result3 = True and expensive_check()
print(f"Result: {result3}")

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: User authentication
def check_login(username, password, is_admin=False):
    """Check if user can login"""
    # Basic validation
    has_username = len(username) > 0
    has_password = len(password) > 0
    valid_credentials = username == "admin" and password == "password"
    
    # Admin check
    is_admin_user = valid_credentials and is_admin
    
    print(f"Username: '{username}', Password: '{password}', Admin: {is_admin}")
    print(f"Has username: {has_username}")
    print(f"Has password: {has_password}")
    print(f"Valid credentials: {valid_credentials}")
    print(f"Is admin user: {is_admin_user}")
    
    return has_username and has_password and valid_credentials

# Test authentication
print("=== Authentication Tests ===")
check_login("admin", "password", True)
print()
check_login("user", "wrong", False)
print()
check_login("", "password", False)

# Example 2: Shopping cart validation
def validate_cart(items, total, has_coupon=False):
    """Validate shopping cart"""
    has_items = len(items) > 0
    valid_total = total > 0
    can_checkout = has_items and valid_total
    gets_discount = has_coupon and total >= 50
    
    print(f"Items: {items}, Total: ${total}, Has coupon: {has_coupon}")
    print(f"Has items: {has_items}")
    print(f"Valid total: {valid_total}")
    print(f"Can checkout: {can_checkout}")
    print(f"Gets discount: {gets_discount}")
    
    return can_checkout

# Test cart validation
print("\n=== Cart Validation Tests ===")
validate_cart(["apple", "banana"], 15.50, True)
print()
validate_cart([], 0, False)
print()
validate_cart(["book"], 75.00, True)

# Example 3: Weather conditions
def should_go_outside(temperature, is_raining, is_windy, has_umbrella=False):
    """Decide if it's good to go outside"""
    is_warm = temperature > 20
    is_not_raining = not is_raining
    is_not_windy = not is_windy
    has_protection = has_umbrella or is_not_raining
    
    perfect_weather = is_warm and is_not_raining and is_not_windy
    acceptable_weather = is_warm and has_protection
    
    print(f"Temperature: {temperature}°C, Raining: {is_raining}")
    print(f"Windy: {is_windy}, Has umbrella: {has_umbrella}")
    print(f"Perfect weather: {perfect_weather}")
    print(f"Acceptable weather: {acceptable_weather}")
    
    return perfect_weather or acceptable_weather

# Test weather conditions
print("\n=== Weather Decision Tests ===")
should_go_outside(25, False, False, False)  # Perfect day
print()
should_go_outside(15, True, False, True)    # Rainy but has umbrella
print()
should_go_outside(10, True, True, False)    # Bad weather

print("\n=== LOGICAL OPERATORS WITH DIFFERENT TYPES ===")

# Logical operators with non-boolean values
print("Logical operators with different types:")

# AND with different types
print(f"True and 'hello': {True and 'hello'}")      # Returns 'hello'
print(f"False and 'hello': {False and 'hello'}")    # Returns False
print(f"'hello' and 'world': {'hello' and 'world'}") # Returns 'world'

# OR with different types
print(f"True or 'hello': {True or 'hello'}")        # Returns True
print(f"False or 'hello': {False or 'hello'}")      # Returns 'hello'
print(f"'hello' or 'world': {'hello' or 'world'}")  # Returns 'hello'

# NOT with different types
print(f"not 'hello': {not 'hello'}")                # Returns False
print(f"not '': {not ''}")                          # Returns True
print(f"not 0: {not 0}")                            # Returns True
print(f"not 42: {not 42}")                          # Returns False

print("\n=== COMMON LOGICAL PATTERNS ===")

# Pattern 1: All conditions must be true
def all_conditions_true(condition1, condition2, condition3):
    """Check if all conditions are true"""
    return condition1 and condition2 and condition3

# Pattern 2: At least one condition must be true
def any_condition_true(condition1, condition2, condition3):
    """Check if any condition is true"""
    return condition1 or condition2 or condition3

# Pattern 3: Exclusive OR (XOR) - exactly one true
def exclusive_or(condition1, condition2):
    """Exclusive OR - exactly one condition true"""
    return (condition1 and not condition2) or (not condition1 and condition2)

# Test patterns
print("Pattern testing:")
print(f"All true: {all_conditions_true(True, True, True)}")
print(f"Any true: {any_condition_true(False, True, False)}")
print(f"XOR: {exclusive_or(True, False)}")
print(f"XOR: {exclusive_or(True, True)}")

print("\n=== OPERATOR PRECEDENCE ===")

# Logical operator precedence
print("Logical operator precedence (highest to lowest):")
print("1. not")
print("2. and")
print("3. or")

# Examples
a = True
b = False
c = True

print(f"\na = {a}, b = {b}, c = {c}")
print(f"not a and b: {not a and b}")        # (not a) and b
print(f"a and b or c: {a and b or c}")       # (a and b) or c
print(f"a and (b or c): {a and (b or c)}")  # a and (b or c)

print("\n=== LOGICAL OPERATORS SUMMARY ===")

print("""
Logical Operators:
- and: Both conditions must be True
- or: At least one condition must be True
- not: Reverses the boolean value

Key Points:
1. Use parentheses for clarity
2. Python uses short-circuit evaluation
3. and/or can work with non-boolean values
4. not always returns True or False
5. Precedence: not > and > or
6. Use for complex decision-making
7. Essential for conditional statements
8. Can combine multiple conditions
""")

"""
Key Points to Remember:
1. and: Both conditions must be True
2. or: At least one condition must be True
3. not: Reverses the boolean value
4. Use parentheses for clarity in complex expressions
5. Python uses short-circuit evaluation
6. and/or can work with non-boolean values
7. Precedence: not > and > or
8. Essential for making complex decisions
9. Use for validation and conditional logic
10. Practice with real-world examples
"""
