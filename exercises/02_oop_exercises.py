"""
🏋️ OOP EXERCISES - Practice Problems
====================================

Practice exercises to master Object-Oriented Programming concepts.
Solve these problems to become an OOP expert! 💪
"""

print("=== OOP EXERCISES ===")

# These exercises will help you practice:
# - Class design and implementation
# - Inheritance and polymorphism
# - Encapsulation and abstraction
# - Method overriding and overloading
# - Special methods and operators

print("\n=== EXERCISE 1: BASIC CLASS DESIGN ===")

"""
Exercise 1: Create a Library Management System

Create a Library class that can:
1. Add books to the library
2. Remove books from the library
3. Search for books by title or author
4. Check out books to members
5. Return books from members
6. Get library statistics

Requirements:
- Use encapsulation (private attributes)
- Implement proper validation
- Handle errors gracefully
- Provide clear feedback to users
"""

# Your solution here:
class Library:
    """Library management system"""
    
    def __init__(self, name):
        self.name = name
        self._books = []
        self._members = []
        self._checked_out = {}
    
    def add_book(self, title, author, isbn):
        """Add a book to the library"""
        if not self._validate_book_info(title, author, isbn):
            return "Invalid book information"
        
        book = {"title": title, "author": author, "isbn": isbn, "available": True}
        self._books.append(book)
        return f"Added book: {title} by {author}"
    
    def remove_book(self, isbn):
        """Remove a book from the library"""
        for i, book in enumerate(self._books):
            if book["isbn"] == isbn:
                if not book["available"]:
                    return "Cannot remove book - it's checked out"
                del self._books[i]
                return f"Removed book: {book['title']}"
        return "Book not found"
    
    def search_books(self, query):
        """Search for books by title or author"""
        results = []
        for book in self._books:
            if query.lower() in book["title"].lower() or query.lower() in book["author"].lower():
                results.append(book)
        return results
    
    def add_member(self, member_name, member_id):
        """Add a member to the library"""
        if member_name in [member["name"] for member in self._members]:
            return "Member already exists"
        
        self._members.append({"name": member_name, "id": member_id})
        return f"Added member: {member_name}"
    
    def check_out_book(self, isbn, member_name):
        """Check out a book to a member"""
        if member_name not in [member["name"] for member in self._members]:
            return "Member not found"
        
        for book in self._books:
            if book["isbn"] == isbn:
                if book["available"]:
                    book["available"] = False
                    self._checked_out[isbn] = member_name
                    return f"Checked out {book['title']} to {member_name}"
                else:
                    return "Book is already checked out"
        return "Book not found"
    
    def return_book(self, isbn):
        """Return a book to the library"""
        if isbn in self._checked_out:
            member_name = self._checked_out[isbn]
            for book in self._books:
                if book["isbn"] == isbn:
                    book["available"] = True
                    del self._checked_out[isbn]
                    return f"Returned {book['title']} from {member_name}"
        return "Book not checked out"
    
    def get_library_stats(self):
        """Get library statistics"""
        total_books = len(self._books)
        available_books = len([book for book in self._books if book["available"]])
        checked_out_books = len(self._checked_out)
        total_members = len(self._members)
        
        return f"Library: {self.name}, Books: {total_books}, Available: {available_books}, Checked Out: {checked_out_books}, Members: {total_members}"
    
    def _validate_book_info(self, title, author, isbn):
        """Validate book information"""
        return (isinstance(title, str) and len(title) > 0 and
                isinstance(author, str) and len(author) > 0 and
                isinstance(isbn, str) and len(isbn) > 0)

# Test Exercise 1
print("=== Testing Exercise 1 ===")
library = Library("Python Library")
print(library.add_book("Python Programming", "Guido van Rossum", "978-0-123456-78-9"))
print(library.add_book("Data Structures", "John Doe", "978-0-123456-79-0"))
print(library.add_member("Alice", "M001"))
print(library.add_member("Bob", "M002"))
print(library.check_out_book("978-0-123456-78-9", "Alice"))
print(library.return_book("978-0-123456-78-9"))
print(library.get_library_stats())

print("\n=== EXERCISE 2: INHERITANCE ===")

"""
Exercise 2: Create a Vehicle Hierarchy

Create a base Vehicle class and derived classes:
1. Vehicle (base class)
2. Car (inherits from Vehicle)
3. Truck (inherits from Vehicle)
4. Motorcycle (inherits from Vehicle)

Each vehicle should have:
- Make, model, year
- Start/stop functionality
- Speed control
- Unique features for each type

Requirements:
- Use inheritance properly
- Override methods when appropriate
- Use super() to call parent methods
- Implement unique features for each vehicle type
"""

# Your solution here:
class Vehicle:
    """Base class for all vehicles"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._is_running = False
        self._speed = 0
    
    def start(self):
        """Start the vehicle"""
        if not self._is_running:
            self._is_running = True
            return f"{self.year} {self.make} {self.model} is now running"
        else:
            return "Vehicle is already running"
    
    def stop(self):
        """Stop the vehicle"""
        if self._is_running:
            self._is_running = False
            self._speed = 0
            return f"{self.year} {self.make} {self.model} has stopped"
        else:
            return "Vehicle is already stopped"
    
    def accelerate(self, speed_increase):
        """Accelerate the vehicle"""
        if self._is_running:
            self._speed += speed_increase
            return f"Accelerated to {self._speed} mph"
        else:
            return "Cannot accelerate - vehicle is not running"
    
    def brake(self, speed_decrease):
        """Brake the vehicle"""
        if self._speed > 0:
            self._speed = max(0, self._speed - speed_decrease)
            return f"Braked to {self._speed} mph"
        else:
            return "Vehicle is already stopped"
    
    def get_info(self):
        """Get vehicle information"""
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    """Car class inheriting from Vehicle"""
    
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors
        self._passengers = 0
    
    def open_door(self, door_number):
        """Open a specific door"""
        if 1 <= door_number <= self.doors:
            return f"Opened door {door_number}"
        else:
            return "Invalid door number"
    
    def get_info(self):
        """Override to include door count"""
        base_info = super().get_info()
        return f"{base_info} with {self.doors} doors"

class Truck(Vehicle):
    """Truck class inheriting from Vehicle"""
    
    def __init__(self, make, model, year, cargo_capacity):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity
        self._cargo = []
    
    def load_cargo(self, item):
        """Load cargo into truck"""
        if len(self._cargo) < self.cargo_capacity:
            self._cargo.append(item)
            return f"Loaded {item} into truck"
        else:
            return "Truck is at capacity"
    
    def unload_cargo(self, item):
        """Unload cargo from truck"""
        if item in self._cargo:
            self._cargo.remove(item)
            return f"Unloaded {item} from truck"
        else:
            return f"{item} not found in truck"
    
    def get_info(self):
        """Override to include cargo capacity"""
        base_info = super().get_info()
        return f"{base_info} with {self.cargo_capacity} cargo capacity"

class Motorcycle(Vehicle):
    """Motorcycle class inheriting from Vehicle"""
    
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size
        self._has_helmet = False
    
    def put_on_helmet(self):
        """Put on helmet"""
        self._has_helmet = True
        return "Helmet is on"
    
    def take_off_helmet(self):
        """Take off helmet"""
        self._has_helmet = False
        return "Helmet is off"
    
    def get_info(self):
        """Override to include engine size"""
        base_info = super().get_info()
        return f"{base_info} with {self.engine_size}cc engine"

# Test Exercise 2
print("=== Testing Exercise 2 ===")
vehicles = [
    Car("Toyota", "Camry", 2020, 4),
    Truck("Ford", "F-150", 2019, 5),
    Motorcycle("Honda", "CBR", 2021, 600)
]

for vehicle in vehicles:
    print(f"\n{vehicle.get_info()}")
    print(vehicle.start())
    print(vehicle.accelerate(30))
    print(vehicle.brake(10))
    print(vehicle.stop())

print("\n=== EXERCISE 3: POLYMORPHISM ===")

"""
Exercise 3: Create a Shape Hierarchy with Polymorphism

Create a base Shape class and derived classes:
1. Shape (abstract base class)
2. Rectangle (inherits from Shape)
3. Circle (inherits from Shape)
4. Triangle (inherits from Shape)

Each shape should implement:
- area() method
- perimeter() method
- get_info() method

Use polymorphism to:
- Calculate total area of all shapes
- Calculate total perimeter of all shapes
- Display information about all shapes

Requirements:
- Use abstract base classes
- Implement polymorphism
- Use method overriding
- Handle different shape types uniformly
"""

# Your solution here:
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for shapes"""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        """Calculate area"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter"""
        pass
    
    def get_info(self):
        """Get shape information"""
        return f"{self.name}: Area = {self.area():.2f}, Perimeter = {self.perimeter():.2f}"

class Rectangle(Shape):
    """Rectangle class implementing Shape"""
    
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate rectangle area"""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate rectangle perimeter"""
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Circle class implementing Shape"""
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        """Calculate circle area"""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculate circle perimeter"""
        return 2 * math.pi * self.radius

class Triangle(Shape):
    """Triangle class implementing Shape"""
    
    def __init__(self, base, height, side1, side2):
        super().__init__("Triangle")
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
    
    def area(self):
        """Calculate triangle area"""
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        """Calculate triangle perimeter"""
        return self.base + self.side1 + self.side2

# Test Exercise 3
print("=== Testing Exercise 3 ===")
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Triangle(6, 4, 5, 5),
    Rectangle(10, 7),
    Circle(3)
]

# Polymorphic behavior
total_area = sum(shape.area() for shape in shapes)
total_perimeter = sum(shape.perimeter() for shape in shapes)

print("Shape Information:")
for shape in shapes:
    print(shape.get_info())

print(f"\nTotal Area: {total_area:.2f}")
print(f"Total Perimeter: {total_perimeter:.2f}")

print("\n=== EXERCISE 4: ENCAPSULATION ===")

"""
Exercise 4: Create a Bank Account with Proper Encapsulation

Create a BankAccount class that demonstrates:
1. Private attributes
2. Public methods for controlled access
3. Data validation
4. Error handling
5. Property methods

Requirements:
- Use private attributes (_attribute)
- Implement getter and setter methods
- Validate all input data
- Handle errors gracefully
- Use properties for controlled access
"""

# Your solution here:
class BankAccount:
    """Bank account with proper encapsulation"""
    
    def __init__(self, account_number, account_holder, initial_balance=0):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = initial_balance
        self._transactions = []
        self._is_active = True
    
    @property
    def account_number(self):
        """Get account number"""
        return self._account_number
    
    @property
    def account_holder(self):
        """Get account holder"""
        return self._account_holder
    
    @property
    def balance(self):
        """Get current balance"""
        return self._balance
    
    @property
    def is_active(self):
        """Get account status"""
        return self._is_active
    
    def deposit(self, amount):
        """Deposit money into account"""
        if not self._is_active:
            return "Account is inactive"
        
        if self._validate_amount(amount):
            self._balance += amount
            self._record_transaction(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self._balance}"
        else:
            return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if not self._is_active:
            return "Account is inactive"
        
        if self._validate_amount(amount) and self._has_sufficient_funds(amount):
            self._balance -= amount
            self._record_transaction(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        else:
            return "Insufficient funds or invalid amount"
    
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
    
    def _validate_amount(self, amount):
        """Validate amount"""
        return isinstance(amount, (int, float)) and amount > 0
    
    def _has_sufficient_funds(self, amount):
        """Check if account has sufficient funds"""
        return amount <= self._balance
    
    def _record_transaction(self, transaction):
        """Record transaction"""
        self._transactions.append(transaction)

# Test Exercise 4
print("=== Testing Exercise 4 ===")
account = BankAccount("12345", "Alice", 1000)
print(f"Account: {account.account_number}, Holder: {account.account_holder}")
print(f"Initial balance: ${account.balance}")
print(account.deposit(500))
print(account.withdraw(200))
print(f"Current balance: ${account.balance}")
print(f"Transactions: {account.get_transactions()}")

print("\n=== EXERCISE 5: SPECIAL METHODS ===")

"""
Exercise 5: Create a Vector Class with Special Methods

Create a Vector class that implements:
1. __init__ for initialization
2. __str__ for string representation
3. __repr__ for developer representation
4. __add__ for vector addition
5. __sub__ for vector subtraction
6. __mul__ for scalar multiplication
7. __eq__ for equality comparison
8. __len__ for vector length
9. __getitem__ for indexing
10. __setitem__ for assignment

Requirements:
- Implement all special methods
- Handle different data types
- Provide meaningful representations
- Support mathematical operations
"""

# Your solution here:
class Vector:
    """Vector class with special methods"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """String representation"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """Developer representation"""
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        """Vector addition"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return Vector(self.x + other, self.y + other)
    
    def __sub__(self, other):
        """Vector subtraction"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            return Vector(self.x - other, self.y - other)
    
    def __mul__(self, scalar):
        """Scalar multiplication"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """Equality comparison"""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __len__(self):
        """Vector length (number of components)"""
        return 2
    
    def __getitem__(self, index):
        """Get component by index"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")
    
    def __setitem__(self, index, value):
        """Set component by index"""
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Vector index out of range")
    
    def magnitude(self):
        """Calculate vector magnitude"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

# Test Exercise 5
print("=== Testing Exercise 5 ===")
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 2: {v1 * 2}")
print(f"v1 == v2: {v1 == v2}")
print(f"Length of v1: {len(v1)}")
print(f"v1[0]: {v1[0]}")
print(f"v1[1]: {v1[1]}")
print(f"Magnitude of v1: {v1.magnitude()}")

print("\n=== EXERCISE SOLUTIONS COMPLETED ===")

print("""
Congratulations! You've completed all OOP exercises:

1. ✅ Library Management System - Basic class design
2. ✅ Vehicle Hierarchy - Inheritance patterns
3. ✅ Shape Hierarchy - Polymorphism with abstract classes
4. ✅ Bank Account - Encapsulation with private attributes
5. ✅ Vector Class - Special methods and operators

Key Learning Points:
- Class design and implementation
- Inheritance and method overriding
- Polymorphism and abstract classes
- Encapsulation and data hiding
- Special methods and operator overloading
- Error handling and validation
- Code organization and structure

Next Steps:
- Practice with more complex problems
- Implement design patterns
- Build real-world applications
- Continue learning and improving
""")

"""
Key Points to Remember:
1. Practice makes perfect - solve more problems
2. Understand the problem before coding
3. Design your classes carefully
4. Use OOP principles effectively
5. Test your code thoroughly
6. Learn from your mistakes
7. Keep practicing and improving
8. Build real-world projects
9. Follow best practices
10. Never stop learning
"""
