"""
🔄 LOOPS - While Loops
======================

While loops repeat code as long as a condition is True.
They're perfect for situations where you don't know how many times to repeat! 🔁
"""

print("=== BASIC WHILE LOOPS ===")

# Simple while loop
count = 0
print("Counting from 0 to 4:")
while count < 5:
    print(f"  Count: {count}")
    count += 1

# Countdown example
print("\nCountdown from 5:")
timer = 5
while timer > 0:
    print(f"  {timer}...")
    timer -= 1
print("  Blast off! 🚀")

# User input loop
print("\n=== USER INPUT LOOPS ===")

# Simple input validation
def get_positive_number():
    """Get a positive number from user"""
    while True:
        try:
            number = float(input("Enter a positive number: "))
            if number > 0:
                return number
            else:
                print("Please enter a positive number!")
        except ValueError:
            print("Please enter a valid number!")

# Uncomment to test input validation
# positive_num = get_positive_number()
# print(f"You entered: {positive_num}")

# Menu system
def show_menu():
    """Display menu options"""
    print("\n=== Menu ===")
    print("1. Add item")
    print("2. Remove item")
    print("3. View items")
    print("4. Exit")

def menu_system():
    """Simple menu system using while loop"""
    items = []
    
    while True:
        show_menu()
        choice = input("Choose option (1-4): ")
        
        if choice == "1":
            item = input("Enter item to add: ")
            items.append(item)
            print(f"Added '{item}' to list")
            
        elif choice == "2":
            if items:
                item = input("Enter item to remove: ")
                if item in items:
                    items.remove(item)
                    print(f"Removed '{item}' from list")
                else:
                    print(f"'{item}' not found in list")
            else:
                print("List is empty!")
                
        elif choice == "3":
            if items:
                print("Items in list:")
                for i, item in enumerate(items, 1):
                    print(f"  {i}. {item}")
            else:
                print("List is empty!")
                
        elif choice == "4":
            print("Goodbye! 👋")
            break
            
        else:
            print("Invalid choice! Please try again.")

# Uncomment to test menu system
# menu_system()

print("\n=== CONDITIONAL WHILE LOOPS ===")

# Loop until condition is met
def guess_number():
    """Number guessing game"""
    import random
    
    secret_number = random.randint(1, 10)
    attempts = 0
    max_attempts = 3
    
    print(f"Guess a number between 1 and 10 (you have {max_attempts} attempts)")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"🎉 Correct! You guessed it in {attempts} attempts!")
                return True
            elif guess < secret_number:
                print("Too low! 📉")
            else:
                print("Too high! 📈")
                
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"Game over! The number was {secret_number}")
    return False

# Uncomment to test guessing game
# guess_number()

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Password validation
def validate_password():
    """Validate password with multiple attempts"""
    correct_password = "password123"
    max_attempts = 3
    attempts = 0
    
    print("Password validation system")
    print("You have 3 attempts to enter the correct password")
    
    while attempts < max_attempts:
        password = input(f"Attempt {attempts + 1}: Enter password: ")
        attempts += 1
        
        if password == correct_password:
            print("✅ Password correct! Access granted!")
            return True
        else:
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"❌ Incorrect password. {remaining} attempts remaining.")
            else:
                print("❌ Access denied! No more attempts.")
    
    return False

# Test password validation
# validate_password()

# Example 2: Number sequence generator
def generate_sequence(start, end, step=1):
    """Generate number sequence using while loop"""
    numbers = []
    current = start
    
    while current < end:
        numbers.append(current)
        current += step
    
    return numbers

# Test sequence generation
sequence = generate_sequence(0, 10, 2)
print(f"Even numbers 0-10: {sequence}")

sequence = generate_sequence(1, 20, 3)
print(f"Numbers 1-20 step 3: {sequence}")

# Example 3: Data processing loop
def process_data_until_done():
    """Process data until user says done"""
    data = []
    
    print("Enter data (type 'done' when finished):")
    
    while True:
        item = input("Enter item: ")
        
        if item.lower() == 'done':
            break
        
        data.append(item)
        print(f"Added: {item}")
    
    print(f"\nProcessed {len(data)} items:")
    for i, item in enumerate(data, 1):
        print(f"  {i}. {item}")

# Uncomment to test data processing
# process_data_until_done()

print("\n=== WHILE LOOP PATTERNS ===")

# Pattern 1: Sentinel-controlled loop
def calculate_average():
    """Calculate average of numbers entered"""
    numbers = []
    print("Enter numbers (type -1 to stop):")
    
    while True:
        try:
            num = float(input("Enter number: "))
            if num == -1:
                break
            numbers.append(num)
        except ValueError:
            print("Please enter a valid number!")
    
    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"Average of {numbers}: {average:.2f}")
    else:
        print("No numbers entered!")

# Test average calculation
# calculate_average()

# Pattern 2: Flag-controlled loop
def search_in_list():
    """Search for item in list"""
    items = ["apple", "banana", "cherry", "date", "elderberry"]
    found = False
    search_count = 0
    
    print(f"Searching in: {items}")
    
    while not found and search_count < len(items):
        search_item = input("Enter item to search: ")
        search_count += 1
        
        if search_item in items:
            print(f"✅ Found '{search_item}' at position {items.index(search_item)}")
            found = True
        else:
            print(f"❌ '{search_item}' not found. Try again.")
    
    if not found:
        print("Search limit reached!")

# Test search function
# search_in_list()

print("\n=== NESTED WHILE LOOPS ===")

# Multiplication table with while loops
def multiplication_table(size):
    """Create multiplication table using nested while loops"""
    i = 1
    while i <= size:
        j = 1
        while j <= size:
            result = i * j
            print(f"{result:3}", end=" ")
            j += 1
        print()  # New line after each row
        i += 1

# Test multiplication table
print("Multiplication table (3x3):")
multiplication_table(3)

print("\n=== WHILE LOOP CONTROL ===")

# Break in while loops
def demonstrate_break():
    """Demonstrate break in while loop"""
    count = 0
    while count < 10:
        if count == 5:
            print("Breaking at 5!")
            break
        print(f"Count: {count}")
        count += 1

demonstrate_break()

# Continue in while loops
def demonstrate_continue():
    """Demonstrate continue in while loop"""
    count = 0
    while count < 5:
        count += 1
        if count == 3:
            print("Skipping 3!")
            continue
        print(f"Count: {count}")

demonstrate_continue()

print("\n=== INFINITE LOOPS AND PREVENTION ===")

# Safe infinite loop with break
def safe_infinite_loop():
    """Example of safe infinite loop"""
    count = 0
    while True:  # Infinite loop
        count += 1
        print(f"Count: {count}")
        
        if count >= 5:
            print("Breaking out of infinite loop!")
            break

safe_infinite_loop()

# Loop with timeout
def loop_with_timeout():
    """Loop with timeout to prevent infinite loops"""
    import time
    
    start_time = time.time()
    timeout = 5  # 5 seconds
    count = 0
    
    while time.time() - start_time < timeout:
        count += 1
        print(f"Count: {count}")
        time.sleep(0.5)  # Small delay
    
    print("Loop timed out!")

# Test timeout loop
# loop_with_timeout()

print("\n=== WHILE LOOP BEST PRACTICES ===")

print("""
While Loop Best Practices:
1. Always ensure the condition will eventually become False
2. Use break and continue judiciously
3. Avoid infinite loops unless intentional
4. Use meaningful variable names
5. Initialize variables before the loop
6. Update loop variables inside the loop
7. Handle edge cases (empty conditions)
8. Use timeouts for potentially infinite loops
9. Test with different input values
10. Consider using for loops when possible
""")

# Example of good while loop practices
def good_while_loop_example():
    """Example of well-structured while loop"""
    # Initialize variables
    numbers = []
    max_numbers = 5
    count = 0
    
    # Clear condition with meaningful variable names
    while count < max_numbers:
        try:
            # Get input with validation
            num = float(input(f"Enter number {count + 1}: "))
            numbers.append(num)
            count += 1
            
        except ValueError:
            print("Please enter a valid number!")
            # Continue without incrementing count
    
    # Process results
    if numbers:
        print(f"Numbers entered: {numbers}")
        print(f"Sum: {sum(numbers)}")
        print(f"Average: {sum(numbers) / len(numbers):.2f}")
    else:
        print("No valid numbers entered!")

# Test good while loop example
# good_while_loop_example()

"""
Key Points to Remember:
1. While loops repeat while condition is True
2. Always ensure condition will eventually become False
3. Use break to exit loop early
4. Use continue to skip current iteration
5. Initialize variables before the loop
6. Update loop variables inside the loop
7. Avoid infinite loops unless intentional
8. Use meaningful variable names
9. Handle edge cases and errors
10. Test with different input values
"""
