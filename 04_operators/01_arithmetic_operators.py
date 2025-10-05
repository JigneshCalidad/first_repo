"""
➕ OPERATORS - Arithmetic Operators
==================================

Arithmetic operators perform mathematical operations on numbers.
They're the building blocks of calculations in programming! 🧮
"""

print("=== BASIC ARITHMETIC OPERATORS ===")

# Let's work with some numbers
a = 10
b = 3
print(f"a = {a}, b = {b}")

# Addition (+)
sum_result = a + b
print(f"Addition: {a} + {b} = {sum_result}")

# Subtraction (-)
difference = a - b
print(f"Subtraction: {a} - {b} = {difference}")

# Multiplication (*)
product = a * b
print(f"Multiplication: {a} * {b} = {product}")

# Division (/)
quotient = a / b
print(f"Division: {a} / {b} = {quotient}")

# Floor Division (//) - returns integer result
floor_quotient = a // b
print(f"Floor Division: {a} // {b} = {floor_quotient}")

# Modulo (%) - returns remainder
remainder = a % b
print(f"Modulo: {a} % {b} = {remainder}")

# Exponentiation (**) - power
power = a ** b
print(f"Exponentiation: {a} ** {b} = {power}")

print("\n=== OPERATOR PRECEDENCE ===")

# Order of operations (PEMDAS/BODMAS)
result1 = 2 + 3 * 4
result2 = (2 + 3) * 4
result3 = 2 ** 3 * 4
result4 = 2 ** (3 * 4)

print(f"2 + 3 * 4 = {result1}")        # Multiplication first
print(f"(2 + 3) * 4 = {result2}")       # Parentheses first
print(f"2 ** 3 * 4 = {result3}")        # Exponentiation first
print(f"2 ** (3 * 4) = {result4}")       # Parentheses first

# Precedence order (highest to lowest):
print("""
Operator Precedence (highest to lowest):
1. ** (Exponentiation)
2. *, /, //, % (Multiplication, Division, Floor Division, Modulo)
3. +, - (Addition, Subtraction)
4. Parentheses () override precedence
""")

print("\n=== ASSIGNMENT OPERATORS ===")

# Basic assignment
x = 10
print(f"Initial x: {x}")

# Addition assignment
x += 5  # Same as x = x + 5
print(f"After x += 5: {x}")

# Subtraction assignment
x -= 3  # Same as x = x - 3
print(f"After x -= 3: {x}")

# Multiplication assignment
x *= 2  # Same as x = x * 2
print(f"After x *= 2: {x}")

# Division assignment
x /= 4  # Same as x = x / 4
print(f"After x /= 4: {x}")

# Floor division assignment
x //= 2  # Same as x = x // 2
print(f"After x //= 2: {x}")

# Modulo assignment
x %= 3  # Same as x = x % 3
print(f"After x %= 3: {x}")

# Exponentiation assignment
x **= 2  # Same as x = x ** 2
print(f"After x **= 2: {x}")

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Calculator functions
def calculator(num1, num2, operation):
    """Basic calculator with different operations"""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
    elif operation == "//":
        return num1 // num2
    elif operation == "%":
        return num1 % num2
    elif operation == "**":
        return num1 ** num2
    else:
        return "Invalid operation!"

# Test calculator
print("Calculator Examples:")
print(f"10 + 3 = {calculator(10, 3, '+')}")
print(f"10 - 3 = {calculator(10, 3, '-')}")
print(f"10 * 3 = {calculator(10, 3, '*')}")
print(f"10 / 3 = {calculator(10, 3, '/')}")
print(f"10 // 3 = {calculator(10, 3, '//')}")
print(f"10 % 3 = {calculator(10, 3, '%')}")
print(f"10 ** 3 = {calculator(10, 3, '**')}")

# Example 2: Area and perimeter calculations
def calculate_circle(radius):
    """Calculate circle area and circumference"""
    pi = 3.14159
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return area, circumference

def calculate_rectangle(length, width):
    """Calculate rectangle area and perimeter"""
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Test calculations
radius = 5
area, circumference = calculate_circle(radius)
print(f"\nCircle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")

length, width = 4, 6
area, perimeter = calculate_rectangle(length, width)
print(f"\nRectangle {length}x{width}:")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

# Example 3: Number manipulation
def manipulate_number(number):
    """Demonstrate various number operations"""
    print(f"Original number: {number}")
    
    # Double it
    doubled = number * 2
    print(f"Doubled: {doubled}")
    
    # Square it
    squared = number ** 2
    print(f"Squared: {squared}")
    
    # Half it
    halved = number / 2
    print(f"Halved: {halved}")
    
    # Check if even or odd
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    
    # Find remainder when divided by 3
    remainder = number % 3
    print(f"Remainder when divided by 3: {remainder}")

manipulate_number(15)

print("\n=== FLOATING POINT ARITHMETIC ===")

# Working with decimal numbers
price = 19.99
tax_rate = 0.08
quantity = 3

# Calculate total with tax
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Price per item: ${price}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Total: ${total:.2f}")

# Rounding results
print(f"Total rounded to nearest dollar: ${round(total)}")
print(f"Total rounded to 1 decimal: ${round(total, 1)}")

print("\n=== LARGE NUMBER OPERATIONS ===")

# Python can handle very large numbers
big_number1 = 123456789012345678901234567890
big_number2 = 987654321098765432109876543210

print(f"Big number 1: {big_number1}")
print(f"Big number 2: {big_number2}")
print(f"Sum: {big_number1 + big_number2}")
print(f"Product: {big_number1 * big_number2}")

print("\n=== ARITHMETIC WITH DIFFERENT TYPES ===")

# Mixing integers and floats
int_num = 10
float_num = 3.5

print(f"Integer: {int_num}, Float: {float_num}")
print(f"int + float: {int_num + float_num} (type: {type(int_num + float_num)})")
print(f"int * float: {int_num * float_num} (type: {type(int_num * float_num)})")

# Division always returns float
result = 10 / 2
print(f"10 / 2 = {result} (type: {type(result)})")

print("\n=== COMMON ARITHMETIC PATTERNS ===")

# Increment and decrement
counter = 0
print(f"Initial counter: {counter}")

counter += 1  # Increment
print(f"After increment: {counter}")

counter -= 1  # Decrement
print(f"After decrement: {counter}")

# Accumulator pattern
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num  # Accumulate sum
print(f"Sum of {numbers}: {total}")

# Average calculation
average = total / len(numbers)
print(f"Average: {average}")

"""
Key Points to Remember:
1. + (addition), - (subtraction), * (multiplication)
2. / (division) always returns float
3. // (floor division) returns integer
4. % (modulo) returns remainder
5. ** (exponentiation) for powers
6. Operator precedence: ** > *,/,//,% > +,-
7. Use parentheses to override precedence
8. Assignment operators: +=, -=, *=, /=, etc.
9. Python can handle very large numbers
10. Mixing int and float results in float
"""
