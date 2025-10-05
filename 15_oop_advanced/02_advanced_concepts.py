"""
🚀 OOP ADVANCED - Advanced Concepts
===================================

Advanced OOP concepts including metaclasses, descriptors, context managers,
and other powerful Python features for professional development! 💪
"""

print("=== METACLASSES ===")

# Metaclasses are classes that create other classes
class SingletonMeta(type):
    """Metaclass for singleton pattern"""
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        """Create instance only if none exists"""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    """Database class using singleton metaclass"""
    
    def __init__(self):
        self.connection = "Database connection"
        self.data = {}
    
    def connect(self):
        """Connect to database"""
        return self.connection
    
    def store(self, key, value):
        """Store data"""
        self.data[key] = value
        return f"Stored {key} = {value}"
    
    def retrieve(self, key):
        """Retrieve data"""
        return self.data.get(key, "Key not found")

# Test metaclass
print("=== Metaclass Example ===")
db1 = Database()
db2 = Database()

print(f"Same instance: {db1 is db2}")
print(db1.store("user", "Alice"))
print(db2.store("age", 25))
print(f"Data from db1: {db1.data}")
print(f"Data from db2: {db2.data}")

print("\n=== DESCRIPTORS ===")

# Descriptors control attribute access
class Descriptor:
    """Descriptor class"""
    
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        """Get attribute value"""
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)
    
    def __set__(self, instance, value):
        """Set attribute value with validation"""
        if not isinstance(value, str):
            raise TypeError("Value must be a string")
        if len(value) < 2:
            raise ValueError("Value must be at least 2 characters long")
        instance.__dict__[self.name] = value
    
    def __delete__(self, instance):
        """Delete attribute"""
        instance.__dict__.pop(self.name, None)

class Person:
    """Person class using descriptors"""
    
    name = Descriptor("name")
    email = Descriptor("email")
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def get_info(self):
        """Get person information"""
        return f"Name: {self.name}, Email: {self.email}"

# Test descriptors
print("=== Descriptor Example ===")
person = Person("Alice", "alice@example.com")
print(person.get_info())

try:
    person.name = "A"  # Too short
except ValueError as e:
    print(f"Error: {e}")

try:
    person.name = 123  # Not a string
except TypeError as e:
    print(f"Error: {e}")

person.name = "Alice Smith"
print(f"Updated name: {person.name}")

print("\n=== CONTEXT MANAGERS ===")

# Context managers handle resource management
class DatabaseConnection:
    """Database connection context manager"""
    
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
    
    def __enter__(self):
        """Enter context"""
        print(f"Connecting to {self.connection_string}")
        self.connection = f"Connection to {self.connection_string}"
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context"""
        print(f"Closing connection to {self.connection_string}")
        self.connection = None
        if exc_type:
            print(f"Exception occurred: {exc_type.__name__}: {exc_val}")
        return False  # Don't suppress exceptions
    
    def execute_query(self, query):
        """Execute query"""
        if self.connection:
            return f"Executing: {query}"
        else:
            return "Not connected"

# Test context manager
print("=== Context Manager Example ===")
with DatabaseConnection("localhost:5432/mydb") as db:
    print(db.execute_query("SELECT * FROM users"))
    print(db.execute_query("INSERT INTO users VALUES ('Alice', 25)"))

print("Connection closed automatically")

print("\n=== PROPERTY DESCRIPTORS ===")

# Property descriptors for controlled attribute access
class Temperature:
    """Temperature class with property descriptors"""
    
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

# Test property descriptors
print("=== Property Descriptor Example ===")
temp = Temperature(25)
print(f"Initial: {temp.celsius}°C, {temp.fahrenheit}°F, {temp.kelvin}K")

temp.celsius = 30
print(f"After setting Celsius to 30: {temp.celsius}°C, {temp.fahrenheit}°F, {temp.kelvin}K")

temp.fahrenheit = 86
print(f"After setting Fahrenheit to 86: {temp.celsius}°C, {temp.fahrenheit}°F, {temp.kelvin}K")

print("\n=== CLASS METHODS AND STATIC METHODS ===")

# Advanced class methods and static methods
class MathUtils:
    """Math utilities with class and static methods"""
    
    pi = 3.14159
    
    def __init__(self, precision=2):
        self.precision = precision
    
    @classmethod
    def from_string(cls, math_string):
        """Create MathUtils from string"""
        precision = int(math_string.split(':')[1])
        return cls(precision)
    
    @classmethod
    def get_pi(cls):
        """Get pi value"""
        return cls.pi
    
    @staticmethod
    def add(a, b):
        """Add two numbers"""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers"""
        return a * b
    
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
    
    def format_number(self, number):
        """Format number with precision"""
        return f"{number:.{self.precision}f}"

# Test class and static methods
print("=== Class and Static Methods Example ===")
math_utils = MathUtils(3)
print(f"Pi: {MathUtils.get_pi()}")
print(f"Add 5 + 3: {MathUtils.add(5, 3)}")
print(f"Multiply 4 * 7: {MathUtils.multiply(4, 7)}")
print(f"Factorial 5: {MathUtils.factorial(5)}")
print(f"Formatted number: {math_utils.format_number(3.14159)}")

math_utils2 = MathUtils.from_string("MathUtils:4")
print(f"From string precision: {math_utils2.precision}")

print("\n=== SPECIAL METHODS (DUNDER METHODS) ===")

# Advanced special methods
class Vector:
    """Vector class with advanced special methods"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Overload + operator"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return Vector(self.x + other, self.y + other)
    
    def __sub__(self, other):
        """Overload - operator"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            return Vector(self.x - other, self.y - other)
    
    def __mul__(self, scalar):
        """Overload * operator"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        """Overload / operator"""
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return Vector(self.x / scalar, self.y / scalar)
    
    def __eq__(self, other):
        """Overload == operator"""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __lt__(self, other):
        """Overload < operator"""
        if isinstance(other, Vector):
            return self.magnitude() < other.magnitude()
        return False
    
    def __le__(self, other):
        """Overload <= operator"""
        if isinstance(other, Vector):
            return self.magnitude() <= other.magnitude()
        return False
    
    def __gt__(self, other):
        """Overload > operator"""
        if isinstance(other, Vector):
            return self.magnitude() > other.magnitude()
        return False
    
    def __ge__(self, other):
        """Overload >= operator"""
        if isinstance(other, Vector):
            return self.magnitude() >= other.magnitude()
        return False
    
    def __str__(self):
        """String representation"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """Developer representation"""
        return f"Vector({self.x}, {self.y})"
    
    def __len__(self):
        """Length of vector"""
        return 2
    
    def __getitem__(self, index):
        """Get item by index"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")
    
    def __setitem__(self, index, value):
        """Set item by index"""
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Vector index out of range")
    
    def __iter__(self):
        """Make vector iterable"""
        return iter([self.x, self.y])
    
    def __contains__(self, value):
        """Check if value is in vector"""
        return value in [self.x, self.y]
    
    def magnitude(self):
        """Calculate vector magnitude"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

# Test special methods
print("=== Special Methods Example ===")
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 2: {v1 * 2}")
print(f"v1 / 2: {v1 / 2}")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 < v2: {v1 < v2}")
print(f"v1 > v2: {v1 > v2}")
print(f"Length of v1: {len(v1)}")
print(f"v1[0]: {v1[0]}")
print(f"v1[1]: {v1[1]}")
print(f"Iterating v1: {list(v1)}")
print(f"3 in v1: {3 in v1}")
print(f"5 in v1: {5 in v1}")

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
        return f"Engine started ({self.horsepower}HP)"
    
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

print("\n=== ADVANCED OOP BEST PRACTICES ===")

print("""
Advanced OOP Best Practices:
1. Use metaclasses sparingly and document their purpose
2. Use descriptors for controlled attribute access
3. Use context managers for resource management
4. Override special methods when appropriate
5. Use composition over inheritance when possible
6. Follow the Single Responsibility Principle
7. Keep classes focused and cohesive
8. Use meaningful names and documentation
9. Test advanced features thoroughly
10. Practice with real-world examples
""")

# Example of advanced OOP design
class Logger:
    """Advanced logger with multiple features"""
    
    def __init__(self, name):
        self.name = name
        self.logs = []
        self.level = "INFO"
    
    def set_level(self, level):
        """Set log level"""
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if level in valid_levels:
            self.level = level
            return f"Log level set to {level}"
        else:
            raise ValueError(f"Invalid log level. Must be one of: {valid_levels}")
    
    def log(self, message, level="INFO"):
        """Log a message"""
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        self.logs.append(log_entry)
        print(log_entry)
    
    def get_logs(self, level=None):
        """Get logs, optionally filtered by level"""
        if level:
            return [log for log in self.logs if f"[{level}]" in log]
        return self.logs.copy()
    
    def clear_logs(self):
        """Clear all logs"""
        self.logs.clear()
        return "Logs cleared"
    
    def __str__(self):
        """String representation"""
        return f"Logger: {self.name}, Level: {self.level}, Logs: {len(self.logs)}"
    
    def __repr__(self):
        """Developer representation"""
        return f"Logger('{self.name}')"

# Test advanced logger
print("=== Advanced Logger Example ===")
logger = Logger("MyApp")
print(logger.set_level("DEBUG"))
logger.log("Application started", "INFO")
logger.log("Debug information", "DEBUG")
logger.log("Warning message", "WARNING")
logger.log("Error occurred", "ERROR")

print(f"\n{logger}")
print(f"All logs: {len(logger.get_logs())}")
print(f"Error logs: {len(logger.get_logs('ERROR'))}")

"""
Key Points to Remember:
1. Metaclasses control class creation
2. Descriptors control attribute access
3. Context managers handle resource management
4. Special methods define object behavior
5. Use composition over inheritance when possible
6. Follow OOP principles and best practices
7. Test advanced features thoroughly
8. Document your code clearly
9. Practice with real-world examples
10. Keep learning and improving
"""
