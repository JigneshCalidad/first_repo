"""
🎯 EXERCISES - Python Basics
============================

Practice exercises for Python basics. Try to solve these on your own
before looking at the solutions! 💪
"""

print("=== EXERCISE 1: VARIABLES AND DATA TYPES ===")
print("""
Create variables for:
1. Your name (string)
2. Your age (integer)
3. Your height in meters (float)
4. Whether you like Python (boolean)

Then print them in a formatted sentence.
""")

# Your solution here
# name = "Your Name"
# age = 25
# height = 1.75
# likes_python = True
# print(f"Hi, I'm {name}, {age} years old, {height}m tall, and I {'love' if likes_python else 'don't like'} Python!")

print("\n=== EXERCISE 2: STRING MANIPULATION ===")
print("""
Given the string "Hello, World!", write code to:
1. Print the length of the string
2. Print the string in uppercase
3. Print the string in lowercase
4. Print the string reversed
5. Print the string with each word capitalized
""")

# Your solution here
# text = "Hello, World!"
# print(f"Length: {len(text)}")
# print(f"Uppercase: {text.upper()}")
# print(f"Lowercase: {text.lower()}")
# print(f"Reversed: {text[::-1]}")
# print(f"Title case: {text.title()}")

print("\n=== EXERCISE 3: LIST OPERATIONS ===")
print("""
Create a list of your favorite fruits and:
1. Print the list
2. Add a new fruit to the end
3. Insert a fruit at the beginning
4. Remove a fruit from the middle
5. Print the final list
""")

# Your solution here
# fruits = ["apple", "banana", "cherry"]
# print(f"Original: {fruits}")
# fruits.append("orange")
# fruits.insert(0, "grape")
# fruits.remove("banana")
# print(f"Final: {fruits}")

print("\n=== EXERCISE 4: CONDITIONAL STATEMENTS ===")
print("""
Write a program that:
1. Asks the user for their age
2. Determines if they are a child (0-12), teenager (13-19), adult (20-64), or senior (65+)
3. Prints an appropriate message
""")

# Your solution here
# age = int(input("Enter your age: "))
# if age <= 12:
#     print("You are a child!")
# elif age <= 19:
#     print("You are a teenager!")
# elif age <= 64:
#     print("You are an adult!")
# else:
#     print("You are a senior!")

print("\n=== EXERCISE 5: LOOPS ===")
print("""
Write a program that:
1. Prints numbers 1 to 10
2. Prints only even numbers from 1 to 20
3. Prints the multiplication table for 5 (1x5 to 10x5)
""")

# Your solution here
# print("Numbers 1 to 10:")
# for i in range(1, 11):
#     print(i)
# 
# print("Even numbers 1 to 20:")
# for i in range(2, 21, 2):
#     print(i)
# 
# print("Multiplication table for 5:")
# for i in range(1, 11):
#     print(f"{i} x 5 = {i * 5}")

print("\n=== EXERCISE 6: FUNCTIONS ===")
print("""
Create a function called calculate_area that:
1. Takes length and width as parameters
2. Returns the area of a rectangle
3. Test it with different values
""")

# Your solution here
# def calculate_area(length, width):
#     return length * width
# 
# print(f"Area of 5x3 rectangle: {calculate_area(5, 3)}")
# print(f"Area of 10x7 rectangle: {calculate_area(10, 7)}")

print("\n=== EXERCISE 7: STRING METHODS ==="")
print("""
Given the string "  Python Programming  ", write code to:
1. Remove leading and trailing whitespace
2. Replace "Programming" with "Basics"
3. Split the string into words
4. Join the words with hyphens
""")

# Your solution here
# text = "  Python Programming  "
# cleaned = text.strip()
# replaced = cleaned.replace("Programming", "Basics")
# words = replaced.split()
# joined = "-".join(words)
# print(f"Original: '{text}'")
# print(f"Cleaned: '{cleaned}'")
# print(f"Replaced: '{replaced}'")
# print(f"Words: {words}")
# print(f"Joined: '{joined}'")

print("\n=== EXERCISE 8: LIST COMPREHENSION ===")
print("""
Use list comprehension to:
1. Create a list of squares from 1 to 10
2. Create a list of even numbers from 1 to 20
3. Create a list of words longer than 5 characters from a given list
""")

# Your solution here
# squares = [x**2 for x in range(1, 11)]
# evens = [x for x in range(1, 21) if x % 2 == 0]
# words = ["apple", "banana", "cherry", "date", "elderberry"]
# long_words = [word for word in words if len(word) > 5]
# print(f"Squares: {squares}")
# print(f"Evens: {evens}")
# print(f"Long words: {long_words}")

print("\n=== EXERCISE 9: ERROR HANDLING ==="")
print("""
Write a program that:
1. Asks the user for two numbers
2. Divides the first by the second
3. Handles the case where the second number is 0
4. Prints the result or an error message
""")

# Your solution here
# try:
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     result = num1 / num2
#     print(f"Result: {result}")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")
# except ValueError:
#     print("Error: Please enter valid numbers!")

print("\n=== EXERCISE 10: PRACTICAL PROJECT ==="")
print("""
Create a simple calculator that:
1. Asks the user for two numbers
2. Asks the user for an operation (+, -, *, /)
3. Performs the operation
4. Displays the result
5. Asks if the user wants to continue
6. Repeats until the user says no
""")

# Your solution here
# while True:
#     try:
#         num1 = float(input("Enter first number: "))
#         operation = input("Enter operation (+, -, *, /): ")
#         num2 = float(input("Enter second number: "))
#         
#         if operation == "+":
#             result = num1 + num2
#         elif operation == "-":
#             result = num1 - num2
#         elif operation == "*":
#             result = num1 * num2
#         elif operation == "/":
#             result = num1 / num2
#         else:
#             print("Invalid operation!")
#             continue
#         
#         print(f"Result: {result}")
#         
#         continue_calc = input("Do you want to continue? (y/n): ")
#         if continue_calc.lower() != 'y':
#             break
#             
#     except ValueError:
#         print("Please enter valid numbers!")
#     except ZeroDivisionError:
#         print("Cannot divide by zero!")

print("\n=== BONUS EXERCISES ===")
print("""
1. Create a program that generates a random password
2. Write a function that checks if a string is a palindrome
3. Create a program that counts the frequency of each letter in a text
4. Write a function that sorts a list without using the sort() method
5. Create a program that simulates a simple bank account
""")

print("\n=== SOLUTIONS ===")
print("""
Uncomment the code above to see the solutions!
Remember: The best way to learn is by trying to solve
the problems yourself first, then checking the solutions.
""")

"""
Key Points to Remember:
1. Practice regularly - even 30 minutes a day helps
2. Don't just read the code - run it and modify it
3. Try to solve problems on your own first
4. Experiment with different approaches
5. Ask questions when you're stuck
6. Build projects to apply your knowledge
7. Practice with real-world examples
8. Don't be afraid to make mistakes - they're part of learning!
"""
