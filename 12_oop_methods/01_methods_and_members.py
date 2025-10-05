"""
🔧 OOP METHODS - Methods and Members
====================================

Learn about different types of methods and members in Python classes.
Understanding these concepts is crucial for effective OOP design! 🛠️
"""

print("=== INSTANCE METHODS ===")

# Instance methods operate on instance data
class BankAccount:
    """A bank account class with instance methods"""
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = []
    
    def deposit(self, amount):
        """Instance method to deposit money"""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Instance method to withdraw money"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        """Instance method to get balance"""
        return self.balance
    
    def get_transactions(self):
        """Instance method to get transactions"""
        return self.transactions.copy()
    
    def get_account_info(self):
        """Instance method to get account information"""
        return f"Account: {self.account_number}, Balance: ${self.balance}"

# Test instance methods
print("=== Instance Methods Example ===")
account = BankAccount("12345", 1000)
print(account.get_account_info())
print(account.deposit(500))
print(account.withdraw(200))
print(f"Balance: ${account.get_balance()}")
print(f"Transactions: {account.get_transactions()}")

print("\n=== CLASS METHODS ===")

# Class methods operate on class data
class Student:
    """A student class with class methods"""
    
    # Class attribute
    total_students = 0
    
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}
        # Increment class attribute
        Student.total_students += 1
    
    @classmethod
    def from_string(cls, student_string):
        """Class method to create student from string"""
        name, student_id = student_string.split(',')
        return cls(name.strip(), student_id.strip())
    
    @classmethod
    def get_total_students(cls):
        """Class method to get total number of students"""
        return cls.total_students
    
    @classmethod
    def reset_counter(cls):
        """Class method to reset student counter"""
        cls.total_students = 0
        return "Student counter reset"
    
    def add_grade(self, course, grade):
        """Instance method to add grade"""
        self.grades[course] = grade
        return f"Grade {grade} added for {course}"
    
    def get_gpa(self):
        """Instance method to calculate GPA"""
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)
    
    def get_info(self):
        """Instance method to get student info"""
        return f"Student: {self.name} (ID: {self.student_id}), GPA: {self.get_gpa():.2f}"

# Test class methods
print("=== Class Methods Example ===")
student1 = Student("Alice", "S001")
student2 = Student("Bob", "S002")
student3 = Student.from_string("Charlie, S003")

print(f"Total students: {Student.get_total_students()}")
print(f"Student 1: {student1.get_info()}")
print(f"Student 2: {student2.get_info()}")
print(f"Student 3: {student3.get_info()}")

print("\n=== STATIC METHODS ===")

# Static methods don't need access to class or instance data
class MathUtils:
    """A class with static methods for mathematical operations"""
    
    @staticmethod
    def add(a, b):
        """Static method to add two numbers"""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """Static method to multiply two numbers"""
        return a * b
    
    @staticmethod
    def is_even(number):
        """Static method to check if number is even"""
        return number % 2 == 0
    
    @staticmethod
    def factorial(n):
        """Static method to calculate factorial"""
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
        """Static method to check if number is prime"""
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    
    @staticmethod
    def fibonacci(n):
        """Static method to calculate Fibonacci number"""
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Test static methods
print("=== Static Methods Example ===")
print(f"Add 5 + 3: {MathUtils.add(5, 3)}")
print(f"Multiply 4 * 7: {MathUtils.multiply(4, 7)}")
print(f"Is 8 even? {MathUtils.is_even(8)}")
print(f"Factorial of 5: {MathUtils.factorial(5)}")
print(f"Is 17 prime? {MathUtils.is_prime(17)}")
print(f"Fibonacci(10): {MathUtils.fibonacci(10)}")

# Can also call on instance
math_utils = MathUtils()
print(f"Add 2 + 3: {math_utils.add(2, 3)}")

print("\n=== PROPERTY METHODS ===")

# Property methods provide controlled access to attributes
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

# Test property methods
print("=== Property Methods Example ===")
temp = Temperature(25)
print(f"Initial: {temp}")

# Use properties
temp.celsius = 30
print(f"After setting Celsius to 30: {temp}")

temp.fahrenheit = 86
print(f"After setting Fahrenheit to 86: {temp}")

temp.kelvin = 300
print(f"After setting Kelvin to 300: {temp}")

print("\n=== SPECIAL METHODS (DUNDER METHODS) ===")

# Special methods start and end with double underscores
class Person:
    """A person class with special methods"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """String representation for users"""
        return f"Person(name='{self.name}', age={self.age})"
    
    def __repr__(self):
        """Developer representation"""
        return f"Person('{self.name}', {self.age})"
    
    def __len__(self):
        """Length of the person (age)"""
        return self.age
    
    def __eq__(self, other):
        """Check if two persons are equal"""
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False
    
    def __lt__(self, other):
        """Check if person is younger than other"""
        if isinstance(other, Person):
            return self.age < other.age
        return False
    
    def __le__(self, other):
        """Check if person is younger than or equal to other"""
        if isinstance(other, Person):
            return self.age <= other.age
        return False
    
    def __gt__(self, other):
        """Check if person is older than other"""
        if isinstance(other, Person):
            return self.age > other.age
        return False
    
    def __ge__(self, other):
        """Check if person is older than or equal to other"""
        if isinstance(other, Person):
            return self.age >= other.age
        return False
    
    def __hash__(self):
        """Hash for use in sets and dictionaries"""
        return hash((self.name, self.age))
    
    def __bool__(self):
        """Boolean representation"""
        return self.age > 0

# Test special methods
print("=== Special Methods Example ===")
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
person3 = Person("Alice", 25)

print(f"Person 1: {person1}")
print(f"Person 1 repr: {repr(person1)}")
print(f"Person 1 length: {len(person1)}")
print(f"Person 1 == Person 2: {person1 == person2}")
print(f"Person 1 == Person 3: {person1 == person3}")
print(f"Person 1 < Person 2: {person1 < person2}")
print(f"Person 1 > Person 2: {person1 > person2}")
print(f"Person 1 <= Person 2: {person1 <= person2}")
print(f"Person 1 >= Person 2: {person1 >= person2}")
print(f"Person 1 hash: {hash(person1)}")
print(f"Person 1 bool: {bool(person1)}")

print("\n=== PRIVATE METHODS ===")

# Private methods (convention: start with underscore)
class BankAccount:
    """A bank account with private methods"""
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = []
    
    def deposit(self, amount):
        """Public method to deposit money"""
        if self._validate_amount(amount):
            self.balance += amount
            self._record_transaction(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Public method to withdraw money"""
        if self._validate_amount(amount) and self._has_sufficient_funds(amount):
            self.balance -= amount
            self._record_transaction(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        """Public method to get balance"""
        return self.balance
    
    def get_transactions(self):
        """Public method to get transactions"""
        return self.transactions.copy()
    
    # Private methods (implementation details)
    def _validate_amount(self, amount):
        """Private method to validate amount"""
        return isinstance(amount, (int, float)) and amount > 0
    
    def _has_sufficient_funds(self, amount):
        """Private method to check sufficient funds"""
        return amount <= self.balance
    
    def _record_transaction(self, transaction):
        """Private method to record transaction"""
        self.transactions.append(transaction)
    
    def _calculate_interest(self, rate):
        """Private method to calculate interest"""
        return self.balance * rate

# Test private methods
print("=== Private Methods Example ===")
account = BankAccount("12345", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(f"Balance: ${account.get_balance()}")
print(f"Transactions: {account.get_transactions()}")

print("\n=== METHOD OVERLOADING ===")

# Python doesn't have true method overloading, but we can simulate it
class Calculator:
    """A calculator class with method overloading simulation"""
    
    def add(self, a, b=None):
        """Add two numbers or sum a list"""
        if b is None:
            if isinstance(a, (list, tuple)):
                return sum(a)
            else:
                return a
        else:
            return a + b
    
    def multiply(self, a, b=None):
        """Multiply two numbers or multiply a list"""
        if b is None:
            if isinstance(a, (list, tuple)):
                result = 1
                for item in a:
                    result *= item
                return result
            else:
                return a
        else:
            return a * b
    
    def calculate(self, operation, *args):
        """Polymorphic calculation method"""
        if operation == "add":
            return self.add(*args)
        elif operation == "multiply":
            return self.multiply(*args)
        elif operation == "subtract":
            if len(args) == 2:
                return args[0] - args[1]
        elif operation == "divide":
            if len(args) == 2:
                return args[0] / args[1]
        else:
            return "Unknown operation"

# Test method overloading
print("=== Method Overloading Example ===")
calc = Calculator()
print(f"Add 5 + 3: {calc.add(5, 3)}")
print(f"Add list [1, 2, 3, 4]: {calc.add([1, 2, 3, 4])}")
print(f"Multiply 4 * 7: {calc.multiply(4, 7)}")
print(f"Multiply list [2, 3, 4]: {calc.multiply([2, 3, 4])}")
print(f"Calculate add 10 + 5: {calc.calculate('add', 10, 5)}")
print(f"Calculate subtract 10 - 5: {calc.calculate('subtract', 10, 5)}")

print("\n=== METHOD CHAINING ===")

# Method chaining allows calling multiple methods in sequence
class StringBuilder:
    """A string builder class with method chaining"""
    
    def __init__(self, initial_string=""):
        self.string = initial_string
    
    def append(self, text):
        """Append text to string"""
        self.string += text
        return self  # Return self for chaining
    
    def prepend(self, text):
        """Prepend text to string"""
        self.string = text + self.string
        return self  # Return self for chaining
    
    def insert(self, index, text):
        """Insert text at index"""
        self.string = self.string[:index] + text + self.string[index:]
        return self  # Return self for chaining
    
    def replace(self, old, new):
        """Replace text in string"""
        self.string = self.string.replace(old, new)
        return self  # Return self for chaining
    
    def to_upper(self):
        """Convert string to uppercase"""
        self.string = self.string.upper()
        return self  # Return self for chaining
    
    def to_lower(self):
        """Convert string to lowercase"""
        self.string = self.string.lower()
        return self  # Return self for chaining
    
    def get_string(self):
        """Get the final string"""
        return self.string
    
    def __str__(self):
        """String representation"""
        return self.string

# Test method chaining
print("=== Method Chaining Example ===")
builder = StringBuilder("Hello")
result = (builder
          .append(" World")
          .prepend("Say: ")
          .to_upper()
          .replace("WORLD", "PYTHON")
          .get_string())
print(f"Result: {result}")

# Another example
builder2 = StringBuilder()
result2 = (builder2
           .append("Python")
           .append(" is")
           .append(" awesome")
           .to_upper()
           .get_string())
print(f"Result 2: {result2}")

print("\n=== METHODS AND MEMBERS BEST PRACTICES ===")

print("""
Methods and Members Best Practices:
1. Use instance methods for object-specific operations
2. Use class methods for alternative constructors
3. Use static methods for utility functions
4. Use properties for controlled attribute access
5. Use private methods for implementation details
6. Override special methods when appropriate
7. Use method chaining for fluent interfaces
8. Follow naming conventions
9. Document your methods clearly
10. Test all method types thoroughly
""")

# Example of good method design
class Library:
    """A library class with well-designed methods"""
    
    def __init__(self, name):
        self.name = name
        self._books = []
        self._members = []
    
    # Public methods
    def add_book(self, title, author):
        """Add a book to the library"""
        if self._validate_book(title, author):
            book = {"title": title, "author": author, "available": True}
            self._books.append(book)
            return f"Added book: {title} by {author}"
        else:
            return "Invalid book information"
    
    def remove_book(self, title):
        """Remove a book from the library"""
        for i, book in enumerate(self._books):
            if book["title"] == title:
                del self._books[i]
                return f"Removed book: {title}"
        return f"Book not found: {title}"
    
    def borrow_book(self, title, member_name):
        """Borrow a book"""
        if not self._is_member(member_name):
            return f"{member_name} is not a library member"
        
        for book in self._books:
            if book["title"] == title and book["available"]:
                book["available"] = False
                return f"{member_name} borrowed {title}"
        return f"Book not available: {title}"
    
    def return_book(self, title):
        """Return a book"""
        for book in self._books:
            if book["title"] == title and not book["available"]:
                book["available"] = True
                return f"Returned book: {title}"
        return f"Book not found or already available: {title}"
    
    def get_available_books(self):
        """Get list of available books"""
        return [book["title"] for book in self._books if book["available"]]
    
    def get_library_info(self):
        """Get library information"""
        total_books = len(self._books)
        available_books = len(self.get_available_books())
        return f"Library: {self.name}, Books: {total_books}, Available: {available_books}"
    
    # Private methods
    def _validate_book(self, title, author):
        """Validate book information"""
        return isinstance(title, str) and len(title) > 0 and isinstance(author, str) and len(author) > 0
    
    def _is_member(self, member_name):
        """Check if person is a library member"""
        return member_name in self._members
    
    def add_member(self, member_name):
        """Add a library member"""
        if member_name not in self._members:
            self._members.append(member_name)
            return f"Added member: {member_name}"
        else:
            return f"Already a member: {member_name}"

# Test library methods
print("=== Library Methods Example ===")
library = Library("Python Library")
print(library.add_member("Alice"))
print(library.add_member("Bob"))

print(library.add_book("Python Programming", "Guido van Rossum"))
print(library.add_book("Data Structures", "John Doe"))
print(library.add_book("Algorithms", "Jane Smith"))

print(f"\n{library.get_library_info()}")
print(f"Available books: {library.get_available_books()}")

print(library.borrow_book("Python Programming", "Alice"))
print(library.borrow_book("Data Structures", "Bob"))
print(f"Available books after borrowing: {library.get_available_books()}")

print(library.return_book("Python Programming"))
print(f"Available books after return: {library.get_available_books()}")

"""
Key Points to Remember:
1. Instance methods operate on instance data
2. Class methods operate on class data
3. Static methods don't need class or instance data
4. Properties provide controlled attribute access
5. Special methods define object behavior
6. Private methods hide implementation details
7. Use method chaining for fluent interfaces
8. Follow naming conventions
9. Document your methods clearly
10. Test all method types thoroughly
"""
