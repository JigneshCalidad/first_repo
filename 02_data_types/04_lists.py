"""
📋 DATA TYPES - Lists (Collections)
==================================

Lists are ordered collections of items that can be changed (mutable).
Think of them as shopping lists - you can add, remove, and reorder items!

Lists can contain any type of data: numbers, strings, other lists, etc.
"""

print("=== CREATING LISTS ===")

# Empty list
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

print("\n=== ACCESSING LIST ELEMENTS ===")

# Indexing (starts from 0)
colors = ["red", "green", "blue", "yellow", "purple"]
print(f"Colors: {colors}")
print(f"First color (index 0): {colors[0]}")
print(f"Second color (index 1): {colors[1]}")
print(f"Last color (index -1): {colors[-1]}")
print(f"Second to last (index -2): {colors[-2]}")

# Slicing [start:end:step]
print(f"First 3 colors: {colors[0:3]}")
print(f"Colors 2-4: {colors[1:4]}")
print(f"Last 3 colors: {colors[-3:]}")
print(f"Every second color: {colors[::2]}")
print(f"Reverse list: {colors[::-1]}")

print("\n=== LIST METHODS - ADDING ELEMENTS ===")

# append() - add to end
shopping = ["bread", "milk"]
print(f"Original: {shopping}")
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

print("\n=== LIST METHODS - REMOVING ELEMENTS ===")

# remove() - remove first occurrence
numbers = [1, 2, 3, 2, 4, 2]
print(f"Original: {numbers}")
numbers.remove(2)  # Removes first 2
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

# index() - find position of element
fruits = ["apple", "banana", "cherry", "banana"]
print(f"Fruits: {fruits}")
print(f"Index of 'banana': {fruits.index('banana')}")
print(f"Index of 'cherry': {fruits.index('cherry')}")

# count() - count occurrences
print(f"Count of 'banana': {fruits.count('banana')}")
print(f"Count of 'apple': {fruits.count('apple')}")

# in operator - check if element exists
print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")

print("\n=== LIST METHODS - SORTING ===")

# sort() - sort in place
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")
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

print("\n=== LIST METHODS - OTHER ===")

# reverse() - reverse list in place
numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")
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

print("\n=== NESTED LISTS ===")

# Lists within lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matrix: {matrix}")
print(f"Element at [1][2]: {matrix[1][2]}")

# Accessing nested elements
students = [
    ["Alice", 85],
    ["Bob", 92],
    ["Charlie", 78]
]
print(f"Students: {students}")
print(f"Bob's score: {students[1][1]}")

print("\n=== LIST COMPREHENSION ===")

# Create list from existing list
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")

# Filter with comprehension
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Transform strings
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"Words: {words}")
print(f"Upper case: {upper_words}")

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Shopping list manager
def add_item(shopping_list, item):
    """Add item to shopping list"""
    if item not in shopping_list:
        shopping_list.append(item)
        print(f"Added '{item}' to shopping list")
    else:
        print(f"'{item}' is already in the list")

def remove_item(shopping_list, item):
    """Remove item from shopping list"""
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed '{item}' from shopping list")
    else:
        print(f"'{item}' not found in list")

# Test shopping list
shopping = ["bread", "milk"]
print(f"Initial list: {shopping}")

add_item(shopping, "eggs")
add_item(shopping, "bread")  # Already exists
add_item(shopping, "butter")
print(f"After adding: {shopping}")

remove_item(shopping, "milk")
remove_item(shopping, "cheese")  # Not in list
print(f"After removing: {shopping}")

# Example 2: Grade calculator
def calculate_grades(scores):
    """Calculate statistics for scores"""
    if not scores:
        return "No scores provided"
    
    total = sum(scores)
    average = total / len(scores)
    highest = max(scores)
    lowest = min(scores)
    
    return {
        "total": total,
        "average": round(average, 1),
        "highest": highest,
        "lowest": lowest,
        "count": len(scores)
    }

student_scores = [85, 92, 78, 96, 88]
stats = calculate_grades(student_scores)
print(f"Scores: {student_scores}")
print(f"Statistics: {stats}")

# Example 3: To-do list with priorities
def add_task(todo_list, task, priority="medium"):
    """Add task with priority"""
    todo_list.append({"task": task, "priority": priority})

def show_tasks(todo_list):
    """Display all tasks"""
    for i, item in enumerate(todo_list, 1):
        print(f"{i}. {item['task']} (Priority: {item['priority']})")

# Test to-do list
todos = []
add_task(todos, "Learn Python", "high")
add_task(todos, "Buy groceries", "medium")
add_task(todos, "Call mom", "low")

print("\nTo-do List:")
show_tasks(todos)

"""
Key Points to Remember:
1. Lists are ordered and mutable (can be changed)
2. Use [] to create lists
3. Indexing starts at 0, negative indexing from end
4. Common methods: append(), insert(), remove(), pop()
5. Use len() to get length
6. Lists can contain any data type
7. Use list comprehension for creating lists
8. Lists are passed by reference (changes affect original)
9. Use copy() or [:] to create copies
10. Lists are very versatile and commonly used!
"""
