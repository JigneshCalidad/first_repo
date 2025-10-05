"""
🐍 PYTHON BASICS - Syntax and Indentation
=========================================

Python uses INDENTATION (spaces/tabs) to organize code blocks.
This makes Python code very readable and forces good formatting!

Think of indentation like paragraphs in writing - it groups related ideas together.
"""

# Basic syntax rules
print("=== Python Syntax Rules ===")

# 1. No semicolons needed (unlike Java, C++)
print("Hello World")  # ✅ Good
# print("Hello World");  # ❌ Unnecessary semicolon

# 2. Indentation matters! Python uses it to define code blocks
if True:
    print("This is indented")  # 4 spaces (or 1 tab)
    print("This is also indented")
    if True:
        print("This is double-indented")  # 8 spaces (or 2 tabs)

# 3. Colon (:) starts a new block
if 5 > 3:
    print("5 is greater than 3")
    print("This is inside the if block")

# 4. Parentheses for grouping
result = (2 + 3) * 4  # 20
print(f"Result: {result}")

# 5. Quotes for strings
single_quote = 'Hello'
double_quote = "World"
triple_quote = """This is a
multi-line string"""

print(single_quote, double_quote)
print(triple_quote)

# Indentation examples
print("\n=== Indentation Examples ===")

# Example 1: If statement
temperature = 25
if temperature > 20:
    print("It's warm outside!")
    print("Perfect for a walk")
    if temperature > 30:
        print("Maybe too hot though...")
else:
    print("It's cool outside")
    print("Bring a jacket")

# Example 2: Function definition
def greet_person(name):
    """This function greets a person"""
    print(f"Hello, {name}!")
    print("Welcome to Python!")
    if name == "Python":
        print("You're learning about yourself!")

# Call the function
greet_person("Alice")
greet_person("Python")

# Example 3: Loop with indentation
print("\n=== Loop Example ===")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
    if fruit == "banana":
        print("  (Especially in smoothies!)")
    print("  Yummy!")

# Common indentation mistakes to avoid:
print("\n=== Common Mistakes ===")

# ❌ Wrong - inconsistent indentation
# if True:
#     print("This is indented")
#   print("This is wrong indentation")  # Error!

# ❌ Wrong - missing indentation
# if True:
# print("This will cause an error")  # IndentationError!

# ✅ Correct - consistent indentation
if True:
    print("This is correct")
    print("This is also correct")
    if True:
        print("This is double-indented correctly")

# Indentation tips:
print("\n=== Indentation Tips ===")
print("1. Use 4 spaces (recommended) or 1 tab")
print("2. Be consistent throughout your code")
print("3. Most editors can show you indentation levels")
print("4. Python will tell you if indentation is wrong")

# You can check indentation with this trick:
def show_indentation():
    """This function shows proper indentation"""
    print("Level 1 - no indentation")
    if True:
        print("Level 2 - 4 spaces")
        if True:
            print("Level 3 - 8 spaces")
            if True:
                print("Level 4 - 12 spaces")

show_indentation()

"""
Key Points:
1. Python uses indentation instead of braces {}
2. Use 4 spaces (recommended) or 1 tab consistently
3. Indentation defines code blocks
4. Colon (:) starts a new block
5. Be consistent with your indentation style
6. Most IDEs help with indentation

Remember: Python is like poetry - the structure matters! 📝
"""
