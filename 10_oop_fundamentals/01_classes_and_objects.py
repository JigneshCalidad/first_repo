"""
🏗️ OOP FUNDAMENTALS - Classes and Objects
=========================================

Object-Oriented Programming (OOP) is a programming paradigm based on objects.
Think of objects as real-world entities with properties and behaviors! 🎯
"""

print("=== WHAT IS OOP? ===")

# OOP is a way of organizing code using objects
# Objects have:
# 1. Attributes (properties/data)
# 2. Methods (functions/behaviors)

print("""
OOP Concepts:
- Class: Blueprint for creating objects
- Object: Instance of a class
- Attributes: Data/properties of an object
- Methods: Functions/behaviors of an object
- Encapsulation: Bundling data and methods together
- Abstraction: Hiding complex implementation details
- Inheritance: Creating new classes from existing ones
- Polymorphism: Same interface, different implementations
""")

print("\n=== CREATING YOUR FIRST CLASS ===")

# Basic class definition
class Dog:
    """A simple Dog class"""
    
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """Initialize a new Dog instance"""
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
        self.is_hungry = True
    
    def bark(self):
        """Make the dog bark"""
        return f"{self.name} says Woof! Woof!"
    
    def eat(self):
        """Feed the dog"""
        if self.is_hungry:
            self.is_hungry = False
            return f"{self.name} is eating and is no longer hungry!"
        else:
            return f"{self.name} is not hungry right now."
    
    def sleep(self):
        """Make the dog sleep"""
        return f"{self.name} is sleeping peacefully... 😴"
    
    def get_info(self):
        """Get information about the dog"""
        return f"{self.name} is {self.age} years old and is a {self.species}"

# Create objects (instances) of the Dog class
print("Creating Dog objects:")
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
dog3 = Dog("Luna", 2)

print(f"Dog 1: {dog1.get_info()}")
print(f"Dog 2: {dog2.get_info()}")
print(f"Dog 3: {dog3.get_info()}")

print("\n=== WORKING WITH OBJECTS ===")

# Access attributes
print(f"Dog1's name: {dog1.name}")
print(f"Dog1's age: {dog1.age}")
print(f"Dog1's species: {dog1.species}")

# Call methods
print(f"\n{dog1.bark()}")
print(f"{dog1.eat()}")
print(f"{dog1.sleep()}")

# Modify attributes
dog1.age = 4
print(f"Updated age: {dog1.get_info()}")

print("\n=== CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES ===")

# Class attributes are shared by all instances
print(f"All dogs are: {Dog.species}")
print(f"Dog1 species: {dog1.species}")
print(f"Dog2 species: {dog2.species}")

# Instance attributes are unique to each instance
print(f"Dog1 name: {dog1.name}")
print(f"Dog2 name: {dog2.name}")

# Modify class attribute
Dog.species = "Canis lupus"
print(f"Updated species for all dogs: {dog1.species}")

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Bank Account
class BankAccount:
    """A simple bank account class"""
    
    def __init__(self, account_number, owner_name, initial_balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance
        self.transactions = []
    
    def deposit(self, amount):
        """Deposit money into account"""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        """Get current balance"""
        return f"Balance: ${self.balance}"
    
    def get_transactions(self):
        """Get transaction history"""
        return self.transactions
    
    def get_account_info(self):
        """Get account information"""
        return f"Account: {self.account_number}, Owner: {self.owner_name}, Balance: ${self.balance}"

# Test BankAccount
print("=== Bank Account Example ===")
account = BankAccount("12345", "Alice", 1000)
print(account.get_account_info())
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())
print("Transactions:", account.get_transactions())

# Example 2: Student
class Student:
    """A student class for managing student information"""
    
    def __init__(self, student_id, name, grade_level):
        self.student_id = student_id
        self.name = name
        self.grade_level = grade_level
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
    
    def get_gpa(self):
        """Calculate GPA"""
        if not self.grades:
            return "No grades available"
        
        total_points = sum(self.grades.values())
        return total_points / len(self.grades)
    
    def get_student_info(self):
        """Get student information"""
        return f"Student: {self.name} (ID: {self.student_id}), Grade: {self.grade_level}"

# Test Student
print("\n=== Student Example ===")
student = Student("S001", "Bob", "Senior")
print(student.get_student_info())
print(student.enroll_course("Python Programming"))
print(student.enroll_course("Data Structures"))
print(student.add_grade("Python Programming", 95))
print(student.add_grade("Data Structures", 88))
print(f"GPA: {student.get_gpa():.2f}")

print("\n=== SPECIAL METHODS ===")

# Special methods (dunder methods) start and end with double underscores
class Person:
    """A person class with special methods"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """String representation of the object"""
        return f"Person(name='{self.name}', age={self.age})"
    
    def __repr__(self):
        """Developer representation of the object"""
        return f"Person('{self.name}', {self.age})"
    
    def __len__(self):
        """Length of the person (age)"""
        return self.age
    
    def __eq__(self, other):
        """Check if two persons are equal"""
        return self.name == other.name and self.age == other.age

# Test special methods
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
person3 = Person("Alice", 25)

print(f"Person 1: {person1}")
print(f"Person 1 repr: {repr(person1)}")
print(f"Person 1 length: {len(person1)}")
print(f"Person 1 == Person 2: {person1 == person2}")
print(f"Person 1 == Person 3: {person1 == person3}")

print("\n=== CLASS METHODS AND STATIC METHODS ===")

class Circle:
    """A circle class with class and static methods"""
    
    pi = 3.14159
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """Calculate area of the circle"""
        return Circle.pi * self.radius ** 2
    
    def circumference(self):
        """Calculate circumference of the circle"""
        return 2 * Circle.pi * self.radius
    
    @classmethod
    def from_diameter(cls, diameter):
        """Create circle from diameter"""
        return cls(diameter / 2)
    
    @staticmethod
    def is_valid_radius(radius):
        """Check if radius is valid"""
        return radius > 0
    
    def __str__(self):
        return f"Circle(radius={self.radius})"

# Test Circle class
print("=== Circle Example ===")
circle1 = Circle(5)
print(f"Circle 1: {circle1}")
print(f"Area: {circle1.area():.2f}")
print(f"Circumference: {circle1.circumference():.2f}")

# Create circle from diameter
circle2 = Circle.from_diameter(10)
print(f"Circle 2 (from diameter): {circle2}")

# Static method
print(f"Radius 5 is valid: {Circle.is_valid_radius(5)}")
print(f"Radius -2 is valid: {Circle.is_valid_radius(-2)}")

print("\n=== OOP BEST PRACTICES ===")

print("""
OOP Best Practices:
1. Use descriptive class and method names
2. Write clear docstrings for classes and methods
3. Keep classes focused on a single responsibility
4. Use meaningful attribute names
5. Initialize all attributes in __init__
6. Use private attributes (_attribute) when appropriate
7. Write getter and setter methods when needed
8. Test your classes thoroughly
9. Use inheritance to avoid code duplication
10. Follow the DRY principle (Don't Repeat Yourself)
""")

# Example of good OOP design
class Rectangle:
    """A rectangle class with proper encapsulation"""
    
    def __init__(self, width, height):
        """Initialize rectangle with width and height"""
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self._width = width
        self._height = height
    
    @property
    def width(self):
        """Get rectangle width"""
        return self._width
    
    @width.setter
    def width(self, value):
        """Set rectangle width"""
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value
    
    @property
    def height(self):
        """Get rectangle height"""
        return self._height
    
    @height.setter
    def height(self, value):
        """Set rectangle height"""
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value
    
    def area(self):
        """Calculate rectangle area"""
        return self._width * self._height
    
    def perimeter(self):
        """Calculate rectangle perimeter"""
        return 2 * (self._width + self._height)
    
    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"

# Test Rectangle
print("=== Rectangle Example ===")
try:
    rect = Rectangle(5, 3)
    print(f"Rectangle: {rect}")
    print(f"Area: {rect.area()}")
    print(f"Perimeter: {rect.perimeter()}")
    
    # Use properties
    rect.width = 7
    print(f"Updated width: {rect.width}")
    print(f"New area: {rect.area()}")
    
except ValueError as e:
    print(f"Error: {e}")

"""
Key Points to Remember:
1. Classes are blueprints for creating objects
2. Objects are instances of classes
3. Attributes store data, methods define behavior
4. Use __init__ to initialize objects
5. Use self to refer to the current instance
6. Class attributes are shared, instance attributes are unique
7. Use special methods (__str__, __repr__, etc.) for custom behavior
8. Use @classmethod and @staticmethod for class-level methods
9. Follow OOP principles for better code organization
10. Practice with real-world examples
"""
