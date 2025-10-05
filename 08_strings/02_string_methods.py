"""
📝 STRINGS - String Methods
==========================

Python provides many built-in string methods for common operations.
Learn how to use them effectively! 🛠️
"""

print("=== CASE CONVERSION METHODS ===")

# Case conversion methods
text = "  Hello, World!  "
print(f"Original: '{text}'")

# Upper case
print(f"Upper: {text.upper()}")

# Lower case
print(f"Lower: {text.lower()}")

# Title case (first letter of each word capitalized)
print(f"Title: {text.title()}")

# Capitalize (first letter of string capitalized)
print(f"Capitalize: {text.capitalize()}")

# Swap case (swap upper and lower case)
print(f"Swap case: {text.swapcase()}")

# Case folding (for case-insensitive comparison)
print(f"Case fold: {text.casefold()}")

print("\n=== WHITESPACE METHODS ===")

# Whitespace methods
text = "  \t  Hello, World!  \n  "
print(f"Original: '{text}'")

# Strip whitespace from both ends
print(f"Strip: '{text.strip()}'")

# Strip from left end
print(f"Left strip: '{text.lstrip()}'")

# Strip from right end
print(f"Right strip: '{text.rstrip()}'")

# Strip specific characters
text_with_chars = "***Hello, World!***"
print(f"Strip '*': '{text_with_chars.strip('*')}'")

print("\n=== SEARCH METHODS ===")

# Search methods
text = "Python is awesome and Python is fun"
print(f"Text: {text}")

# Find first occurrence
print(f"Find 'Python': {text.find('Python')}")
print(f"Find 'Java': {text.find('Java')}")  # Returns -1 if not found

# Find last occurrence
print(f"Rfind 'Python': {text.rfind('Python')}")

# Find with start and end positions
print(f"Find 'is' from position 10: {text.find('is', 10)}")

# Count occurrences
print(f"Count 'Python': {text.count('Python')}")
print(f"Count 'is': {text.count('is')}")

# Check if string starts with prefix
print(f"Starts with 'Python': {text.startswith('Python')}")
print(f"Starts with 'Java': {text.startswith('Java')}")

# Check if string ends with suffix
print(f"Ends with 'fun': {text.endswith('fun')}")
print(f"Ends with 'awesome': {text.endswith('awesome')}")

# Check if string contains substring
print(f"Contains 'awesome': {'awesome' in text}")
print(f"Contains 'Java': {'Java' in text}")

print("\n=== REPLACEMENT METHODS ===")

# Replacement methods
text = "Hello, World! Hello, Python!"
print(f"Original: {text}")

# Replace all occurrences
new_text = text.replace("Hello", "Hi")
print(f"Replace 'Hello' with 'Hi': {new_text}")

# Replace with count limit
new_text = text.replace("Hello", "Hi", 1)
print(f"Replace first 'Hello' with 'Hi': {new_text}")

# Replace multiple characters
text = "Hello, World!"
new_text = text.replace("l", "L")
print(f"Replace 'l' with 'L': {new_text}")

# Replace with empty string (remove)
new_text = text.replace(", ", "")
print(f"Remove ', ': {new_text}")

print("\n=== SPLITTING AND JOINING ===")

# Splitting methods
text = "apple,banana,cherry,date"
print(f"Original: {text}")

# Split by comma
fruits = text.split(",")
print(f"Split by ',': {fruits}")

# Split with max splits
fruits = text.split(",", 2)
print(f"Split with max 2: {fruits}")

# Split by spaces
text = "Python is awesome"
words = text.split()
print(f"Split by spaces: {words}")

# Split by multiple delimiters
text = "apple,banana;cherry:date"
import re
fruits = re.split("[,;:]", text)
print(f"Split by multiple delimiters: {fruits}")

# Join methods
fruits = ["apple", "banana", "cherry"]
print(f"Fruits list: {fruits}")

# Join with comma
joined = ",".join(fruits)
print(f"Joined with ',': {joined}")

# Join with space
joined = " ".join(fruits)
print(f"Joined with space: {joined}")

# Join with custom separator
joined = " -> ".join(fruits)
print(f"Joined with ' -> ': {joined}")

print("\n=== VALIDATION METHODS ===")

# Validation methods
def test_validation(text, label):
    """Test various validation methods"""
    print(f"{label}: '{text}'")
    print(f"  isalpha(): {text.isalpha()}")
    print(f"  isdigit(): {text.isdigit()}")
    print(f"  isalnum(): {text.isalnum()}")
    print(f"  isspace(): {text.isspace()}")
    print(f"  islower(): {text.islower()}")
    print(f"  isupper(): {text.isupper()}")
    print(f"  istitle(): {text.istitle()}")
    print()

# Test different strings
test_validation("Hello", "Letters only")
test_validation("123", "Digits only")
test_validation("Hello123", "Letters and digits")
test_validation("   ", "Spaces only")
test_validation("hello", "Lowercase")
test_validation("HELLO", "Uppercase")
test_validation("Hello World", "Title case")

print("\n=== ALIGNMENT METHODS ===")

# Alignment methods
text = "Hello"
print(f"Original: '{text}'")

# Center alignment
print(f"Center (width 20): '{text.center(20)}'")
print(f"Center with '*': '{text.center(20, '*')}'")

# Left alignment
print(f"Left (width 20): '{text.ljust(20)}'")
print(f"Left with '*': '{text.ljust(20, '*')}'")

# Right alignment
print(f"Right (width 20): '{text.rjust(20)}'")
print(f"Right with '*': '{text.rjust(20, '*')}'")

# Zero padding
number = "42"
print(f"Zero pad (width 5): '{number.zfill(5)}'")

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Text cleaner
def clean_text(text):
    """Clean and normalize text"""
    # Remove extra whitespace
    cleaned = text.strip()
    
    # Replace multiple spaces with single space
    import re
    cleaned = re.sub(r'\s+', ' ', cleaned)
    
    # Capitalize first letter
    cleaned = cleaned.capitalize()
    
    return cleaned

# Test text cleaner
dirty_text = "  hello    world   python  "
cleaned = clean_text(dirty_text)
print(f"Original: '{dirty_text}'")
print(f"Cleaned: '{cleaned}'")

# Example 2: Word counter
def count_words(text):
    """Count words in text"""
    if not text.strip():
        return 0
    
    words = text.split()
    return len(words)

# Test word counter
texts = [
    "Hello, World!",
    "Python is awesome",
    "   ",  # Empty after strip
    "One two three four five"
]

for text in texts:
    count = count_words(text)
    print(f"Text: '{text}' -> {count} words")

# Example 3: Email validator
def validate_email(email):
    """Basic email validation"""
    if not email or not email.strip():
        return False, "Email is empty"
    
    email = email.strip().lower()
    
    # Check for @ symbol
    if "@" not in email:
        return False, "Email must contain @"
    
    # Split by @
    parts = email.split("@")
    if len(parts) != 2:
        return False, "Email must have exactly one @"
    
    local, domain = parts
    
    # Check local part
    if not local or not local.isalnum():
        return False, "Local part must be alphanumeric"
    
    # Check domain part
    if not domain or "." not in domain:
        return False, "Domain must contain a dot"
    
    return True, "Valid email"

# Test email validation
emails = [
    "user@example.com",
    "invalid-email",
    "user@domain",
    "user@domain.com",
    "  USER@EXAMPLE.COM  "  # Should be normalized
]

for email in emails:
    is_valid, message = validate_email(email)
    print(f"Email: '{email}' -> {message}")

# Example 4: Text formatter
def format_paragraph(text, width=50):
    """Format text into paragraphs"""
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

# Test paragraph formatter
long_text = "This is a very long text that needs to be formatted into paragraphs. It should wrap to multiple lines when the text exceeds the specified width."
formatted = format_paragraph(long_text, 30)
print("Formatted paragraph:")
print(formatted)

print("\n=== STRING METHOD CHAINING ===")

# Method chaining
text = "  Hello, World!  "
print(f"Original: '{text}'")

# Chain multiple methods
result = text.strip().lower().replace("world", "python").title()
print(f"Chained methods: '{result}'")

# Complex chaining example
def process_text(text):
    """Process text with method chaining"""
    return (text.strip()
            .lower()
            .replace("  ", " ")  # Replace double spaces
            .capitalize())

# Test method chaining
test_texts = [
    "  HELLO    WORLD  ",
    "  python   programming  ",
    "  HELLO    PYTHON  "
]

for text in test_texts:
    processed = process_text(text)
    print(f"'{text}' -> '{processed}'")

print("\n=== STRING METHOD BEST PRACTICES ===")

print("""
String Method Best Practices:
1. Use strip() to clean user input
2. Use lower() for case-insensitive comparison
3. Use replace() to clean data
4. Use split() and join() for list conversion
5. Use startswith() and endswith() for validation
6. Use find() instead of index() to avoid exceptions
7. Use count() to count occurrences
8. Chain methods for complex transformations
9. Test with edge cases (empty strings, special characters)
10. Consider performance for large strings
""")

# Example of good string method usage
def process_user_data(name, email, phone):
    """Process user data with proper validation"""
    # Clean name
    name = name.strip().title()
    
    # Clean email
    email = email.strip().lower()
    
    # Clean phone (remove non-digits)
    phone = ''.join(filter(str.isdigit, phone))
    
    # Validate
    if not name:
        return False, "Name is required"
    
    if not email or "@" not in email:
        return False, "Valid email is required"
    
    if not phone or len(phone) < 10:
        return False, "Valid phone number is required"
    
    return True, f"Processed: {name}, {email}, {phone}"

# Test user data processing
test_cases = [
    ("  john doe  ", "JOHN@EXAMPLE.COM", "123-456-7890"),
    ("", "invalid-email", "123"),
    ("  jane smith  ", "jane@example.com", "987-654-3210")
]

for name, email, phone in test_cases:
    is_valid, result = process_user_data(name, email, phone)
    print(f"Input: {name}, {email}, {phone}")
    print(f"Result: {result}")
    print()

"""
Key Points to Remember:
1. String methods return new strings (strings are immutable)
2. Use strip() to clean whitespace
3. Use lower() for case-insensitive operations
4. Use replace() to modify text
5. Use split() and join() for list conversion
6. Use validation methods to check string properties
7. Chain methods for complex transformations
8. Test with edge cases and special characters
9. Consider performance for large strings
10. Practice with real-world examples
"""
