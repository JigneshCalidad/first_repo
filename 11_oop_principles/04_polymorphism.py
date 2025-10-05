"""
🎭 OOP PRINCIPLES - Polymorphism
================================

Polymorphism allows objects of different types to be treated as objects
of a common base type. It enables the same interface to work with different types! 🔄
"""

print("=== WHAT IS POLYMORPHISM? ===")

# Polymorphism means "many forms"
# The same interface can work with different types of objects

print("""
Polymorphism Concepts:
- Same interface, different implementations
- Method overriding in inheritance
- Duck typing in Python
- Operator overloading
- Function polymorphism
- Runtime polymorphism
""")

print("\n=== POLYMORPHISM WITH INHERITANCE ===")

# Polymorphism through inheritance
class Animal:
    """Base class for all animals"""
    
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        """Animal makes a sound"""
        return f"{self.name} makes a sound"
    
    def move(self):
        """Animal moves"""
        return f"{self.name} is moving"
    
    def get_info(self):
        """Get animal information"""
        return f"{self.name} is an animal"

class Dog(Animal):
    """Dog class inheriting from Animal"""
    
    def make_sound(self):
        """Override parent method"""
        return f"{self.name} barks: Woof! Woof!"
    
    def move(self):
        """Override parent method"""
        return f"{self.name} is running"
    
    def get_info(self):
        """Override parent method"""
        return f"{self.name} is a dog"

class Cat(Animal):
    """Cat class inheriting from Animal"""
    
    def make_sound(self):
        """Override parent method"""
        return f"{self.name} meows: Meow! Meow!"
    
    def move(self):
        """Override parent method"""
        return f"{self.name} is walking"
    
    def get_info(self):
        """Override parent method"""
        return f"{self.name} is a cat"

class Bird(Animal):
    """Bird class inheriting from Animal"""
    
    def make_sound(self):
        """Override parent method"""
        return f"{self.name} chirps: Tweet! Tweet!"
    
    def move(self):
        """Override parent method"""
        return f"{self.name} is flying"
    
    def get_info(self):
        """Override parent method"""
        return f"{self.name} is a bird"

# Test polymorphism with inheritance
print("=== Polymorphism with Inheritance ===")
animals = [
    Dog("Buddy"),
    Cat("Whiskers"),
    Bird("Tweety"),
    Dog("Max"),
    Cat("Fluffy")
]

# Same interface, different implementations
for animal in animals:
    print(f"{animal.get_info()}")
    print(f"  Sound: {animal.make_sound()}")
    print(f"  Movement: {animal.move()}")
    print()

print("\n=== POLYMORPHISM WITH DUCK TYPING ===")

# Duck typing: "If it walks like a duck and quacks like a duck, it's a duck"
class Duck:
    """Duck class"""
    
    def quack(self):
        """Duck quacks"""
        return "Quack! Quack!"
    
    def walk(self):
        """Duck walks"""
        return "Waddle, waddle"

class Person:
    """Person class"""
    
    def quack(self):
        """Person quacks (imitating duck)"""
        return "Quack! Quack! (imitating duck)"
    
    def walk(self):
        """Person walks"""
        return "Step, step"

class Robot:
    """Robot class"""
    
    def quack(self):
        """Robot quacks (synthesized)"""
        return "Quack! Quack! (synthesized)"
    
    def walk(self):
        """Robot walks"""
        return "Beep, beep, step"

# Function that works with any object that has quack() and walk() methods
def make_it_quack_and_walk(creature):
    """Make any creature quack and walk"""
    print(f"Creature: {creature.__class__.__name__}")
    print(f"  Sound: {creature.quack()}")
    print(f"  Movement: {creature.walk()}")
    print()

# Test duck typing
print("=== Duck Typing Example ===")
creatures = [Duck(), Person(), Robot()]

for creature in creatures:
    make_it_quack_and_walk(creature)

print("\n=== POLYMORPHISM WITH OPERATOR OVERLOADING ===")

# Operator overloading for polymorphism
class Vector:
    """Vector class with operator overloading"""
    
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
    
    def __eq__(self, other):
        """Overload == operator"""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __str__(self):
        """String representation"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """Developer representation"""
        return f"Vector({self.x}, {self.y})"

# Test operator overloading
print("=== Operator Overloading Example ===")
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 2: {v1 * 2}")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == Vector(3, 4): {v1 == Vector(3, 4)}")

print("\n=== POLYMORPHISM WITH ABSTRACT BASE CLASSES ===")

# Abstract base classes for polymorphism
from abc import ABC, abstractmethod

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
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculate circle perimeter"""
        import math
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

# Test polymorphism with abstract base classes
print("=== Polymorphism with Abstract Base Classes ===")
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Triangle(6, 4, 5, 5),
    Rectangle(10, 7),
    Circle(3)
]

# Same interface, different implementations
for shape in shapes:
    print(shape.get_info())

print("\n=== POLYMORPHISM WITH FUNCTION OVERLOADING ===")

# Function polymorphism (Python doesn't have true function overloading)
class Calculator:
    """Calculator class with polymorphic methods"""
    
    def add(self, a, b=None):
        """Add two numbers or a number to a list"""
        if b is None:
            if isinstance(a, (list, tuple)):
                return sum(a)
            else:
                return a
        else:
            return a + b
    
    def multiply(self, a, b=None):
        """Multiply two numbers or a number by a list"""
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

# Test function polymorphism
print("=== Function Polymorphism Example ===")
calc = Calculator()

print(f"Add 5 + 3: {calc.add(5, 3)}")
print(f"Add list [1, 2, 3, 4]: {calc.add([1, 2, 3, 4])}")
print(f"Multiply 4 * 7: {calc.multiply(4, 7)}")
print(f"Multiply list [2, 3, 4]: {calc.multiply([2, 3, 4])}")
print(f"Calculate add 10 + 5: {calc.calculate('add', 10, 5)}")
print(f"Calculate subtract 10 - 5: {calc.calculate('subtract', 10, 5)}")

print("\n=== POLYMORPHISM WITH INTERFACES ===")

# Interface-like polymorphism
class Drawable:
    """Interface for drawable objects"""
    
    def draw(self):
        """Draw the object"""
        pass
    
    def get_color(self):
        """Get object color"""
        pass

class Circle(Drawable):
    """Circle implementing Drawable"""
    
    def __init__(self, radius, color="red"):
        self.radius = radius
        self.color = color
    
    def draw(self):
        """Draw circle"""
        return f"Drawing a {self.color} circle with radius {self.radius}"
    
    def get_color(self):
        """Get circle color"""
        return self.color

class Rectangle(Drawable):
    """Rectangle implementing Drawable"""
    
    def __init__(self, width, height, color="blue"):
        self.width = width
        self.height = height
        self.color = color
    
    def draw(self):
        """Draw rectangle"""
        return f"Drawing a {self.color} rectangle {self.width}x{self.height}"
    
    def get_color(self):
        """Get rectangle color"""
        return self.color

class Triangle(Drawable):
    """Triangle implementing Drawable"""
    
    def __init__(self, base, height, color="green"):
        self.base = base
        self.height = height
        self.color = color
    
    def draw(self):
        """Draw triangle"""
        return f"Drawing a {self.color} triangle with base {self.base} and height {self.height}"
    
    def get_color(self):
        """Get triangle color"""
        return self.color

# Test interface-like polymorphism
print("=== Interface-like Polymorphism ===")
drawable_objects = [
    Circle(5, "red"),
    Rectangle(10, 7, "blue"),
    Triangle(8, 6, "green"),
    Circle(3, "yellow"),
    Rectangle(4, 4, "purple")
]

# Same interface, different implementations
for obj in drawable_objects:
    print(f"{obj.draw()}")
    print(f"  Color: {obj.get_color()}")
    print()

print("\n=== POLYMORPHISM WITH RUNTIME BEHAVIOR ===")

# Runtime polymorphism
class Animal:
    """Base class for animals"""
    
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        """Animal makes a sound"""
        return f"{self.name} makes a sound"
    
    def move(self):
        """Animal moves"""
        return f"{self.name} is moving"

class Dog(Animal):
    """Dog class"""
    
    def make_sound(self):
        """Dog barks"""
        return f"{self.name} barks: Woof! Woof!"
    
    def move(self):
        """Dog runs"""
        return f"{self.name} is running"

class Cat(Animal):
    """Cat class"""
    
    def make_sound(self):
        """Cat meows"""
        return f"{self.name} meows: Meow! Meow!"
    
    def move(self):
        """Cat walks"""
        return f"{self.name} is walking"

class Bird(Animal):
    """Bird class"""
    
    def make_sound(self):
        """Bird chirps"""
        return f"{self.name} chirps: Tweet! Tweet!"
    
    def move(self):
        """Bird flies"""
        return f"{self.name} is flying"

# Function that works with any animal
def animal_show(animal):
    """Show animal behavior"""
    print(f"Animal: {animal.name}")
    print(f"  Sound: {animal.make_sound()}")
    print(f"  Movement: {animal.move()}")
    print()

# Test runtime polymorphism
print("=== Runtime Polymorphism ===")
animals = [Dog("Buddy"), Cat("Whiskers"), Bird("Tweety")]

for animal in animals:
    animal_show(animal)

print("\n=== POLYMORPHISM BEST PRACTICES ===")

print("""
Polymorphism Best Practices:
1. Use polymorphism for code reusability
2. Design interfaces that are easy to implement
3. Use abstract base classes for common interfaces
4. Follow the Liskov Substitution Principle
5. Use duck typing when appropriate
6. Override methods consistently
7. Test polymorphism thoroughly
8. Document polymorphic behavior
9. Use meaningful method names
10. Keep interfaces simple and focused
""")

# Example of good polymorphism design
class PaymentProcessor:
    """Base class for payment processors"""
    
    def process_payment(self, amount):
        """Process payment"""
        pass
    
    def get_payment_info(self):
        """Get payment information"""
        pass

class CreditCardProcessor(PaymentProcessor):
    """Credit card payment processor"""
    
    def __init__(self, card_number, expiry_date):
        self.card_number = card_number
        self.expiry_date = expiry_date
    
    def process_payment(self, amount):
        """Process credit card payment"""
        return f"Processing ${amount} with credit card ending in {self.card_number[-4:]}"
    
    def get_payment_info(self):
        """Get credit card info"""
        return f"Credit Card: ****{self.card_number[-4:]}"

class PayPalProcessor(PaymentProcessor):
    """PayPal payment processor"""
    
    def __init__(self, email):
        self.email = email
    
    def process_payment(self, amount):
        """Process PayPal payment"""
        return f"Processing ${amount} with PayPal account {self.email}"
    
    def get_payment_info(self):
        """Get PayPal info"""
        return f"PayPal: {self.email}"

class BankTransferProcessor(PaymentProcessor):
    """Bank transfer payment processor"""
    
    def __init__(self, account_number, routing_number):
        self.account_number = account_number
        self.routing_number = routing_number
    
    def process_payment(self, amount):
        """Process bank transfer"""
        return f"Processing ${amount} with bank transfer to account {self.account_number}"
    
    def get_payment_info(self):
        """Get bank transfer info"""
        return f"Bank Transfer: Account {self.account_number}"

# Test payment processor polymorphism
print("=== Payment Processor Polymorphism ===")
processors = [
    CreditCardProcessor("1234567890123456", "12/25"),
    PayPalProcessor("user@example.com"),
    BankTransferProcessor("987654321", "123456789")
]

for processor in processors:
    print(f"{processor.get_payment_info()}")
    print(f"  {processor.process_payment(100)}")
    print()

"""
Key Points to Remember:
1. Polymorphism allows same interface for different types
2. Use inheritance for method overriding
3. Use duck typing for flexible interfaces
4. Use abstract base classes for common interfaces
5. Override methods consistently
6. Test polymorphism thoroughly
7. Follow the Liskov Substitution Principle
8. Use meaningful method names
9. Keep interfaces simple and focused
10. Practice with real-world examples
"""
