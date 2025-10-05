"""
🔒 OOP PRINCIPLES - Encapsulation
=================================

Encapsulation is the bundling of data and methods that operate on that data
into a single unit (class). It also involves hiding internal details! 🛡️
"""

print("=== WHAT IS ENCAPSULATION? ===")

# Encapsulation has two main aspects:
# 1. Bundling data and methods together
# 2. Hiding internal implementation details

print("""
Encapsulation Principles:
- Data Hiding: Hide internal data from external access
- Data Protection: Control how data is accessed and modified
- Interface Design: Provide clean, controlled interfaces
- Implementation Hiding: Hide complex internal logic
""")

print("\n=== BASIC ENCAPSULATION ===")

# Basic encapsulation example
class BankAccount:
    """A bank account with basic encapsulation"""
    
    def __init__(self, account_number, initial_balance=0):
        # Private attributes (convention: underscore prefix)
        self._account_number = account_number
        self._balance = initial_balance
        self._transactions = []
    
    # Public methods to access private data
    def get_balance(self):
        """Get current balance"""
        return self._balance
    
    def get_account_number(self):
        """Get account number"""
        return self._account_number
    
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
    
    def get_transactions(self):
        """Get transaction history"""
        return self._transactions.copy()  # Return copy to prevent external modification

# Test basic encapsulation
print("=== Basic Encapsulation Example ===")
account = BankAccount("12345", 1000)
print(f"Account: {account.get_account_number()}")
print(f"Balance: ${account.get_balance()}")
print(account.deposit(500))
print(account.withdraw(200))
print(f"Transactions: {account.get_transactions()}")

print("\n=== PROPERTY-BASED ENCAPSULATION ===")

# Using properties for better encapsulation
class Person:
    """A person class with property-based encapsulation"""
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        """Get person's name"""
        return self._name
    
    @name.setter
    def name(self, value):
        """Set person's name with validation"""
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
    
    @property
    def age(self):
        """Get person's age"""
        return self._age
    
    @age.setter
    def age(self, value):
        """Set person's age with validation"""
        if isinstance(value, int) and 0 <= value <= 150:
            self._age = value
        else:
            raise ValueError("Age must be an integer between 0 and 150")
    
    def __str__(self):
        return f"Person(name='{self._name}', age={self._age})"

# Test property-based encapsulation
print("=== Property-Based Encapsulation ===")
person = Person("Alice", 25)
print(f"Person: {person}")

# Use properties
person.name = "Alice Smith"
person.age = 26
print(f"Updated: {person}")

# Test validation
try:
    person.age = -5
except ValueError as e:
    print(f"Error: {e}")

try:
    person.name = ""
except ValueError as e:
    print(f"Error: {e}")

print("\n=== ADVANCED ENCAPSULATION ===")

# Advanced encapsulation with getters and setters
class Temperature:
    """A temperature class with advanced encapsulation"""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    def get_celsius(self):
        """Get temperature in Celsius"""
        return self._celsius
    
    def set_celsius(self, value):
        """Set temperature in Celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero!")
        self._celsius = value
    
    def get_fahrenheit(self):
        """Get temperature in Fahrenheit"""
        return (self._celsius * 9/5) + 32
    
    def set_fahrenheit(self, value):
        """Set temperature in Fahrenheit"""
        self.set_celsius((value - 32) * 5/9)
    
    def get_kelvin(self):
        """Get temperature in Kelvin"""
        return self._celsius + 273.15
    
    def set_kelvin(self, value):
        """Set temperature in Kelvin"""
        self.set_celsius(value - 273.15)
    
    def __str__(self):
        return f"Temperature: {self._celsius}°C, {self.get_fahrenheit()}°F, {self.get_kelvin()}K"

# Test advanced encapsulation
print("=== Advanced Encapsulation ===")
temp = Temperature(25)
print(f"Initial: {temp}")

temp.set_celsius(30)
print(f"After setting Celsius to 30: {temp}")

temp.set_fahrenheit(86)
print(f"After setting Fahrenheit to 86: {temp}")

temp.set_kelvin(300)
print(f"After setting Kelvin to 300: {temp}")

print("\n=== ENCAPSULATION WITH VALIDATION ===")

# Encapsulation with comprehensive validation
class Student:
    """A student class with comprehensive encapsulation"""
    
    def __init__(self, student_id, name, email):
        self._student_id = student_id
        self._name = name
        self._email = email
        self._courses = []
        self._grades = {}
    
    # Getters
    def get_student_id(self):
        return self._student_id
    
    def get_name(self):
        return self._name
    
    def get_email(self):
        return self._email
    
    def get_courses(self):
        return self._courses.copy()
    
    def get_grades(self):
        return self._grades.copy()
    
    # Setters with validation
    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
    
    def set_email(self, email):
        if isinstance(email, str) and "@" in email and "." in email:
            self._email = email
        else:
            raise ValueError("Email must be a valid email address")
    
    # Business logic methods
    def enroll_course(self, course_name):
        """Enroll in a course"""
        if not isinstance(course_name, str) or len(course_name) == 0:
            raise ValueError("Course name must be a non-empty string")
        
        if course_name not in self._courses:
            self._courses.append(course_name)
            return f"Enrolled in {course_name}"
        else:
            return f"Already enrolled in {course_name}"
    
    def add_grade(self, course_name, grade):
        """Add a grade for a course"""
        if course_name not in self._courses:
            raise ValueError("Not enrolled in this course")
        
        if not isinstance(grade, (int, float)) or grade < 0 or grade > 100:
            raise ValueError("Grade must be a number between 0 and 100")
        
        self._grades[course_name] = grade
        return f"Grade {grade} added for {course_name}"
    
    def calculate_gpa(self):
        """Calculate GPA"""
        if not self._grades:
            return 0.0
        return sum(self._grades.values()) / len(self._grades)
    
    def get_transcript(self):
        """Get student transcript"""
        transcript = f"Student: {self._name} (ID: {self._student_id})\n"
        transcript += f"Email: {self._email}\n"
        transcript += "Courses and Grades:\n"
        for course, grade in self._grades.items():
            transcript += f"  {course}: {grade}\n"
        transcript += f"GPA: {self.calculate_gpa():.2f}"
        return transcript

# Test comprehensive encapsulation
print("=== Comprehensive Encapsulation ===")
student = Student("S123", "Bob", "bob@example.com")
print(f"Student: {student.get_name()} (ID: {student.get_student_id()})")

# Test validation
try:
    student.set_name("")
except ValueError as e:
    print(f"Name validation error: {e}")

try:
    student.set_email("invalid-email")
except ValueError as e:
    print(f"Email validation error: {e}")

# Test business logic
print(student.enroll_course("Python Programming"))
print(student.add_grade("Python Programming", 95))
print(f"\n{student.get_transcript()}")

print("\n=== ENCAPSULATION PATTERNS ===")

# Different encapsulation patterns
class Library:
    """A library class demonstrating different encapsulation patterns"""
    
    def __init__(self, name):
        self._name = name
        self._books = []
        self._members = []
    
    # Public interface
    def add_book(self, title, author):
        """Add a book to the library"""
        if not self._is_valid_book(title, author):
            raise ValueError("Invalid book information")
        
        book = {"title": title, "author": author, "available": True}
        self._books.append(book)
        return f"Added book: {title} by {author}"
    
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
        return f"Library: {self._name}, Books: {total_books}, Available: {available_books}"
    
    # Private methods (implementation details)
    def _is_valid_book(self, title, author):
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

# Test encapsulation patterns
print("=== Encapsulation Patterns ===")
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

print("\n=== ENCAPSULATION BEST PRACTICES ===")

print("""
Encapsulation Best Practices:
1. Use private attributes (_attribute) for internal data
2. Provide public methods for controlled access
3. Validate input in setter methods
4. Use properties for simple getter/setter logic
5. Hide implementation details with private methods
6. Return copies of mutable data to prevent external modification
7. Use meaningful method names
8. Document your public interface clearly
9. Test encapsulation thoroughly
10. Follow the principle of least privilege
""")

# Example of good encapsulation design
class BankAccount:
    """A well-encapsulated bank account class"""
    
    def __init__(self, account_number, initial_balance=0):
        self._account_number = account_number
        self._balance = initial_balance
        self._transactions = []
        self._is_active = True
    
    # Public interface
    def deposit(self, amount):
        """Deposit money into account"""
        if not self._is_active:
            return "Account is inactive"
        
        if self._validate_amount(amount):
            self._balance += amount
            self._transactions.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self._balance}"
        else:
            return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if not self._is_active:
            return "Account is inactive"
        
        if self._validate_amount(amount) and self._has_sufficient_funds(amount):
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
        return self._transactions.copy()
    
    def deactivate(self):
        """Deactivate account"""
        self._is_active = False
        return "Account deactivated"
    
    def activate(self):
        """Activate account"""
        self._is_active = True
        return "Account activated"
    
    # Private methods
    def _validate_amount(self, amount):
        """Validate amount"""
        return isinstance(amount, (int, float)) and amount > 0
    
    def _has_sufficient_funds(self, amount):
        """Check if account has sufficient funds"""
        return amount <= self._balance

# Test well-encapsulated class
print("=== Well-Encapsulated Bank Account ===")
account = BankAccount("12345", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(f"Balance: ${account.get_balance()}")
print(f"Transactions: {account.get_transactions()}")

"""
Key Points to Remember:
1. Encapsulation bundles data and methods together
2. Use private attributes (_attribute) for internal data
3. Provide public methods for controlled access
4. Validate input in setter methods
5. Hide implementation details with private methods
6. Return copies of mutable data to prevent external modification
7. Use properties for simple getter/setter logic
8. Follow the principle of least privilege
9. Test encapsulation thoroughly
10. Practice with real-world examples
"""
