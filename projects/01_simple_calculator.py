"""
 PROJECT 1 - Simple Calculator
================================

Build a simple calculator that can perform basic arithmetic operations.
This project will help you practice functions, user input, and control flow.
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def get_number(prompt):
    """Get a valid number from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def get_operation():
    """Get a valid operation from user"""
    while True:
        operation = input("Enter operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            return operation
        print("Please enter a valid operation (+, -, *, /)")

def calculator():
    """Main calculator function"""
    print("=== Simple Calculator ===")
    print("Available operations: +, -, *, /")
    print("Type 'quit' to exit")
    
    while True:
        try:
            # Get user input
            user_input = input("\nEnter expression (e.g., '5 + 3') or 'quit': ")
            
            if user_input.lower() == 'quit':
                print("Goodbye! 👋")
                break
            
            # Parse the expression
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid format! Use: number operation number")
                continue
            
            num1, operation, num2 = parts
            num1 = float(num1)
            num2 = float(num2)
            
            # Perform calculation
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operation!")
                continue
            
            # Display result
            print(f"Result: {result}")
            
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"An error occurred: {e}")

def advanced_calculator():
    """Advanced calculator with more features"""
    print("=== Advanced Calculator ===")
    print("Available operations: +, -, *, /, ** (power), % (modulo)")
    print("Type 'quit' to exit")
    
    while True:
        try:
            # Get user input
            user_input = input("\nEnter expression (e.g., '5 + 3') or 'quit': ")
            
            if user_input.lower() == 'quit':
                print("Goodbye! 👋")
                break
            
            # Parse the expression
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid format! Use: number operation number")
                continue
            
            num1, operation, num2 = parts
            num1 = float(num1)
            num2 = float(num2)
            
            # Perform calculation
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            elif operation == '**':
                result = num1 ** num2
            elif operation == '%':
                result = num1 % num2
            else:
                print("Invalid operation!")
                continue
            
            # Display result
            print(f"Result: {result}")
            
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"An error occurred: {e}")

def menu_calculator():
    """Calculator with menu interface"""
    print("=== Menu Calculator ===")
    
    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Choose operation (1-5): ")
        
        if choice == '5':
            print("Goodbye! 👋")
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = get_number("Enter first number: ")
                num2 = get_number("Enter second number: ")
                
                if choice == '1':
                    result = add(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"{num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"{num1} * {num2} = {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")
                    
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid choice! Please enter 1-5.")

def scientific_calculator():
    """Scientific calculator with more functions"""
    import math
    
    print("=== Scientific Calculator ===")
    print("Available operations: +, -, *, /, **, sqrt, sin, cos, tan")
    print("Type 'quit' to exit")
    
    while True:
        try:
            user_input = input("\nEnter expression or 'quit': ")
            
            if user_input.lower() == 'quit':
                print("Goodbye! 👋")
                break
            
            # Handle single-argument functions
            if user_input.startswith('sqrt'):
                num = float(user_input.split('(')[1].split(')')[0])
                result = math.sqrt(num)
                print(f"√{num} = {result}")
                continue
            
            # Handle trigonometric functions
            if user_input.startswith(('sin', 'cos', 'tan')):
                func_name = user_input.split('(')[0]
                num = float(user_input.split('(')[1].split(')')[0])
                
                if func_name == 'sin':
                    result = math.sin(math.radians(num))
                elif func_name == 'cos':
                    result = math.cos(math.radians(num))
                elif func_name == 'tan':
                    result = math.tan(math.radians(num))
                
                print(f"{func_name}({num}°) = {result}")
                continue
            
            # Handle two-argument operations
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid format!")
                continue
            
            num1, operation, num2 = parts
            num1 = float(num1)
            num2 = float(num2)
            
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            elif operation == '**':
                result = num1 ** num2
            else:
                print("Invalid operation!")
                continue
            
            print(f"Result: {result}")
            
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    """Main function to choose calculator type"""
    print("Choose calculator type:")
    print("1. Simple Calculator")
    print("2. Advanced Calculator")
    print("3. Menu Calculator")
    print("4. Scientific Calculator")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == '1':
        calculator()
    elif choice == '2':
        advanced_calculator()
    elif choice == '3':
        menu_calculator()
    elif choice == '4':
        scientific_calculator()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()

"""
Project Features:
1. Basic arithmetic operations (+, -, *, /)
2. Error handling for invalid input
3. Multiple calculator interfaces
4. Scientific functions (sqrt, sin, cos, tan)
5. Menu-driven interface
6. User-friendly error messages

Learning Objectives:
- Practice with functions
- Handle user input and validation
- Implement error handling
- Create different program interfaces
- Work with mathematical operations
- Practice control flow and loops

Extensions:
- Add more mathematical functions
- Implement a history feature
- Add unit conversions
- Create a GUI version
- Add keyboard shortcuts
- Implement expression evaluation
"""
