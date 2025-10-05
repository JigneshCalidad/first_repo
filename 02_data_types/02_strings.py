"""
📝 DATA TYPES - Strings (Text)
=============================

Strings are sequences of characters (letters, numbers, symbols).
Think of them as text that you can manipulate, search, and modify!

In Python, strings are immutable (can't be changed directly).
"""

print("=== CREATING STRINGS ===")

# Single quotes
name1 = 'Alice'
print(f"Single quotes: {name1}")

# Double quotes
name2 = "Bob"
print(f"Double quotes: {name2}")

# Triple quotes for multi-line strings
poem = """Roses are red,
Violets are blue,
Python is awesome,
And so are you!"""
print(f"Multi-line string:\n{poem}")

# Escaping characters
escaped = "He said, \"Hello World!\""
print(f"Escaped quotes: {escaped}")

# Raw strings (ignore escape characters)
raw_string = r"C:\Users\Documents\file.txt"
print(f"Raw string: {raw_string}")

print("\n=== STRING OPERATIONS ===")

# Concatenation (joining strings)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# String repetition
stars = "*" * 10
print(f"Stars: {stars}")

# String length
text = "Hello, World!"
print(f"Length of '{text}': {len(text)} characters")

print("\n=== STRING INDEXING ===")

# Each character has an index (position)
word = "Python"
print(f"Word: {word}")
print(f"First character (index 0): {word[0]}")
print(f"Second character (index 1): {word[1]}")
print(f"Last character (index -1): {word[-1]}")
print(f"Second to last (index -2): {word[-2]}")

# String slicing [start:end:step]
print(f"First 3 characters: {word[0:3]}")
print(f"Characters 2-4: {word[1:4]}")
print(f"Last 3 characters: {word[-3:]}")
print(f"Every second character: {word[::2]}")
print(f"Reverse string: {word[::-1]}")

print("\n=== STRING METHODS ===")

text = "  Hello, World!  "
print(f"Original: '{text}'")

# Case methods
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title case: {text.title()}")
print(f"Capitalize: {text.capitalize()}")

# Whitespace methods
print(f"Strip whitespace: '{text.strip()}'")
print(f"Left strip: '{text.lstrip()}'")
print(f"Right strip: '{text.rstrip()}'")

# Search methods
sentence = "Python is awesome and Python is fun"
print(f"Sentence: {sentence}")
print(f"Starts with 'Python': {sentence.startswith('Python')}")
print(f"Ends with 'fun': {sentence.endswith('fun')}")
print(f"Contains 'awesome': {'awesome' in sentence}")
print(f"Find 'Python' at index: {sentence.find('Python')}")
print(f"Count of 'Python': {sentence.count('Python')}")

# Replace method
new_sentence = sentence.replace("Python", "Programming")
print(f"Replace 'Python' with 'Programming': {new_sentence}")

print("\n=== STRING FORMATTING ===")

# f-strings (modern way - recommended!)
name = "Alice"
age = 25
score = 95.5
print(f"Hello, {name}! You are {age} years old.")
print(f"Your score is {score:.1f}%")

# .format() method
message = "Hello, {}! You are {} years old.".format(name, age)
print(f"Using .format(): {message}")

# % formatting (older way)
message = "Hello, %s! You are %d years old." % (name, age)
print(f"Using % formatting: {message}")

print("\n=== STRING SPLITTING AND JOINING ===")

# Split string into list
sentence = "apple,banana,cherry,date"
fruits = sentence.split(",")
print(f"Split by comma: {fruits}")

# Join list into string
fruits_list = ["apple", "banana", "cherry"]
joined = ", ".join(fruits_list)
print(f"Joined with commas: {joined}")

# Split by spaces
words = "Python is awesome".split()
print(f"Split by spaces: {words}")

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: User input validation
def validate_email(email):
    """Check if email has @ symbol and .com"""
    return "@" in email and ".com" in email

email = "user@example.com"
print(f"Email '{email}' is valid: {validate_email(email)}")

# Example 2: Text processing
def count_words(text):
    """Count words in text"""
    words = text.split()
    return len(words)

text = "Python is a great programming language"
word_count = count_words(text)
print(f"Text: '{text}'")
print(f"Word count: {word_count}")

# Example 3: Password strength checker
def check_password_strength(password):
    """Check if password is strong"""
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_length = len(password) >= 8
    
    return has_upper and has_lower and has_digit and has_length

password = "MyPassword123"
is_strong = check_password_strength(password)
print(f"Password '{password}' is strong: {is_strong}")

# Example 4: Palindrome checker
def is_palindrome(word):
    """Check if word is palindrome"""
    return word.lower() == word.lower()[::-1]

test_words = ["racecar", "python", "level", "hello"]
for word in test_words:
    print(f"'{word}' is palindrome: {is_palindrome(word)}")

print("\n=== STRING ESCAPE SEQUENCES ===")

# Common escape sequences
print("New line: Hello\nWorld")
print("Tab: Hello\tWorld")
print("Backslash: C:\\Users\\Documents")
print("Quote: He said, \"Hello!\"")
print("Single quote: It's a beautiful day")

"""
Key Points to Remember:
1. Strings are sequences of characters
2. Use single or double quotes (be consistent)
3. Triple quotes for multi-line strings
4. Strings are immutable (can't change directly)
5. Use f-strings for formatting (f"Hello {name}")
6. Indexing starts at 0, negative indexing from end
7. Slicing: [start:end:step]
8. Many useful methods: upper(), lower(), split(), join()
9. Use len() to get string length
10. Escape sequences for special characters
"""
