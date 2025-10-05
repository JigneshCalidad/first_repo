"""
📋 LISTS - List Comprehension
============================

List comprehension is a concise way to create lists.
It's like a for loop in a single line! 🚀
"""

print("=== BASIC LIST COMPREHENSION ===")

# Basic syntax: [expression for item in iterable]
numbers = [1, 2, 3, 4, 5]
print(f"Original numbers: {numbers}")

# Square each number
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

# Double each number
doubles = [x * 2 for x in numbers]
print(f"Doubles: {doubles}")

# Convert to string
strings = [str(x) for x in numbers]
print(f"Strings: {strings}")

# Transform strings
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"Upper case: {upper_words}")

print("\n=== LIST COMPREHENSION WITH CONDITIONS ===")

# Filter with condition: [expression for item in iterable if condition]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original numbers: {numbers}")

# Filter even numbers
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

# Filter odd numbers
odds = [x for x in numbers if x % 2 != 0]
print(f"Odd numbers: {odds}")

# Filter numbers greater than 5
greater_than_5 = [x for x in numbers if x > 5]
print(f"Greater than 5: {greater_than_5}")

# Filter strings by length
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = [word for word in words if len(word) > 5]
print(f"Long words: {long_words}")

print("\n=== CONDITIONAL EXPRESSIONS IN COMPREHENSION ===")

# Conditional expressions: [expression1 if condition else expression2 for item in iterable]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original numbers: {numbers}")

# Even or odd
even_odd = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(f"Even/Odd: {even_odd}")

# Square even numbers, double odd numbers
transformed = [x**2 if x % 2 == 0 else x * 2 for x in numbers]
print(f"Transformed: {transformed}")

# Grade classification
scores = [85, 92, 78, 96, 88, 91, 83, 89, 94, 87]
grades = ["A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F" for score in scores]
print(f"Scores: {scores}")
print(f"Grades: {grades}")

print("\n=== NESTED LIST COMPREHENSION ===")

# Nested comprehension: [expression for sublist in list for item in sublist]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matrix: {matrix}")

# Flatten matrix
flattened = [num for row in matrix for num in row]
print(f"Flattened: {flattened}")

# Square each element in matrix
squared_matrix = [[num**2 for num in row] for row in matrix]
print(f"Squared matrix: {squared_matrix}")

# Filter and flatten
even_numbers = [num for row in matrix for num in row if num % 2 == 0]
print(f"Even numbers: {even_numbers}")

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Data processing
def process_scores(scores):
    """Process scores with list comprehension"""
    # Filter valid scores (0-100)
    valid_scores = [score for score in scores if 0 <= score <= 100]
    
    # Calculate grades
    grades = ["A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F" for score in valid_scores]
    
    # Create grade report
    report = [f"{score}: {grade}" for score, grade in zip(valid_scores, grades)]
    
    return valid_scores, grades, report

# Test score processing
scores = [85, 92, 78, 96, 88, 91, 83, 89, 94, 87, -5, 105]
valid, grades, report = process_scores(scores)
print(f"Valid scores: {valid}")
print(f"Grades: {grades}")
print("Report:")
for item in report:
    print(f"  {item}")

# Example 2: Text processing
def process_text(text):
    """Process text with list comprehension"""
    # Split into words
    words = text.split()
    
    # Filter words longer than 3 characters
    long_words = [word for word in words if len(word) > 3]
    
    # Convert to uppercase
    upper_words = [word.upper() for word in long_words]
    
    # Remove punctuation
    clean_words = [word.strip(".,!?") for word in upper_words]
    
    return words, long_words, upper_words, clean_words

# Test text processing
text = "Hello, World! Python is awesome and fun to learn."
words, long_words, upper_words, clean_words = process_text(text)
print(f"Original text: {text}")
print(f"All words: {words}")
print(f"Long words: {long_words}")
print(f"Upper case: {upper_words}")
print(f"Clean words: {clean_words}")

# Example 3: Matrix operations
def matrix_operations(matrix):
    """Perform matrix operations with list comprehension"""
    # Transpose matrix
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    
    # Sum of each row
    row_sums = [sum(row) for row in matrix]
    
    # Sum of each column
    col_sums = [sum(col) for col in transposed]
    
    # Find maximum in each row
    row_maxs = [max(row) for row in matrix]
    
    # Find maximum in each column
    col_maxs = [max(col) for col in transposed]
    
    return transposed, row_sums, col_sums, row_maxs, col_maxs

# Test matrix operations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed, row_sums, col_sums, row_maxs, col_maxs = matrix_operations(matrix)
print(f"Original matrix: {matrix}")
print(f"Transposed: {transposed}")
print(f"Row sums: {row_sums}")
print(f"Column sums: {col_sums}")
print(f"Row maximums: {row_maxs}")
print(f"Column maximums: {col_maxs}")

print("\n=== ADVANCED LIST COMPREHENSION ===")

# Multiple conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original numbers: {numbers}")

# Multiple conditions with and
even_greater_than_5 = [x for x in numbers if x % 2 == 0 and x > 5]
print(f"Even and greater than 5: {even_greater_than_5}")

# Multiple conditions with or
divisible_by_3_or_5 = [x for x in numbers if x % 3 == 0 or x % 5 == 0]
print(f"Divisible by 3 or 5: {divisible_by_3_or_5}")

# Complex conditions
complex_filter = [x for x in numbers if x > 3 and x < 8 and x % 2 == 0]
print(f"Complex filter: {complex_filter}")

# Multiple expressions
numbers = [1, 2, 3, 4, 5]
results = [x**2 if x % 2 == 0 else x*3 for x in numbers]
print(f"Square if even, triple if odd: {results}")

print("\n=== LIST COMPREHENSION VS LOOPS ===")

# Traditional loop approach
def traditional_approach(numbers):
    """Traditional loop approach"""
    squares = []
    for x in numbers:
        squares.append(x**2)
    return squares

# List comprehension approach
def comprehension_approach(numbers):
    """List comprehension approach"""
    return [x**2 for x in numbers]

# Test both approaches
numbers = [1, 2, 3, 4, 5]
traditional_result = traditional_approach(numbers)
comprehension_result = comprehension_approach(numbers)
print(f"Traditional: {traditional_result}")
print(f"Comprehension: {comprehension_result}")

# Performance comparison (conceptual)
import time

def time_comparison():
    """Compare performance of traditional vs comprehension"""
    numbers = list(range(1000))
    
    # Traditional approach
    start = time.time()
    traditional_result = []
    for x in numbers:
        traditional_result.append(x**2)
    traditional_time = time.time() - start
    
    # Comprehension approach
    start = time.time()
    comprehension_result = [x**2 for x in numbers]
    comprehension_time = time.time() - start
    
    print(f"Traditional time: {traditional_time:.6f}s")
    print(f"Comprehension time: {comprehension_time:.6f}s")
    print(f"Results equal: {traditional_result == comprehension_result}")

# Run performance comparison
time_comparison()

print("\n=== LIST COMPREHENSION BEST PRACTICES ===")

print("""
List Comprehension Best Practices:
1. Use for simple transformations and filtering
2. Keep expressions simple and readable
3. Avoid complex nested comprehensions
4. Use meaningful variable names
5. Consider readability over brevity
6. Use traditional loops for complex logic
7. Test with edge cases
8. Consider performance for large datasets
9. Use parentheses for complex expressions
10. Document complex comprehensions
""")

# Example of good vs bad comprehension
def good_comprehension_example():
    """Example of good list comprehension"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Good: Simple and readable
    even_squares = [x**2 for x in numbers if x % 2 == 0]
    print(f"Even squares: {even_squares}")
    
    # Good: Clear variable names
    student_scores = [85, 92, 78, 96, 88]
    passing_grades = [score for score in student_scores if score >= 80]
    print(f"Passing grades: {passing_grades}")

def bad_comprehension_example():
    """Example of bad list comprehension (too complex)"""
    # Bad: Too complex, hard to read
    # complex_result = [x**2 if x % 2 == 0 else x*3 if x > 5 else x for x in numbers if x > 0 and x < 100]
    
    # Better: Break into steps
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Step 1: Filter
    filtered = [x for x in numbers if x > 0 and x < 100]
    
    # Step 2: Transform
    transformed = [x**2 if x % 2 == 0 else x*3 for x in filtered]
    
    print(f"Filtered: {filtered}")
    print(f"Transformed: {transformed}")

# Test examples
good_comprehension_example()
print()
bad_comprehension_example()

"""
Key Points to Remember:
1. List comprehension is concise and readable
2. Syntax: [expression for item in iterable if condition]
3. Use for simple transformations and filtering
4. Avoid complex nested comprehensions
5. Consider readability over brevity
6. Use traditional loops for complex logic
7. Test with edge cases
8. Practice with real-world examples
9. Understand when to use vs when not to use
10. Master the syntax and patterns
"""
