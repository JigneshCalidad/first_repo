"""
🔧 FUNCTIONS - Advanced Functions
================================

Advanced function concepts including lambda functions, decorators,
and function composition. Level up your function skills! 🚀
"""

print("=== LAMBDA FUNCTIONS ===")

# Lambda functions are anonymous (unnamed) functions
# They're useful for simple operations

# Basic lambda function
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple parameters
add = lambda x, y: x + y
print(f"5 + 3 = {add(5, 3)}")

# Lambda with conditional
is_even = lambda x: x % 2 == 0
print(f"Is 4 even? {is_even(4)}")
print(f"Is 5 even? {is_even(5)}")

# Lambda with string operations
get_first_letter = lambda word: word[0].upper()
print(f"First letter of 'hello': {get_first_letter('hello')}")

print("\n=== LAMBDA WITH BUILT-IN FUNCTIONS ===")

# Lambda with map() - apply function to each item
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared}")

# Lambda with filter() - filter items based on condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Lambda with sorted() - custom sorting
names = ["Alice", "Bob", "Charlie", "David"]
sorted_by_length = sorted(names, key=lambda x: len(x))
print(f"Names sorted by length: {sorted_by_length}")

# Lambda with reduce() - accumulate values
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"Product of numbers: {product}")

print("\n=== HIGHER-ORDER FUNCTIONS ===")

# Functions that take other functions as parameters
def apply_operation(numbers, operation):
    """Apply operation to each number"""
    results = []
    for num in numbers:
        results.append(operation(num))
    return results

# Test with different operations
numbers = [1, 2, 3, 4, 5]
print(f"Original numbers: {numbers}")

# Square each number
squared = apply_operation(numbers, lambda x: x ** 2)
print(f"Squared: {squared}")

# Double each number
doubled = apply_operation(numbers, lambda x: x * 2)
print(f"Doubled: {doubled}")

# Convert to string
strings = apply_operation(numbers, lambda x: f"Number: {x}")
print(f"Strings: {strings}")

print("\n=== FUNCTION COMPOSITION ===")

# Compose multiple functions
def compose(f, g):
    """Compose two functions: f(g(x))"""
    return lambda x: f(g(x))

# Example: square then double
square = lambda x: x ** 2
double = lambda x: x * 2
square_then_double = compose(double, square)

print(f"Square then double 3: {square_then_double(3)}")  # (3^2) * 2 = 18

# Multiple composition
def compose_multiple(*functions):
    """Compose multiple functions"""
    def composed(x):
        result = x
        for func in reversed(functions):
            result = func(result)
        return result
    return composed

# Example: add 1, square, then double
add_one = lambda x: x + 1
square = lambda x: x ** 2
double = lambda x: x * 2

complex_operation = compose_multiple(add_one, square, double)
print(f"Add 1, square, double 2: {complex_operation(2)}")  # ((2+1)^2) * 2 = 18

print("\n=== CLOSURES ===")

# Closures - functions that remember their environment
def create_multiplier(factor):
    """Create a function that multiplies by factor"""
    def multiplier(number):
        return number * factor
    return multiplier

# Create different multipliers
double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

print(f"Double 5: {double(5)}")
print(f"Triple 5: {triple(5)}")
print(f"Quadruple 5: {quadruple(5)}")

# Counter closure
def create_counter():
    """Create a counter that remembers its state"""
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

# Test counter
counter1 = create_counter()
counter2 = create_counter()

print(f"Counter 1: {counter1()}, {counter1()}, {counter1()}")
print(f"Counter 2: {counter2()}, {counter2()}")

print("\n=== DECORATORS ===")

# Decorators - functions that modify other functions
def timing_decorator(func):
    """Decorator to measure function execution time"""
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Use decorator
@timing_decorator
def slow_function():
    """Function that takes time to execute"""
    import time
    time.sleep(0.1)  # Simulate slow operation
    return "Done!"

# Test decorator
result = slow_function()
print(f"Result: {result}")

# Logging decorator
def log_calls(func):
    """Decorator to log function calls"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_calls
def add_numbers(a, b):
    """Add two numbers"""
    return a + b

# Test logging decorator
result = add_numbers(3, 5)
print(f"Final result: {result}")

print("\n=== GENERATOR FUNCTIONS ===")

# Generator functions - functions that yield values
def fibonacci_generator(n):
    """Generate Fibonacci numbers up to n"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Use generator
print("Fibonacci numbers:")
for num in fibonacci_generator(10):
    print(f"  {num}")

# Generator with yield from
def flatten_list(nested_list):
    """Flatten a nested list"""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_list(item)
        else:
            yield item

# Test flattening
nested = [1, [2, 3], [4, [5, 6]], 7]
flattened = list(flatten_list(nested))
print(f"Nested: {nested}")
print(f"Flattened: {flattened}")

print("\n=== RECURSIVE FUNCTIONS ===")

# Recursive functions - functions that call themselves
def factorial(n):
    """Calculate factorial recursively"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Test factorial
for i in range(1, 6):
    print(f"Factorial of {i}: {factorial(i)}")

# Fibonacci recursively
def fibonacci_recursive(n):
    """Calculate Fibonacci number recursively"""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Test Fibonacci
print("Fibonacci sequence:")
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")

# Recursive list processing
def count_items(lst):
    """Count items in nested list recursively"""
    count = 0
    for item in lst:
        if isinstance(item, list):
            count += count_items(item)
        else:
            count += 1
    return count

# Test counting
nested_list = [1, [2, 3], [4, [5, 6]], 7]
item_count = count_items(nested_list)
print(f"Items in {nested_list}: {item_count}")

print("\n=== FUNCTION ARGUMENTS ===")

# *args - variable number of positional arguments
def sum_all(*args):
    """Sum all arguments"""
    return sum(args)

print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")

# **kwargs - variable number of keyword arguments
def print_info(**kwargs):
    """Print information from keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")

# Combined args and kwargs
def flexible_function(*args, **kwargs):
    """Function that accepts both args and kwargs"""
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

flexible_function(1, 2, 3, name="Alice", age=25)

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Data processing pipeline
def process_data(data, *processors):
    """Process data through multiple functions"""
    result = data
    for processor in processors:
        result = processor(result)
    return result

# Define processors
def filter_positive(numbers):
    return [x for x in numbers if x > 0]

def square_numbers(numbers):
    return [x ** 2 for x in numbers]

def sum_numbers(numbers):
    return sum(numbers)

# Test pipeline
data = [-2, -1, 0, 1, 2, 3, 4, 5]
result = process_data(data, filter_positive, square_numbers, sum_numbers)
print(f"Original data: {data}")
print(f"Processed result: {result}")

# Example 2: Function memoization
def memoize(func):
    """Memoization decorator"""
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci_memoized(n):
    """Memoized Fibonacci function"""
    if n <= 1:
        return n
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)

# Test memoization
import time

start = time.time()
result = fibonacci_memoized(30)
end = time.time()
print(f"Fibonacci(30) = {result} (took {end - start:.4f} seconds)")

print("\n=== FUNCTION BEST PRACTICES ===")

print("""
Advanced Function Best Practices:
1. Use lambda for simple, one-line functions
2. Use closures for stateful functions
3. Use decorators for cross-cutting concerns
4. Use generators for memory-efficient iteration
5. Use recursion for tree-like structures
6. Use *args and **kwargs for flexible functions
7. Use memoization for expensive computations
8. Keep functions pure when possible
9. Use type hints for better documentation
10. Test edge cases and error conditions
""")

"""
Key Points to Remember:
1. Lambda functions are anonymous and concise
2. Closures remember their environment
3. Decorators modify function behavior
4. Generators yield values one at a time
5. Recursion calls the function itself
6. *args handles variable positional arguments
7. **kwargs handles variable keyword arguments
8. Use memoization for expensive computations
9. Practice with real-world examples
10. Understand when to use each pattern
"""
