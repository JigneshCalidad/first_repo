"""
🔢 DATA TYPES - Numeric Types (Numbers)
======================================

Python has several types of numbers:
- Integers (int): Whole numbers like 1, 42, -100
- Floats (float): Decimal numbers like 3.14, 2.5, -0.5
- Complex (complex): Complex numbers like 3+4j (for advanced math)

Let's explore numbers in Python! 🧮
"""

print("=== INTEGER (int) - Whole Numbers ===")

# Positive integers
age = 25
count = 100
year = 2024

print(f"Age: {age} (type: {type(age)})")
print(f"Count: {count} (type: {type(count)})")
print(f"Year: {year} (type: {type(year)})")

# Negative integers
temperature = -10
debt = -500
print(f"Temperature: {temperature}°C")
print(f"Debt: ${debt}")

# Large integers (Python can handle huge numbers!)
big_number = 123456789012345678901234567890
print(f"Big number: {big_number}")

# Integer operations
a = 10
b = 3
print(f"\nInteger operations:")
print(f"{a} + {b} = {a + b}")  # Addition
print(f"{a} - {b} = {a - b}")  # Subtraction
print(f"{a} * {b} = {a * b}")  # Multiplication
print(f"{a} / {b} = {a / b}")  # Division (returns float!)
print(f"{a} // {b} = {a // b}")  # Floor division (integer result)
print(f"{a} % {b} = {a % b}")   # Modulo (remainder)
print(f"{a} ** {b} = {a ** b}") # Exponentiation (power)

print("\n=== FLOAT (float) - Decimal Numbers ===")

# Decimal numbers
pi = 3.14159
price = 19.99
temperature = 36.6

print(f"Pi: {pi} (type: {type(pi)})")
print(f"Price: ${price}")
print(f"Body temperature: {temperature}°C")

# Scientific notation
speed_of_light = 3.0e8  # 3.0 × 10^8
small_number = 1.5e-6   # 1.5 × 10^-6
print(f"Speed of light: {speed_of_light} m/s")
print(f"Small number: {small_number}")

# Float operations
x = 10.5
y = 3.2
print(f"\nFloat operations:")
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")
print(f"{x} // {y} = {x // y}")  # Floor division
print(f"{x} % {y} = {x % y}")    # Modulo
print(f"{x} ** {y} = {x ** y}")  # Power

print("\n=== TYPE CONVERSION ===")

# Converting between types
integer_num = 42
float_num = 3.14

# Convert int to float
int_to_float = float(integer_num)
print(f"int {integer_num} → float {int_to_float}")

# Convert float to int (truncates decimal part)
float_to_int = int(float_num)
print(f"float {float_num} → int {float_to_int}")

# Convert string to number
string_num = "123"
converted_int = int(string_num)
converted_float = float(string_num)
print(f"String '{string_num}' → int {converted_int}")
print(f"String '{string_num}' → float {converted_float}")

print("\n=== USEFUL NUMBER FUNCTIONS ===")

# Built-in functions for numbers
numbers = [1, 5, 3, 9, 2, 8, 4]
print(f"Numbers: {numbers}")
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Length: {len(numbers)}")

# Absolute value
negative_num = -42
print(f"Absolute value of {negative_num}: {abs(negative_num)}")

# Rounding
pi = 3.14159
print(f"Pi rounded to 2 decimal places: {round(pi, 2)}")
print(f"Pi rounded to nearest integer: {round(pi)}")

# Power function
base = 2
exponent = 3
print(f"{base} to the power of {exponent}: {pow(base, exponent)}")

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Calculate area of a circle
radius = 5.0
area = 3.14159 * radius ** 2
print(f"Circle with radius {radius} has area: {area:.2f}")

# Example 2: Calculate BMI
weight = 70.5  # kg
height = 1.75  # meters
bmi = weight / (height ** 2)
print(f"Weight: {weight}kg, Height: {height}m")
print(f"BMI: {bmi:.1f}")

# Example 3: Temperature conversion
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Example 4: Check if number is even or odd
number = 17
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

"""
Key Points to Remember:
1. Integers are whole numbers (positive, negative, or zero)
2. Floats are decimal numbers
3. Division (/) always returns a float
4. Floor division (//) returns an integer
5. Use type() to check the type of a variable
6. Convert between types using int(), float()
7. Python can handle very large numbers
8. Be careful with floating-point precision in calculations
"""
