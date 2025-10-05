"""
📋 LISTS - List Operations
========================

Lists are ordered collections of items. Learn how to create,
manipulate, and work with lists effectively! 🗂️
"""

print("=== CREATING LISTS ===")

# Different ways to create lists
empty_list = []
print(f"Empty list: {empty_list}")

# List with numbers
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# List with strings
fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")

# Mixed data types
mixed = [1, "hello", 3.14, True, [1, 2, 3]]
print(f"Mixed types: {mixed}")

# List with duplicates
scores = [85, 90, 85, 78, 90]
print(f"Scores with duplicates: {scores}")

# List from range
range_list = list(range(1, 6))
print(f"From range: {range_list}")

# List from string
string_list = list("Hello")
print(f"From string: {string_list}")

print("\n=== LIST INDEXING AND SLICING ===")

# List indexing
colors = ["red", "green", "blue", "yellow", "purple"]
print(f"Colors: {colors}")

print(f"First color: {colors[0]}")
print(f"Second color: {colors[1]}")
print(f"Last color: {colors[-1]}")
print(f"Second to last: {colors[-2]}")

# List slicing
print(f"First 3 colors: {colors[0:3]}")
print(f"Colors 2-4: {colors[1:4]}")
print(f"Last 3 colors: {colors[-3:]}")
print(f"Every 2nd color: {colors[::2]}")
print(f"Reverse list: {colors[::-1]}")

# Step slicing
print(f"Every 3rd color: {colors[::3]}")

print("\n=== LIST METHODS - ADDING ELEMENTS ===")

# Adding elements
shopping = ["bread", "milk"]
print(f"Original: {shopping}")

# append() - add to end
shopping.append("eggs")
print(f"After append('eggs'): {shopping}")

# insert() - add at specific position
shopping.insert(1, "butter")
print(f"After insert(1, 'butter'): {shopping}")

# extend() - add multiple items
shopping.extend(["cheese", "yogurt"])
print(f"After extend(['cheese', 'yogurt']): {shopping}")

# + operator - create new list
new_items = ["cookies", "chocolate"]
combined = shopping + new_items
print(f"Combined lists: {combined}")

# += operator - modify existing list
shopping += new_items
print(f"After +=: {shopping}")

print("\n=== LIST METHODS - REMOVING ELEMENTS ===")

# Removing elements
numbers = [1, 2, 3, 2, 4, 2]
print(f"Original: {numbers}")

# remove() - remove first occurrence
numbers.remove(2)
print(f"After remove(2): {numbers}")

# pop() - remove and return element
last_item = numbers.pop()
print(f"Popped item: {last_item}")
print(f"After pop(): {numbers}")

# pop(index) - remove specific index
second_item = numbers.pop(1)
print(f"Popped item at index 1: {second_item}")
print(f"After pop(1): {numbers}")

# del - delete by index
del numbers[0]
print(f"After del numbers[0]: {numbers}")

# clear() - remove all elements
numbers.clear()
print(f"After clear(): {numbers}")

print("\n=== LIST METHODS - SEARCHING ===")

# Searching methods
fruits = ["apple", "banana", "cherry", "banana"]
print(f"Fruits: {fruits}")

# index() - find position of element
print(f"Index of 'banana': {fruits.index('banana')}")
print(f"Index of 'cherry': {fruits.index('cherry')}")

# count() - count occurrences
print(f"Count of 'banana': {fruits.count('banana')}")
print(f"Count of 'apple': {fruits.count('apple')}")

# in operator - check if element exists
print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")

# not in operator
print(f"'grape' not in fruits: {'grape' not in fruits}")

print("\n=== LIST METHODS - SORTING ===")

# Sorting methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")

# sort() - sort in place
numbers.sort()
print(f"Sorted: {numbers}")

# sort(reverse=True) - sort in descending order
numbers.sort(reverse=True)
print(f"Sorted reverse: {numbers}")

# sorted() - create new sorted list
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(f"Original: {original}")
print(f"Sorted copy: {sorted_list}")

# Sort strings
names = ["Charlie", "Alice", "Bob"]
names.sort()
print(f"Sorted names: {names}")

# Sort with custom key
words = ["apple", "banana", "cherry", "date"]
words.sort(key=len)  # Sort by length
print(f"Sorted by length: {words}")

print("\n=== LIST METHODS - OTHER ===")

# Other useful methods
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# reverse() - reverse list in place
numbers.reverse()
print(f"Reversed: {numbers}")

# len() - get length
print(f"Length: {len(numbers)}")

# max() and min()
scores = [85, 92, 78, 96, 88]
print(f"Scores: {scores}")
print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")
print(f"Sum: {sum(scores)}")
print(f"Average: {sum(scores) / len(scores):.1f}")

# any() and all()
boolean_list = [True, False, True]
print(f"Any true: {any(boolean_list)}")
print(f"All true: {all(boolean_list)}")

print("\n=== NESTED LISTS ===")

# Nested lists (2D lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matrix: {matrix}")

# Access nested elements
print(f"Element at [1][2]: {matrix[1][2]}")
print(f"First row: {matrix[0]}")
print(f"First column: {[row[0] for row in matrix]}")

# Create nested list
students = [
    ["Alice", 85],
    ["Bob", 92],
    ["Charlie", 78]
]
print(f"Students: {students}")

# Access student data
for student in students:
    name, score = student
    print(f"{name}: {score}")

print("\n=== LIST COMPREHENSION ===")

# List comprehension - create lists from existing lists
numbers = [1, 2, 3, 4, 5]
print(f"Original numbers: {numbers}")

# Square each number
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

# Filter even numbers
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

# Transform strings
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"Upper case words: {upper_words}")

# Complex comprehension
scores = [85, 92, 78, 96, 88]
grade_letters = ["A" if score >= 90 else "B" if score >= 80 else "C" for score in scores]
print(f"Scores: {scores}")
print(f"Grades: {grade_letters}")

# Nested comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Matrix: {matrix}")
print(f"Flattened: {flattened}")

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Shopping list manager
class ShoppingList:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        """Add item to shopping list"""
        if item not in self.items:
            self.items.append(item)
            print(f"Added '{item}' to shopping list")
        else:
            print(f"'{item}' is already in the list")
    
    def remove_item(self, item):
        """Remove item from shopping list"""
        if item in self.items:
            self.items.remove(item)
            print(f"Removed '{item}' from shopping list")
        else:
            print(f"'{item}' not found in list")
    
    def view_list(self):
        """View shopping list"""
        if self.items:
            print("Shopping List:")
            for i, item in enumerate(self.items, 1):
                print(f"  {i}. {item}")
        else:
            print("Shopping list is empty!")
    
    def clear_list(self):
        """Clear shopping list"""
        self.items.clear()
        print("Shopping list cleared!")

# Test shopping list
shopping = ShoppingList()
shopping.add_item("bread")
shopping.add_item("milk")
shopping.add_item("eggs")
shopping.view_list()

shopping.remove_item("milk")
shopping.view_list()

# Example 2: Grade calculator
def calculate_grades(student_scores):
    """Calculate and display grades"""
    print("Grade Report:")
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
    
    # Find highest and lowest scores
    highest = max(student_scores.values())
    lowest = min(student_scores.values())
    print(f"Highest: {highest}, Lowest: {lowest}")

# Test grade calculator
scores = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 76,
    "Diana": 92,
    "Eve": 68
}
calculate_grades(scores)

# Example 3: Data analysis
def analyze_data(data):
    """Analyze numerical data"""
    if not data:
        print("No data to analyze")
        return
    
    print(f"Data: {data}")
    print(f"Count: {len(data)}")
    print(f"Sum: {sum(data)}")
    print(f"Average: {sum(data) / len(data):.2f}")
    print(f"Minimum: {min(data)}")
    print(f"Maximum: {max(data)}")
    
    # Sort data
    sorted_data = sorted(data)
    print(f"Sorted: {sorted_data}")
    
    # Find median
    n = len(sorted_data)
    if n % 2 == 0:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]
    print(f"Median: {median}")

# Test data analysis
test_data = [85, 92, 78, 96, 88, 91, 83, 89, 94, 87]
analyze_data(test_data)

print("\n=== LIST BEST PRACTICES ===")

print("""
List Best Practices:
1. Use list() to create empty lists
2. Use append() to add single items
3. Use extend() to add multiple items
4. Use list comprehension for transformations
5. Use sorted() to create new sorted lists
6. Use sort() to sort in place
7. Use in operator to check membership
8. Use enumerate() to get index and value
9. Use zip() for parallel iteration
10. Test with edge cases (empty lists, single items)
""")

# Example of good list practices
def process_data(data):
    """Example of good list practices"""
    if not data:  # Handle empty data
        print("No data to process")
        return []
    
    print(f"Processing {len(data)} items:")
    
    # Use enumerate for index and value
    for i, item in enumerate(data, 1):
        if item is None:  # Handle None values
            print(f"  {i}. Skipping None value")
            continue
        
        print(f"  {i}. Processing: {item}")
    
    # Use list comprehension for transformation
    processed = [item for item in data if item is not None]
    return processed

# Test data processing
test_data = [1, 2, None, 4, 5, None, 7]
processed = process_data(test_data)
print(f"Processed data: {processed}")

"""
Key Points to Remember:
1. Lists are ordered and mutable
2. Use [] to create lists
3. Indexing starts at 0, negative indexing from end
4. Use append() to add items, remove() to remove items
5. Use list comprehension for transformations
6. Use sorted() for new sorted lists, sort() for in-place
7. Use in operator to check membership
8. Lists can contain any data type
9. Use enumerate() to get both index and value
10. Practice with real-world examples
"""
