"""
⚖️ OPERATORS - Comparison Operators
==================================

Comparison operators compare two values and return True or False.
They're essential for making decisions in your programs! 🤔
"""

print("=== BASIC COMPARISON OPERATORS ===")

# Let's compare some values
a = 10
b = 5
c = 10

print(f"a = {a}, b = {b}, c = {c}")

# Equal to (==)
print(f"a == b: {a == b}")      # False
print(f"a == c: {a == c}")     # True

# Not equal to (!=)
print(f"a != b: {a != b}")     # True
print(f"a != c: {a != c}")     # False

# Greater than (>)
print(f"a > b: {a > b}")       # True
print(f"b > a: {b > a}")       # False

# Less than (<)
print(f"a < b: {a < b}")       # False
print(f"b < a: {b < a}")       # True

# Greater than or equal to (>=)
print(f"a >= b: {a >= b}")     # True
print(f"a >= c: {a >= c}")     # True
print(f"b >= a: {b >= a}")     # False

# Less than or equal to (<=)
print(f"a <= b: {a <= b}")     # False
print(f"a <= c: {a <= c}")     # True
print(f"b <= a: {b <= a}")     # True

print("\n=== STRING COMPARISONS ===")

# Strings are compared alphabetically
name1 = "Alice"
name2 = "Bob"
name3 = "Alice"

print(f"'{name1}' == '{name2}': {name1 == name2}")  # False
print(f"'{name1}' == '{name3}': {name1 == name3}")  # True
print(f"'{name1}' < '{name2}': {name1 < name2}")    # True (A comes before B)
print(f"'{name2}' > '{name1}': {name2 > name1}")    # True

# Case-sensitive comparison
word1 = "Hello"
word2 = "hello"
print(f"'{word1}' == '{word2}': {word1 == word2}")  # False (case matters)

# Case-insensitive comparison
print(f"'{word1.lower()}' == '{word2.lower()}': {word1.lower() == word2.lower()}")  # True

print("\n=== NUMERIC COMPARISONS ===")

# Different number types
int_num = 10
float_num = 10.0
print(f"int {int_num} == float {float_num}: {int_num == float_num}")  # True

# Decimal precision
num1 = 0.1 + 0.2
num2 = 0.3
print(f"0.1 + 0.2 == 0.3: {num1 == num2}")  # False! (floating point precision)
print(f"0.1 + 0.2 = {num1}")
print(f"0.3 = {num2}")

# Safe comparison for floats
tolerance = 0.0001
print(f"Safe comparison: {abs(num1 - num2) < tolerance}")

print("\n=== CHAINED COMPARISONS ===")

# Python allows chained comparisons
x = 5
print(f"x = {x}")
print(f"3 < x < 7: {3 < x < 7}")        # True
print(f"1 < x < 3: {1 < x < 3}")        # False
print(f"5 <= x <= 10: {5 <= x <= 10}")  # True

# Equivalent to: 3 < x and x < 7
print(f"3 < x and x < 7: {3 < x and x < 7}")

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Grade classification
def get_grade(score):
    """Classify score into grade"""
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

# Test grades
scores = [95, 85, 75, 65, 55]
for score in scores:
    grade = get_grade(score)
    print(f"Score {score} → Grade {grade}")

# Example 2: Age verification
def check_age_eligibility(age):
    """Check various age-based eligibilities"""
    can_vote = age >= 18
    can_drive = age >= 16
    can_drink = age >= 21
    is_senior = age >= 65
    
    print(f"Age {age}:")
    print(f"  Can vote: {can_vote}")
    print(f"  Can drive: {can_drive}")
    print(f"  Can drink: {can_drink}")
    print(f"  Is senior: {is_senior}")

# Test different ages
ages = [15, 18, 21, 30, 65]
for age in ages:
    check_age_eligibility(age)
    print()

# Example 3: Password strength checker
def check_password_strength(password):
    """Check password strength based on length and content"""
    length_ok = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    strength_score = sum([length_ok, has_upper, has_lower, has_digit])
    
    if strength_score == 4:
        return "Strong"
    elif strength_score >= 2:
        return "Medium"
    else:
        return "Weak"

# Test passwords
passwords = ["password", "Password", "Password123", "P@ssw0rd!"]
for pwd in passwords:
    strength = check_password_strength(pwd)
    print(f"Password '{pwd}' is {strength}")

print("\n=== COMPARISON WITH LISTS ===")

# List comparisons
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = {list3}")

print(f"list1 == list2: {list1 == list2}")  # True
print(f"list1 == list3: {list1 == list3}")  # False
print(f"list1 < list3: {list1 < list3}")   # True (element-wise comparison)

# Empty list comparisons
empty_list = []
print(f"empty_list == []: {empty_list == []}")  # True
print(f"len(empty_list) == 0: {len(empty_list) == 0}")  # True

print("\n=== SPECIAL VALUES COMPARISON ===")

# None comparisons
value = None
print(f"value == None: {value == None}")  # True
print(f"value is None: {value is None}")   # True (preferred)

# Boolean comparisons
true_val = True
false_val = False
print(f"True == 1: {True == 1}")      # True
print(f"False == 0: {False == 0}")    # True
print(f"True == 1.0: {True == 1.0}")  # True

print("\n=== COMPARISON OPERATORS SUMMARY ===")

print("""
Comparison Operators:
- == (equal to)
- != (not equal to)
- > (greater than)
- < (less than)
- >= (greater than or equal to)
- <= (less than or equal to)

Key Points:
1. All comparison operators return True or False
2. Strings are compared alphabetically
3. Case matters in string comparisons
4. Use == for equality, not = (assignment)
5. Chained comparisons: 3 < x < 7
6. Be careful with floating point comparisons
7. Use is/is not for None comparisons
8. Lists are compared element-wise
""")

print("\n=== TRUTH TABLES ===")

# Demonstrate truth tables
print("Equality (==) Truth Table:")
print("True == True:", True == True)
print("True == False:", True == False)
print("False == True:", False == True)
print("False == False:", False == False)

print("\nInequality (!=) Truth Table:")
print("True != True:", True != True)
print("True != False:", True != False)
print("False != True:", False != True)
print("False != False:", False != False)

"""
Key Points to Remember:
1. == checks equality, != checks inequality
2. >, <, >=, <= for numeric comparisons
3. Strings compared alphabetically (case-sensitive)
4. All comparisons return True or False
5. Use == for equality, not = (assignment)
6. Chained comparisons: 3 < x < 7
7. Be careful with floating point precision
8. Use is/is not for None comparisons
9. Lists compared element-wise
10. Comparison operators are essential for decision-making
"""
