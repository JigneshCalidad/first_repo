"""
🎯 FLOW CONTROL - If/Else Statements
===================================

If/else statements let your program make decisions based on conditions.
They're like crossroads in your code - choose which path to take! 🛤️
"""

print("=== BASIC IF STATEMENT ===")

# Simple if statement
age = 18
print(f"Age: {age}")

if age >= 18:
    print("You are an adult! 🎉")

# If with comparison
temperature = 25
print(f"Temperature: {temperature}°C")

if temperature > 20:
    print("It's warm outside! ☀️")

print("\n=== IF-ELSE STATEMENT ===")

# If-else statement
score = 85
print(f"Score: {score}")

if score >= 70:
    print("You passed! ✅")
else:
    print("You failed! ❌")

# Another example
weather = "rainy"
print(f"Weather: {weather}")

if weather == "sunny":
    print("Perfect day for a picnic! 🧺")
else:
    print("Better stay indoors! 🏠")

print("\n=== IF-ELIF-ELSE STATEMENT ===")

# Multiple conditions with elif
grade = 85
print(f"Grade: {grade}")

if grade >= 90:
    print("Grade: A - Excellent! 🌟")
elif grade >= 80:
    print("Grade: B - Good job! 👍")
elif grade >= 70:
    print("Grade: C - Satisfactory! ✅")
elif grade >= 60:
    print("Grade: D - Needs improvement! 📈")
else:
    print("Grade: F - Failed! ❌")

# Temperature example
temp = 15
print(f"\nTemperature: {temp}°C")

if temp > 30:
    print("It's very hot! 🔥")
elif temp > 20:
    print("It's warm! ☀️")
elif temp > 10:
    print("It's cool! 🌤️")
else:
    print("It's cold! ❄️")

print("\n=== NESTED IF STATEMENTS ===")

# Nested if statements
age = 20
has_license = True
has_insurance = True

print(f"Age: {age}, Has license: {has_license}, Has insurance: {has_insurance}")

if age >= 18:
    print("You are an adult!")
    if has_license:
        print("You have a driver's license!")
        if has_insurance:
            print("You can drive safely! 🚗")
        else:
            print("You need insurance to drive!")
    else:
        print("You need a driver's license!")
else:
    print("You are not an adult yet!")

print("\n=== COMPLEX CONDITIONS ===")

# Multiple conditions with logical operators
username = "admin"
password = "password123"
is_admin = True

print(f"Username: {username}, Password: {password}, Is admin: {is_admin}")

if username == "admin" and password == "password123":
    print("Login successful! ✅")
    if is_admin:
        print("Welcome, Administrator! 👑")
    else:
        print("Welcome, User! 👤")
else:
    print("Login failed! ❌")

# Weather decision with multiple factors
temperature = 25
is_sunny = True
is_weekend = True

print(f"\nTemperature: {temperature}°C, Sunny: {is_sunny}, Weekend: {is_weekend}")

if temperature > 20 and is_sunny:
    print("Perfect weather for outdoor activities! 🏃‍♂️")
    if is_weekend:
        print("Great weekend weather! 🎉")
    else:
        print("Nice weather for a weekday! 😊")
elif temperature > 15:
    print("Decent weather! 🌤️")
else:
    print("Not great weather! ☁️")

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Age-based permissions
def check_permissions(age, has_parent_consent=False):
    """Check what a person can do based on age"""
    print(f"Age: {age}, Parent consent: {has_parent_consent}")
    
    if age >= 18:
        print("✅ Can vote")
        print("✅ Can drive")
        print("✅ Can drink (in most places)")
        print("✅ Can work without restrictions")
    elif age >= 16:
        print("✅ Can drive (with restrictions)")
        print("✅ Can work (with restrictions)")
        print("❌ Cannot vote")
        print("❌ Cannot drink")
    elif age >= 13:
        print("✅ Can use social media (with supervision)")
        print("❌ Cannot drive")
        print("❌ Cannot vote")
        print("❌ Cannot work")
    else:
        print("❌ Limited activities")
        if has_parent_consent:
            print("✅ Some activities allowed with parent consent")

# Test different ages
check_permissions(25)
print()
check_permissions(16)
print()
check_permissions(10, True)

# Example 2: Shopping cart logic
def process_order(items, total, has_coupon=False, is_member=False):
    """Process shopping cart with discounts"""
    print(f"Items: {items}, Total: ${total}")
    print(f"Has coupon: {has_coupon}, Is member: {is_member}")
    
    # Calculate discounts
    discount = 0
    if is_member and total >= 100:
        discount = 0.1  # 10% member discount
        print("🎉 Member discount applied!")
    elif has_coupon and total >= 50:
        discount = 0.05  # 5% coupon discount
        print("🎫 Coupon discount applied!")
    
    # Apply discount
    if discount > 0:
        savings = total * discount
        final_total = total - savings
        print(f"Savings: ${savings:.2f}")
        print(f"Final total: ${final_total:.2f}")
    else:
        print("No discount applied")
        print(f"Final total: ${total:.2f}")

# Test shopping scenarios
process_order(["book", "pen"], 25.00, False, False)
print()
process_order(["laptop", "mouse"], 1200.00, False, True)
print()
process_order(["shirt", "pants"], 75.00, True, False)

# Example 3: Grade calculator with feedback
def calculate_grade_with_feedback(score, attendance, participation):
    """Calculate grade with detailed feedback"""
    print(f"Score: {score}, Attendance: {attendance}%, Participation: {participation}%")
    
    # Check if student passed
    if attendance < 70:
        print("❌ Failed due to poor attendance")
        return "F"
    
    if participation < 50:
        print("⚠️ Low participation - needs improvement")
    
    # Calculate grade
    if score >= 90:
        grade = "A"
        feedback = "Outstanding work! 🌟"
    elif score >= 80:
        grade = "B"
        feedback = "Good job! 👍"
    elif score >= 70:
        grade = "C"
        feedback = "Satisfactory work ✅"
    elif score >= 60:
        grade = "D"
        feedback = "Needs improvement 📈"
    else:
        grade = "F"
        feedback = "Failed - study harder! 📚"
    
    print(f"Grade: {grade}")
    print(f"Feedback: {feedback}")
    
    # Additional feedback based on participation
    if participation >= 80:
        print("🎉 Excellent participation!")
    elif participation >= 60:
        print("👍 Good participation")
    else:
        print("📈 Work on participation")
    
    return grade

# Test grade calculation
calculate_grade_with_feedback(85, 90, 75)
print()
calculate_grade_with_feedback(65, 60, 40)  # Low attendance
print()
calculate_grade_with_feedback(95, 95, 90)  # Excellent student

print("\n=== CONDITIONAL EXPRESSIONS (TERNARY) ===")

# Ternary operator (conditional expression)
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Age {age}: {status}")

# Multiple ternary operators
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"Score {score}: Grade {grade}")

# Practical ternary examples
temperature = 25
weather_advice = "Wear light clothes! 👕" if temperature > 20 else "Wear warm clothes! 🧥"
print(f"Temperature {temperature}°C: {weather_advice}")

print("\n=== COMMON IF/ELSE PATTERNS ===")

# Pattern 1: Range checking
def check_range(value, min_val, max_val):
    """Check if value is within range"""
    if min_val <= value <= max_val:
        print(f"{value} is within range [{min_val}, {max_val}]")
    else:
        print(f"{value} is outside range [{min_val}, {max_val}]")

check_range(15, 10, 20)
check_range(5, 10, 20)

# Pattern 2: Input validation
def validate_input(value, expected_type):
    """Validate input based on type"""
    if expected_type == "number":
        try:
            num = float(value)
            print(f"Valid number: {num}")
        except ValueError:
            print("Invalid number!")
    elif expected_type == "email":
        if "@" in value and "." in value:
            print(f"Valid email: {value}")
        else:
            print("Invalid email!")
    else:
        print("Unknown validation type")

validate_input("123", "number")
validate_input("abc", "number")
validate_input("user@example.com", "email")
validate_input("invalid-email", "email")

print("\n=== IF/ELSE BEST PRACTICES ===")

print("""
Best Practices for If/Else:
1. Use clear, descriptive condition names
2. Keep conditions simple and readable
3. Use elif for multiple related conditions
4. Avoid deeply nested if statements
5. Use parentheses for complex conditions
6. Consider using functions for complex logic
7. Test all possible conditions
8. Use meaningful variable names
9. Add comments for complex logic
10. Consider using switch-like patterns with elif
""")

"""
Key Points to Remember:
1. if: Execute code if condition is True
2. else: Execute code if condition is False
3. elif: Check additional conditions
4. Use comparison operators (==, !=, <, >, <=, >=)
5. Use logical operators (and, or, not)
6. Indentation is crucial in Python
7. Use parentheses for complex conditions
8. Test all possible code paths
9. Keep conditions simple and readable
10. Practice with real-world examples
"""
