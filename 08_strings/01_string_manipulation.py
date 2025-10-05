"""
📝 STRINGS - String Manipulation
================================

Strings are sequences of characters. Learn how to manipulate,
search, and transform text data in Python! 🔤
"""

print("=== STRING CREATION ===")

# Different ways to create strings
single_quote = 'Hello, World!'
double_quote = "Hello, World!"
triple_quote = """This is a
multi-line string"""

print(f"Single quote: {single_quote}")
print(f"Double quote: {double_quote}")
print(f"Triple quote: {triple_quote}")

# Raw strings (ignore escape characters)
raw_string = r"C:\Users\Documents\file.txt"
print(f"Raw string: {raw_string}")

# String with escape characters
escaped_string = "He said, \"Hello World!\""
print(f"Escaped string: {escaped_string}")

print("\n=== STRING INDEXING AND SLICING ===")

# String indexing
text = "Python Programming"
print(f"Text: {text}")
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"Character at index 3: {text[3]}")

# String slicing
print(f"First 6 characters: {text[0:6]}")
print(f"Characters 7-17: {text[7:17]}")
print(f"Last 5 characters: {text[-5:]}")
print(f"Every 2nd character: {text[::2]}")
print(f"Reverse string: {text[::-1]}")

# Step slicing
print(f"Every 3rd character: {text[::3]}")

print("\n=== STRING METHODS ===")

# Case methods
text = "  Hello, World!  "
print(f"Original: '{text}'")

print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title case: {text.title()}")
print(f"Capitalize: {text.capitalize()}")
print(f"Swap case: {text.swapcase()}")

# Whitespace methods
print(f"Strip: '{text.strip()}'")
print(f"Left strip: '{text.lstrip()}'")
print(f"Right strip: '{text.rstrip()}'")

# Search methods
sentence = "Python is awesome and Python is fun"
print(f"Sentence: {sentence}")

print(f"Starts with 'Python': {sentence.startswith('Python')}")
print(f"Ends with 'fun': {sentence.endswith('fun')}")
print(f"Contains 'awesome': {'awesome' in sentence}")
print(f"Find 'Python' at: {sentence.find('Python')}")
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
print(f"Next year you'll be {age + 1}")

# .format() method
message = "Hello, {}! You are {} years old.".format(name, age)
print(f"Using .format(): {message}")

# % formatting (older way)
message = "Hello, %s! You are %d years old." % (name, age)
print(f"Using % formatting: {message}")

# Multiple formatting examples
price = 19.99
quantity = 3
total = price * quantity

print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: ${total:.2f}")

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

# Split with max splits
text = "one,two,three,four,five"
parts = text.split(",", 2)
print(f"Split with max 2: {parts}")

print("\n=== STRING VALIDATION ===")

# Check string properties
def validate_string(text):
    """Validate string properties"""
    print(f"Text: '{text}'")
    print(f"Length: {len(text)}")
    print(f"Is alpha: {text.isalpha()}")
    print(f"Is digit: {text.isdigit()}")
    print(f"Is alnum: {text.isalnum()}")
    print(f"Is space: {text.isspace()}")
    print(f"Is lower: {text.islower()}")
    print(f"Is upper: {text.isupper()}")
    print(f"Starts with letter: {text[0].isalpha() if text else False}")

# Test validation
test_strings = ["Hello", "123", "Hello123", "   ", "hello", "HELLO"]
for text in test_strings:
    validate_string(text)
    print()

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Text analyzer
def analyze_text(text):
    """Analyze text for various statistics"""
    print(f"Text Analysis: '{text}'")
    print("-" * 40)
    
    # Basic statistics
    char_count = len(text)
    word_count = len(text.split())
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    
    print(f"Character count: {char_count}")
    print(f"Word count: {word_count}")
    print(f"Sentence count: {sentence_count}")
    
    # Letter frequency
    letter_count = {}
    for char in text.lower():
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
    
    print("Letter frequency:")
    for letter, count in sorted(letter_count.items()):
        print(f"  {letter}: {count}")
    
    # Vowel count
    vowels = "aeiou"
    vowel_count = sum(1 for char in text.lower() if char in vowels)
    print(f"Vowel count: {vowel_count}")
    
    # Most common letter
    if letter_count:
        most_common = max(letter_count, key=letter_count.get)
        print(f"Most common letter: {most_common}")

# Test text analyzer
analyze_text("Hello, World!")
analyze_text("Python Programming is awesome!")

# Example 2: Password strength checker
def check_password_strength(password):
    """Check password strength"""
    print(f"Password: '{password}'")
    
    # Check length
    length_ok = len(password) >= 8
    print(f"Length >= 8: {length_ok}")
    
    # Check for uppercase
    has_upper = any(c.isupper() for c in password)
    print(f"Has uppercase: {has_upper}")
    
    # Check for lowercase
    has_lower = any(c.islower() for c in password)
    print(f"Has lowercase: {has_lower}")
    
    # Check for digits
    has_digit = any(c.isdigit() for c in password)
    print(f"Has digits: {has_digit}")
    
    # Check for special characters
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    has_special = any(c in special_chars for c in password)
    print(f"Has special chars: {has_special}")
    
    # Calculate strength
    strength_score = sum([length_ok, has_upper, has_lower, has_digit, has_special])
    
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score >= 3:
        strength = "Strong"
    elif strength_score >= 2:
        strength = "Medium"
    else:
        strength = "Weak"
    
    print(f"Password strength: {strength}")
    return strength

# Test password strength
passwords = ["password", "Password", "Password123", "P@ssw0rd!", "MyP@ssw0rd123!"]
for pwd in passwords:
    check_password_strength(pwd)
    print()

# Example 3: Text formatter
def format_text(text, width=50):
    """Format text to specified width"""
    words = text.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line + " " + word) <= width:
            if current_line:
                current_line += " " + word
            else:
                current_line = word
        else:
            if current_line:
                lines.append(current_line)
                current_line = word
            else:
                lines.append(word)
    
    if current_line:
        lines.append(current_line)
    
    return "\n".join(lines)

# Test text formatter
long_text = "This is a very long text that needs to be formatted to fit within a specific width. It should wrap to multiple lines when necessary."
formatted = format_text(long_text, 30)
print("Formatted text:")
print(formatted)

print("\n=== STRING ENCODING ===")

# String encoding and decoding
text = "Hello, 世界!"  # Text with Unicode characters
print(f"Original text: {text}")

# Encode to bytes
encoded = text.encode('utf-8')
print(f"Encoded (UTF-8): {encoded}")

# Decode back to string
decoded = encoded.decode('utf-8')
print(f"Decoded: {decoded}")

# Different encodings
try:
    encoded_latin = text.encode('latin-1')
    print(f"Encoded (Latin-1): {encoded_latin}")
except UnicodeEncodeError:
    print("Cannot encode to Latin-1 (contains non-Latin characters)")

print("\n=== STRING BEST PRACTICES ===")

print("""
String Best Practices:
1. Use f-strings for formatting (modern way)
2. Use raw strings for file paths
3. Use triple quotes for multi-line strings
4. Handle encoding properly for international text
5. Use string methods instead of manual manipulation
6. Validate input strings before processing
7. Use meaningful variable names
8. Consider performance for large strings
9. Use string constants for repeated values
10. Test with edge cases (empty strings, special characters)
""")

# Example of good string practices
def process_user_input(user_input):
    """Process user input with proper validation"""
    if not user_input:
        return "No input provided"
    
    # Clean and validate input
    cleaned_input = user_input.strip()
    if not cleaned_input:
        return "Input is empty after cleaning"
    
    # Process the input
    word_count = len(cleaned_input.split())
    char_count = len(cleaned_input)
    
    return f"Processed: '{cleaned_input}' ({word_count} words, {char_count} characters)"

# Test input processing
test_inputs = ["  Hello, World!  ", "", "   ", "Python Programming"]
for inp in test_inputs:
    result = process_user_input(inp)
    print(f"Input: '{inp}' -> {result}")

"""
Key Points to Remember:
1. Strings are immutable (can't be changed directly)
2. Use indexing and slicing to access characters
3. Use string methods for manipulation
4. Use f-strings for formatting (recommended)
5. Use split() and join() for list conversion
6. Validate strings before processing
7. Handle encoding for international text
8. Use raw strings for file paths
9. Practice with real-world examples
10. Test edge cases and special characters
"""
