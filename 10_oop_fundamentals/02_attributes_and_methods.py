"""
🏗️ OOP FUNDAMENTALS - Attributes and Methods
============================================

Learn about different types of attributes and methods in Python classes.
Understanding these concepts is crucial for effective OOP! 🎯
"""

print("=== INSTANCE ATTRIBUTES ===")

# Instance attributes are unique to each object
class Car:
    """A car class demonstrating instance attributes"""
    
    def __init__(self, make, model, year, color):
        # Instance attributes (unique to each car)
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = 0  # Default value
        self.is_running = False
    
    def start_engine(self):
        """Start the car engine"""
        if not self.is_running:
            self.is_running = True
            return f"The {self.year} {self.make} {self.model} engine is now running!"
        else:
            return "The engine is already running!"
    
    def stop_engine(self):
        """Stop the car engine"""
        if self.is_running:
            self.is_running = False
            return "The engine has been stopped."
        else:
            return "The engine is already stopped."
    
    def drive(self, miles):
        """Drive the car for specified miles"""
        if self.is_running:
            self.mileage += miles
            return f"Drove {miles} miles. Total mileage: {self.mileage}"
        else:
            return "Cannot drive - engine is not running!"
    
    def get_info(self):
        """Get car information"""
        return f"{self.year} {self.make} {self.model} ({self.color}) - {self.mileage} miles"

# Create car objects
print("Creating Car objects:")
car1 = Car("Toyota", "Camry", 2020, "Blue")
car2 = Car("Honda", "Civic", 2019, "Red")

print(f"Car 1: {car1.get_info()}")
print(f"Car 2: {car2.get_info()}")

# Each car has its own attributes
print(f"Car 1 make: {car1.make}")
print(f"Car 2 make: {car2.make}")

print("\n=== CLASS ATTRIBUTES ===")

# Class attributes are shared by all instances
class BankAccount:
    """A bank account class with class attributes"""
    
    # Class attributes (shared by all instances)
    bank_name = "Python Bank"
    interest_rate = 0.05  # 5% annual interest
    account_count = 0  # Track number of accounts created
    
    def __init__(self, account_holder, initial_balance=0):
        # Instance attributes
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = BankAccount.account_count + 1
        BankAccount.account_count += 1  # Increment class attribute
    
    def deposit(self, amount):
        """Deposit money"""
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    def withdraw(self, amount):
        """Withdraw money"""
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds!"
    
    def add_interest(self):
        """Add annual interest"""
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        return f"Added ${interest:.2f} interest. New balance: ${self.balance:.2f}"
    
    def get_account_info(self):
        """Get account information"""
        return f"Account #{self.account_number}: {self.account_holder} at {BankAccount.bank_name}"

# Test class attributes
print("=== Bank Account Example ===")
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

print(f"Bank name: {BankAccount.bank_name}")
print(f"Interest rate: {BankAccount.interest_rate}%")
print(f"Total accounts: {BankAccount.account_count}")

print(f"\n{account1.get_account_info()}")
print(f"{account2.get_account_info()}")

# Modify class attribute affects all instances
BankAccount.interest_rate = 0.06
print(f"Updated interest rate: {BankAccount.interest_rate}%")

print("\n=== INSTANCE METHODS ===")

# Instance methods operate on instance data
class Student:
    """A student class with instance methods"""
    
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []
        self.grades = {}
    
    def enroll_course(self, course_name):
        """Enroll in a course"""
        if course_name not in self.courses:
            self.courses.append(course_name)
            return f"Enrolled in {course_name}"
        else:
            return f"Already enrolled in {course_name}"
    
    def add_grade(self, course_name, grade):
        """Add a grade for a course"""
        if course_name in self.courses:
            self.grades[course_name] = grade
            return f"Grade {grade} added for {course_name}"
        else:
            return f"Not enrolled in {course_name}"
    
    def calculate_gpa(self):
        """Calculate GPA"""
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)
    
    def get_transcript(self):
        """Get student transcript"""
        transcript = f"Student: {self.name} (ID: {self.student_id})\n"
        transcript += "Courses and Grades:\n"
        for course, grade in self.grades.items():
            transcript += f"  {course}: {grade}\n"
        transcript += f"GPA: {self.calculate_gpa():.2f}"
        return transcript

# Test instance methods
print("=== Student Example ===")
student = Student("Charlie", "S123")
print(student.enroll_course("Python Programming"))
print(student.enroll_course("Data Structures"))
print(student.add_grade("Python Programming", 95))
print(student.add_grade("Data Structures", 88))
print(f"\n{student.get_transcript()}")

print("\n=== CLASS METHODS ===")

# Class methods operate on the class itself
class Date:
    """A date class with class methods"""
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        """Create Date from string (YYYY-MM-DD)"""
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @classmethod
    def today(cls):
        """Create Date for today"""
        import datetime
        today = datetime.date.today()
        return cls(today.year, today.month, today.day)
    
    @classmethod
    def from_timestamp(cls, timestamp):
        """Create Date from timestamp"""
        import datetime
        date = datetime.datetime.fromtimestamp(timestamp)
        return cls(date.year, date.month, date.day)
    
    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

# Test class methods
print("=== Date Class Example ===")
date1 = Date(2023, 12, 25)
date2 = Date.from_string("2023-12-25")
date3 = Date.today()

print(f"Date 1: {date1}")
print(f"Date 2: {date2}")
print(f"Today: {date3}")

print("\n=== STATIC METHODS ===")

# Static methods don't need access to class or instance data
class MathUtils:
    """A class with static methods for mathematical operations"""
    
    @staticmethod
    def add(a, b):
        """Add two numbers"""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers"""
        return a * b
    
    @staticmethod
    def is_even(number):
        """Check if number is even"""
        return number % 2 == 0
    
    @staticmethod
    def factorial(n):
        """Calculate factorial"""
        if n < 0:
            return None
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    @staticmethod
    def is_prime(number):
        """Check if number is prime"""
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

# Test static methods
print("=== MathUtils Example ===")
print(f"Add 5 + 3: {MathUtils.add(5, 3)}")
print(f"Multiply 4 * 7: {MathUtils.multiply(4, 7)}")
print(f"Is 8 even? {MathUtils.is_even(8)}")
print(f"Factorial of 5: {MathUtils.factorial(5)}")
print(f"Is 17 prime? {MathUtils.is_prime(17)}")

# Can also call on instance
math_utils = MathUtils()
print(f"Add 2 + 3: {math_utils.add(2, 3)}")

print("\n=== PROPERTY METHODS ===")

# Properties provide controlled access to attributes
class Temperature:
    """A temperature class with property methods"""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature in Fahrenheit"""
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """Get temperature in Kelvin"""
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        """Set temperature in Kelvin"""
        self.celsius = value - 273.15
    
    def __str__(self):
        return f"Temperature: {self._celsius}°C, {self.fahrenheit}°F, {self.kelvin}K"

# Test properties
print("=== Temperature Example ===")
temp = Temperature(25)
print(f"Initial: {temp}")

# Change Celsius
temp.celsius = 30
print(f"After setting Celsius to 30: {temp}")

# Change Fahrenheit
temp.fahrenheit = 86
print(f"After setting Fahrenheit to 86: {temp}")

# Change Kelvin
temp.kelvin = 300
print(f"After setting Kelvin to 300: {temp}")

print("\n=== PRIVATE ATTRIBUTES ===")

# Private attributes (convention: start with underscore)
class BankAccount:
    """A bank account with private attributes"""
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self._balance = initial_balance  # Private attribute
        self._transactions = []  # Private attribute
    
    def deposit(self, amount):
        """Deposit money"""
        if amount > 0:
            self._balance += amount
            self._transactions.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self._balance}"
        else:
            return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Withdraw money"""
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            self._transactions.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        else:
            return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        """Get current balance"""
        return self._balance
    
    def get_transactions(self):
        """Get transaction history"""
        return self._transactions.copy()  # Return copy to prevent external modification
    
    def __str__(self):
        return f"Account {self.account_number}: ${self._balance}"

# Test private attributes
print("=== Bank Account with Private Attributes ===")
account = BankAccount("12345", 1000)
print(f"Account: {account}")
print(account.deposit(500))
print(account.withdraw(200))
print(f"Balance: ${account.get_balance()}")
print(f"Transactions: {account.get_transactions()}")

print("\n=== METHOD TYPES SUMMARY ===")

print("""
Method Types:
1. Instance Methods: Operate on instance data (self)
2. Class Methods: Operate on class data (@classmethod)
3. Static Methods: Don't need class or instance data (@staticmethod)
4. Property Methods: Control attribute access (@property)

Attribute Types:
1. Instance Attributes: Unique to each object
2. Class Attributes: Shared by all instances
3. Private Attributes: Convention with underscore (_attribute)

Best Practices:
1. Use instance methods for object-specific operations
2. Use class methods for alternative constructors
3. Use static methods for utility functions
4. Use properties for controlled attribute access
5. Use private attributes to hide implementation details
6. Follow naming conventions
7. Document your methods clearly
8. Test all method types
""")

"""
Key Points to Remember:
1. Instance attributes are unique to each object
2. Class attributes are shared by all instances
3. Instance methods operate on instance data
4. Class methods operate on class data
5. Static methods don't need class or instance data
6. Properties provide controlled attribute access
7. Private attributes use underscore convention
8. Use appropriate method types for different purposes
9. Follow naming conventions and best practices
10. Practice with real-world examples
"""
