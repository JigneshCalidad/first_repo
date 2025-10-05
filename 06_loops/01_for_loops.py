"""
🔄 LOOPS - For Loops
===================

For loops let you repeat code for each item in a sequence.
They're perfect for processing lists, strings, and ranges! 🔁
"""

print("=== BASIC FOR LOOPS ===")

# Loop through a list
fruits = ["apple", "banana", "cherry"]
print("Fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# Loop through a string
word = "Python"
print(f"\nLetters in '{word}':")
for letter in word:
    print(f"  {letter}")

# Loop through a range
print("\nNumbers 1 to 5:")
for i in range(1, 6):
    print(f"  {i}")

print("\n=== RANGE FUNCTION ===")

# Different range patterns
print("Range(5):", list(range(5)))           # 0 to 4
print("Range(1, 6):", list(range(1, 6)))     # 1 to 5
print("Range(0, 10, 2):", list(range(0, 10, 2)))  # 0, 2, 4, 6, 8

# Countdown
print("Countdown from 5:")
for i in range(5, 0, -1):
    print(f"  {i}...")
print("  Blast off! 🚀")

# Even numbers
print("\nEven numbers from 0 to 10:")
for i in range(0, 11, 2):
    print(f"  {i}")

print("\n=== LOOPING WITH INDEX ===")

# Using enumerate to get both index and value
fruits = ["apple", "banana", "cherry"]
print("Fruits with index:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# Start enumeration from 1
print("\nFruits with index starting from 1:")
for index, fruit in enumerate(fruits, 1):
    print(f"  {index}: {fruit}")

# Manual index tracking
print("\nManual index tracking:")
for i in range(len(fruits)):
    print(f"  {i}: {fruits[i]}")

print("\n=== NESTED FOR LOOPS ===")

# Multiplication table
print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"  {i} × {j} = {result}")

# Pattern printing
print("\nStar pattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()  # New line after each row

print("\n=== LOOP CONTROL STATEMENTS ===")

# Break - exit loop early
print("Numbers 1 to 10 (break at 5):")
for i in range(1, 11):
    if i == 5:
        break
    print(f"  {i}")

# Continue - skip current iteration
print("\nNumbers 1 to 10 (skip 5):")
for i in range(1, 11):
    if i == 5:
        continue
    print(f"  {i}")

# Pass - do nothing (placeholder)
print("\nNumbers 1 to 10 (pass at 5):")
for i in range(1, 11):
    if i == 5:
        pass  # Do nothing
    print(f"  {i}")

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Shopping list processor
def process_shopping_list(items, prices):
    """Process shopping list with prices"""
    total = 0
    print("Shopping List:")
    print("-" * 30)
    
    for i, (item, price) in enumerate(zip(items, prices), 1):
        print(f"{i}. {item}: ${price:.2f}")
        total += price
    
    print("-" * 30)
    print(f"Total: ${total:.2f}")
    return total

# Test shopping list
items = ["bread", "milk", "eggs", "cheese"]
prices = [2.50, 3.00, 4.50, 5.25]
process_shopping_list(items, prices)

# Example 2: Grade calculator
def calculate_grades(student_scores):
    """Calculate and display grades"""
    print("\nGrade Report:")
    print("-" * 40)
    
    total = 0
    for student, score in student_scores.items():
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        
        print(f"{student}: {score} ({grade})")
        total += score
    
    average = total / len(student_scores)
    print("-" * 40)
    print(f"Average: {average:.1f}")

# Test grade calculator
scores = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 76,
    "Diana": 92,
    "Eve": 68
}
calculate_grades(scores)

# Example 3: Text analyzer
def analyze_text(text):
    """Analyze text for various statistics"""
    print(f"\nText Analysis for: '{text}'")
    print("-" * 40)
    
    # Character count
    char_count = len(text)
    print(f"Character count: {char_count}")
    
    # Word count
    words = text.split()
    word_count = len(words)
    print(f"Word count: {word_count}")
    
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

# Test text analyzer
analyze_text("Hello, World!")
analyze_text("Python Programming")

print("\n=== LOOPING THROUGH DIFFERENT DATA TYPES ===")

# List of dictionaries
students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 19, "grade": "B"},
    {"name": "Charlie", "age": 21, "grade": "C"}
]

print("Student Information:")
for student in students:
    print(f"  {student['name']}: Age {student['age']}, Grade {student['grade']}")

# List of tuples
coordinates = [(1, 2), (3, 4), (5, 6)]
print("\nCoordinates:")
for x, y in coordinates:
    print(f"  ({x}, {y})")

# Dictionary iteration
person = {"name": "John", "age": 30, "city": "New York"}
print("\nPerson details:")
for key, value in person.items():
    print(f"  {key}: {value}")

print("\n=== ADVANCED FOR LOOP PATTERNS ===")

# Pattern 1: Finding items
def find_item(items, target):
    """Find item in list with index"""
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1

# Test finding items
numbers = [1, 3, 5, 7, 9]
target = 5
index = find_item(numbers, target)
print(f"Found {target} at index {index}")

# Pattern 2: Filtering items
def filter_even_numbers(numbers):
    """Filter even numbers from list"""
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# Test filtering
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = filter_even_numbers(numbers)
print(f"Even numbers from {numbers}: {even_nums}")

# Pattern 3: Transforming items
def square_numbers(numbers):
    """Square each number in list"""
    squared = []
    for num in numbers:
        squared.append(num ** 2)
    return squared

# Test transformation
numbers = [1, 2, 3, 4, 5]
squared = square_numbers(numbers)
print(f"Squared {numbers}: {squared}")

print("\n=== FOR LOOP BEST PRACTICES ===")

print("""
For Loop Best Practices:
1. Use descriptive variable names
2. Use enumerate() when you need both index and value
3. Use range() for numeric sequences
4. Use break and continue judiciously
5. Avoid modifying the list you're iterating over
6. Use list comprehensions for simple transformations
7. Keep loop bodies small and focused
8. Use meaningful loop variable names
9. Consider using zip() for parallel iteration
10. Test edge cases (empty lists, single items)
""")

# Example of good practices
def process_data(data):
    """Example of good for loop practices"""
    if not data:  # Handle empty data
        print("No data to process")
        return
    
    print(f"Processing {len(data)} items:")
    for i, item in enumerate(data, 1):
        if item is None:  # Handle None values
            print(f"  {i}. Skipping None value")
            continue
        
        print(f"  {i}. Processing: {item}")

# Test with different data
process_data([1, 2, 3, None, 5])
process_data([])
process_data(["a", "b", "c"])

"""
Key Points to Remember:
1. For loops iterate over sequences (lists, strings, ranges)
2. Use range() for numeric sequences
3. Use enumerate() to get both index and value
4. Use break to exit loop early
5. Use continue to skip current iteration
6. Use pass as a placeholder
7. Avoid modifying lists while iterating
8. Use descriptive variable names
9. Handle edge cases (empty sequences)
10. Practice with real-world examples
"""
