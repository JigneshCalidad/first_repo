"""
🎛️ LOOPS - Loop Control Statements
=================================

Loop control statements let you control the flow of loops.
They're like traffic signals for your loops! 🚦
"""

print("=== BREAK STATEMENT ===")

# Break - exit loop completely
print("Numbers 1 to 10 (break at 5):")
for i in range(1, 11):
    if i == 5:
        print(f"  Breaking at {i}!")
        break
    print(f"  {i}")

# Break in while loop
print("\nWhile loop with break:")
count = 0
while count < 10:
    count += 1
    if count == 7:
        print(f"  Breaking at {count}!")
        break
    print(f"  Count: {count}")

# Break in nested loops
print("\nNested loops with break:")
for i in range(1, 4):
    print(f"Outer loop: {i}")
    for j in range(1, 4):
        if j == 2:
            print(f"  Breaking inner loop at {j}")
            break
        print(f"  Inner loop: {j}")

print("\n=== CONTINUE STATEMENT ===")

# Continue - skip current iteration
print("Numbers 1 to 10 (skip 5):")
for i in range(1, 11):
    if i == 5:
        print(f"  Skipping {i}!")
        continue
    print(f"  {i}")

# Continue in while loop
print("\nWhile loop with continue:")
count = 0
while count < 10:
    count += 1
    if count == 7:
        print(f"  Skipping {count}!")
        continue
    print(f"  Count: {count}")

# Continue with multiple conditions
print("\nSkip even numbers:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(f"  Odd number: {i}")

print("\n=== PASS STATEMENT ===")

# Pass - do nothing (placeholder)
print("Numbers 1 to 10 (pass at 5):")
for i in range(1, 11):
    if i == 5:
        print(f"  Pass at {i} (doing nothing)")
        pass
    print(f"  {i}")

# Pass in function definition
def incomplete_function():
    """Function with pass placeholder"""
    pass  # TODO: Implement this function

print("Function with pass:", incomplete_function())

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Search with break
def search_item(items, target):
    """Search for item in list with break"""
    print(f"Searching for '{target}' in {items}")
    
    for i, item in enumerate(items):
        if item == target:
            print(f"✅ Found '{target}' at index {i}")
            break
    else:
        print(f"❌ '{target}' not found")

# Test search
fruits = ["apple", "banana", "cherry", "date"]
search_item(fruits, "cherry")
search_item(fruits, "grape")

# Example 2: Data validation with continue
def validate_numbers(numbers):
    """Validate numbers, skip invalid ones"""
    valid_numbers = []
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            print(f"Skipping invalid number: {num}")
            continue
        
        if num < 0:
            print(f"Skipping negative number: {num}")
            continue
        
        valid_numbers.append(num)
        print(f"Added valid number: {num}")
    
    return valid_numbers

# Test validation
mixed_data = [1, -2, 3.5, "hello", 4, -1.5, 6]
valid_nums = validate_numbers(mixed_data)
print(f"Valid numbers: {valid_nums}")

# Example 3: Menu system with break
def interactive_menu():
    """Interactive menu with break"""
    print("=== Interactive Menu ===")
    
    while True:
        print("\n1. Add item")
        print("2. Remove item")
        print("3. View items")
        print("4. Exit")
        
        choice = input("Choose option (1-4): ")
        
        if choice == "4":
            print("Goodbye! 👋")
            break
        elif choice == "1":
            item = input("Enter item to add: ")
            print(f"Added: {item}")
        elif choice == "2":
            item = input("Enter item to remove: ")
            print(f"Removed: {item}")
        elif choice == "3":
            print("Viewing items...")
        else:
            print("Invalid choice!")

# Uncomment to test menu
# interactive_menu()

print("\n=== LOOP CONTROL IN NESTED LOOPS ===")

# Break in nested loops
def find_coordinate(matrix, target):
    """Find target in 2D matrix"""
    print(f"Searching for {target} in matrix:")
    for row in matrix:
        print(f"  {row}")
    
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == target:
                print(f"✅ Found {target} at position ({i}, {j})")
                break  # Only breaks inner loop
        else:
            continue  # Only executed if inner loop didn't break
        break  # Breaks outer loop

# Test coordinate search
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
find_coordinate(matrix, 5)
find_coordinate(matrix, 10)

# Continue in nested loops
def process_matrix(matrix):
    """Process matrix, skip negative numbers"""
    print("Processing matrix:")
    for row in matrix:
        print(f"  {row}")
    
    print("Processing results:")
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value < 0:
                print(f"  Skipping negative value {value} at ({i}, {j})")
                continue
            
            result = value * 2
            print(f"  {value} * 2 = {result} at ({i}, {j})")

# Test matrix processing
matrix_with_negatives = [[1, -2, 3], [-4, 5, -6], [7, 8, -9]]
process_matrix(matrix_with_negatives)

print("\n=== ELSE CLAUSE WITH LOOPS ===")

# Else clause with for loop
def search_with_else(items, target):
    """Search with else clause"""
    print(f"Searching for '{target}' in {items}")
    
    for item in items:
        if item == target:
            print(f"✅ Found '{target}'!")
            break
    else:
        print(f"❌ '{target}' not found in list")

# Test search with else
fruits = ["apple", "banana", "cherry"]
search_with_else(fruits, "banana")
search_with_else(fruits, "grape")

# Else clause with while loop
def countdown_with_else():
    """Countdown with else clause"""
    count = 5
    while count > 0:
        print(f"Countdown: {count}")
        count -= 1
    else:
        print("Countdown complete! 🚀")

countdown_with_else()

print("\n=== LOOP CONTROL PATTERNS ===")

# Pattern 1: Early exit on condition
def process_until_negative(numbers):
    """Process numbers until negative is found"""
    print(f"Processing numbers: {numbers}")
    
    for num in numbers:
        if num < 0:
            print(f"Found negative number {num}, stopping!")
            break
        print(f"Processing: {num}")

# Test early exit
process_until_negative([1, 2, 3, -4, 5, 6])

# Pattern 2: Skip invalid data
def process_valid_data(data):
    """Process only valid data"""
    print(f"Processing data: {data}")
    
    for item in data:
        if not isinstance(item, (int, float)):
            print(f"Skipping invalid item: {item}")
            continue
        
        if item <= 0:
            print(f"Skipping non-positive item: {item}")
            continue
        
        result = item ** 2
        print(f"Valid item {item} squared: {result}")

# Test data processing
mixed_data = [1, "hello", 3.5, -2, 4, "world", 5]
process_valid_data(mixed_data)

# Pattern 3: Retry mechanism
def retry_operation(max_attempts=3):
    """Retry operation with break"""
    attempts = 0
    
    while attempts < max_attempts:
        attempts += 1
        print(f"Attempt {attempts}/{max_attempts}")
        
        # Simulate operation that might fail
        success = attempts >= 2  # Simulate success on second attempt
        
        if success:
            print("✅ Operation successful!")
            break
        else:
            print("❌ Operation failed, retrying...")
    else:
        print("❌ All attempts failed!")

# Test retry mechanism
retry_operation()

print("\n=== LOOP CONTROL BEST PRACTICES ===")

print("""
Loop Control Best Practices:
1. Use break for early exit when condition is met
2. Use continue to skip current iteration
3. Use pass as placeholder for incomplete code
4. Be careful with break in nested loops
5. Use else clause with loops for cleanup
6. Avoid deep nesting with multiple breaks
7. Use meaningful variable names
8. Test all possible code paths
9. Consider using functions for complex logic
10. Document complex loop control logic
""")

# Example of good loop control practices
def good_loop_control_example():
    """Example of well-structured loop control"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    
    print(f"Searching for {target} in {numbers}")
    
    for i, num in enumerate(numbers):
        if num == target:
            print(f"✅ Found {target} at index {i}")
            break
        elif num > target:
            print(f"❌ Number {num} is greater than target, stopping search")
            break
        else:
            print(f"  Checking {num}...")
    else:
        print(f"❌ {target} not found")

# Test good loop control
good_loop_control_example()

"""
Key Points to Remember:
1. break: Exit loop completely
2. continue: Skip current iteration
3. pass: Do nothing (placeholder)
4. else: Execute when loop completes normally
5. Use break for early exit
6. Use continue to skip invalid data
7. Be careful with nested loops
8. Test all possible code paths
9. Use meaningful variable names
10. Practice with real-world examples
"""
