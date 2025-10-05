"""
🧬 OOP INHERITANCE - Advanced Inheritance
========================================

Advanced inheritance concepts including abstract base classes, method resolution order,
and complex inheritance patterns. Master these concepts for professional OOP! 🚀
"""

print("=== ABSTRACT BASE CLASSES ===")

# Abstract base classes define interfaces that must be implemented
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes"""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented by subclasses"""
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
        """Implement abstract method"""
        return self.width * self.height
    
    def perimeter(self):
        """Implement abstract method"""
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Circle class implementing Shape"""
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        """Implement abstract method"""
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Implement abstract method"""
        import math
        return 2 * math.pi * self.radius

# Test abstract base classes
print("=== Abstract Base Classes Example ===")
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Rectangle(10, 7)
]

for shape in shapes:
    print(shape.get_info())

print("\n=== METHOD RESOLUTION ORDER (MRO) ===")

# Method Resolution Order determines the order in which methods are searched
class A:
    """Class A"""
    
    def method(self):
        return "A.method()"

class B(A):
    """Class B inheriting from A"""
    
    def method(self):
        return "B.method()"

class C(A):
    """Class C inheriting from A"""
    
    def method(self):
        return "C.method()"

class D(B, C):
    """Class D inheriting from B and C"""
    
    def method(self):
        return "D.method()"

# Test MRO
print("=== Method Resolution Order Example ===")
d = D()
print(f"D().method(): {d.method()}")
print(f"MRO for D: {D.__mro__}")
print(f"MRO for D: {[cls.__name__ for cls in D.__mro__]}")

# MRO with super()
class A:
    """Class A with super()"""
    
    def method(self):
        return "A.method()"

class B(A):
    """Class B with super()"""
    
    def method(self):
        return f"B.method() -> {super().method()}"

class C(A):
    """Class C with super()"""
    
    def method(self):
        return f"C.method() -> {super().method()}"

class D(B, C):
    """Class D with super()"""
    
    def method(self):
        return f"D.method() -> {super().method()}"

# Test MRO with super()
print("\n=== MRO with super() ===")
d = D()
print(f"D().method(): {d.method()}")

print("\n=== MIXIN CLASSES ===")

# Mixin classes provide functionality to other classes
class TimestampMixin:
    """Mixin for timestamp functionality"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = None
        self.updated_at = None
    
    def set_created_at(self, timestamp):
        """Set creation timestamp"""
        self.created_at = timestamp
    
    def set_updated_at(self, timestamp):
        """Set update timestamp"""
        self.updated_at = timestamp
    
    def get_timestamps(self):
        """Get timestamps"""
        return f"Created: {self.created_at}, Updated: {self.updated_at}"

class LoggingMixin:
    """Mixin for logging functionality"""
    
    def log(self, message):
        """Log a message"""
        print(f"LOG: {message}")
    
    def log_action(self, action):
        """Log an action"""
        self.log(f"Action: {action}")

class User(TimestampMixin, LoggingMixin):
    """User class with mixins"""
    
    def __init__(self, name, email):
        super().__init__()
        self.name = name
        self.email = email
    
    def update_email(self, new_email):
        """Update user email"""
        self.email = new_email
        self.log_action("Email updated")
        self.set_updated_at("2023-12-01")
    
    def get_info(self):
        """Get user information"""
        return f"User: {self.name} ({self.email})"

# Test mixin classes
print("=== Mixin Classes Example ===")
user = User("Alice", "alice@example.com")
user.set_created_at("2023-11-01")
user.update_email("alice.new@example.com")
print(user.get_info())
print(user.get_timestamps())

print("\n=== COMPOSITION VS INHERITANCE ===")

# Composition: "has-a" relationship
class Engine:
    """Engine class"""
    
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.is_running = False
    
    def start(self):
        """Start engine"""
        self.is_running = True
        return "Engine started"
    
    def stop(self):
        """Stop engine"""
        self.is_running = False
        return "Engine stopped"
    
    def get_status(self):
        """Get engine status"""
        return f"Engine: {self.horsepower}HP, Running: {self.is_running}"

class Car:
    """Car class using composition"""
    
    def __init__(self, make, model, year, engine_horsepower):
        self.make = make
        self.model = model
        self.year = year
        self.engine = Engine(engine_horsepower)  # Composition
        self.is_running = False
    
    def start(self):
        """Start car"""
        if not self.is_running:
            self.engine.start()
            self.is_running = True
            return f"{self.year} {self.make} {self.model} is now running"
        else:
            return "Car is already running"
    
    def stop(self):
        """Stop car"""
        if self.is_running:
            self.engine.stop()
            self.is_running = False
            return f"{self.year} {self.make} {self.model} has stopped"
        else:
            return "Car is already stopped"
    
    def get_info(self):
        """Get car information"""
        return f"{self.year} {self.make} {self.model}, {self.engine.get_status()}"

# Test composition
print("=== Composition Example ===")
car = Car("Toyota", "Camry", 2020, 200)
print(car.get_info())
print(car.start())
print(car.stop())

print("\n=== INHERITANCE WITH PROPERTIES ===")

# Inheritance with properties
class Person:
    """Base class for persons"""
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        """Get person's name"""
        return self._name
    
    @name.setter
    def name(self, value):
        """Set person's name"""
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
        """Set person's age"""
        if isinstance(value, int) and 0 <= value <= 150:
            self._age = value
        else:
            raise ValueError("Age must be an integer between 0 and 150")
    
    def get_info(self):
        """Get person information"""
        return f"Name: {self._name}, Age: {self._age}"

class Employee(Person):
    """Employee class inheriting from Person"""
    
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self._employee_id = employee_id
        self._department = department
        self._salary = 0
    
    @property
    def employee_id(self):
        """Get employee ID"""
        return self._employee_id
    
    @property
    def department(self):
        """Get department"""
        return self._department
    
    @property
    def salary(self):
        """Get salary"""
        return self._salary
    
    @salary.setter
    def salary(self, value):
        """Set salary"""
        if isinstance(value, (int, float)) and value >= 0:
            self._salary = value
        else:
            raise ValueError("Salary must be a non-negative number")
    
    def get_info(self):
        """Override parent method"""
        base_info = super().get_info()
        return f"{base_info}, ID: {self._employee_id}, Department: {self._department}, Salary: ${self._salary}"

# Test inheritance with properties
print("=== Inheritance with Properties Example ===")
employee = Employee("Bob", 30, "E001", "Engineering")
employee.salary = 75000
print(employee.get_info())

print("\n=== INHERITANCE WITH SPECIAL METHODS ===")

# Inheritance with special methods
class Animal:
    """Base class for animals"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def __str__(self):
        """String representation"""
        return f"{self.name} is a {self.species}"
    
    def __repr__(self):
        """Developer representation"""
        return f"Animal('{self.name}', '{self.species}')"
    
    def __eq__(self, other):
        """Check equality"""
        if isinstance(other, Animal):
            return self.name == other.name and self.species == other.species
        return False
    
    def __hash__(self):
        """Hash for use in sets and dictionaries"""
        return hash((self.name, self.species))

class Dog(Animal):
    """Dog class inheriting from Animal"""
    
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def __str__(self):
        """Override string representation"""
        return f"{self.name} is a {self.breed} {self.species}"
    
    def __repr__(self):
        """Override developer representation"""
        return f"Dog('{self.name}', '{self.breed}')"
    
    def __eq__(self, other):
        """Override equality check"""
        if isinstance(other, Dog):
            return self.name == other.name and self.breed == other.breed
        return False
    
    def __hash__(self):
        """Override hash"""
        return hash((self.name, self.breed))

# Test inheritance with special methods
print("=== Inheritance with Special Methods Example ===")
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Labrador")
dog3 = Dog("Buddy", "Golden Retriever")

print(f"Dog 1: {dog1}")
print(f"Dog 1 repr: {repr(dog1)}")
print(f"Dog 1 == Dog 2: {dog1 == dog2}")
print(f"Dog 1 == Dog 3: {dog1 == dog3}")
print(f"Dog 1 hash: {hash(dog1)}")

print("\n=== INHERITANCE WITH CLASS METHODS ===")

# Inheritance with class methods
class Vehicle:
    """Base class for vehicles"""
    
    total_vehicles = 0
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Vehicle.total_vehicles += 1
    
    @classmethod
    def get_total_vehicles(cls):
        """Get total number of vehicles"""
        return cls.total_vehicles
    
    @classmethod
    def from_string(cls, vehicle_string):
        """Create vehicle from string"""
        make, model, year = vehicle_string.split(',')
        return cls(make.strip(), model.strip(), int(year.strip()))
    
    def get_info(self):
        """Get vehicle information"""
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    """Car class inheriting from Vehicle"""
    
    total_cars = 0
    
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors
        Car.total_cars += 1
    
    @classmethod
    def get_total_cars(cls):
        """Get total number of cars"""
        return cls.total_cars
    
    @classmethod
    def from_string(cls, car_string):
        """Create car from string"""
        make, model, year, doors = car_string.split(',')
        return cls(make.strip(), model.strip(), int(year.strip()), int(doors.strip()))
    
    def get_info(self):
        """Override parent method"""
        base_info = super().get_info()
        return f"{base_info} with {self.doors} doors"

# Test inheritance with class methods
print("=== Inheritance with Class Methods Example ===")
car1 = Car("Toyota", "Camry", 2020, 4)
car2 = Car("Honda", "Civic", 2019, 4)
car3 = Car.from_string("Ford, Mustang, 2021, 2")

print(f"Total vehicles: {Vehicle.get_total_vehicles()}")
print(f"Total cars: {Car.get_total_cars()}")
print(f"Car 1: {car1.get_info()}")
print(f"Car 2: {car2.get_info()}")
print(f"Car 3: {car3.get_info()}")

print("\n=== INHERITANCE WITH STATIC METHODS ===")

# Inheritance with static methods
class MathUtils:
    """Base class with static methods"""
    
    @staticmethod
    def add(a, b):
        """Add two numbers"""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers"""
        return a * b

class AdvancedMathUtils(MathUtils):
    """Advanced math utils inheriting from MathUtils"""
    
    @staticmethod
    def power(a, b):
        """Calculate power"""
        return a ** b
    
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
    def fibonacci(n):
        """Calculate Fibonacci number"""
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Test inheritance with static methods
print("=== Inheritance with Static Methods Example ==="")
print(f"Add 5 + 3: {AdvancedMathUtils.add(5, 3)}")
print(f"Multiply 4 * 7: {AdvancedMathUtils.multiply(4, 7)}")
print(f"Power 2^8: {AdvancedMathUtils.power(2, 8)}")
print(f"Factorial 5: {AdvancedMathUtils.factorial(5)}")
print(f"Fibonacci 10: {AdvancedMathUtils.fibonacci(10)}")

print("\n=== INHERITANCE BEST PRACTICES ===")

print("""
Advanced Inheritance Best Practices:
1. Use abstract base classes for common interfaces
2. Understand Method Resolution Order (MRO)
3. Use mixin classes for functionality
4. Prefer composition over inheritance when possible
5. Keep inheritance hierarchies shallow
6. Use super() consistently
7. Override special methods when appropriate
8. Test inheritance thoroughly
9. Document inheritance relationships
10. Follow the Liskov Substitution Principle
""")

# Example of advanced inheritance design
class DatabaseConnection:
    """Abstract base class for database connections"""
    
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.is_connected = False
    
    @abstractmethod
    def connect(self):
        """Connect to database"""
        pass
    
    @abstractmethod
    def disconnect(self):
        """Disconnect from database"""
        pass
    
    @abstractmethod
    def execute_query(self, query):
        """Execute database query"""
        pass

class MySQLConnection(DatabaseConnection):
    """MySQL database connection"""
    
    def connect(self):
        """Connect to MySQL database"""
        self.is_connected = True
        return f"Connected to MySQL: {self.connection_string}"
    
    def disconnect(self):
        """Disconnect from MySQL database"""
        self.is_connected = False
        return "Disconnected from MySQL"
    
    def execute_query(self, query):
        """Execute MySQL query"""
        if self.is_connected:
            return f"MySQL Query: {query}"
        else:
            return "Not connected to MySQL"

class PostgreSQLConnection(DatabaseConnection):
    """PostgreSQL database connection"""
    
    def connect(self):
        """Connect to PostgreSQL database"""
        self.is_connected = True
        return f"Connected to PostgreSQL: {self.connection_string}"
    
    def disconnect(self):
        """Disconnect from PostgreSQL database"""
        self.is_connected = False
        return "Disconnected from PostgreSQL"
    
    def execute_query(self, query):
        """Execute PostgreSQL query"""
        if self.is_connected:
            return f"PostgreSQL Query: {query}"
        else:
            return "Not connected to PostgreSQL"

# Test advanced inheritance design
print("=== Advanced Inheritance Design ===")
connections = [
    MySQLConnection("localhost:3306/mydb"),
    PostgreSQLConnection("localhost:5432/mydb")
]

for connection in connections:
    print(f"\n{connection.connect()}")
    print(connection.execute_query("SELECT * FROM users"))
    print(connection.disconnect())

"""
Key Points to Remember:
1. Use abstract base classes for common interfaces
2. Understand Method Resolution Order (MRO)
3. Use mixin classes for functionality
4. Prefer composition over inheritance when possible
5. Keep inheritance hierarchies shallow
6. Use super() consistently
7. Override special methods when appropriate
8. Test inheritance thoroughly
9. Document inheritance relationships
10. Follow the Liskov Substitution Principle
"""
