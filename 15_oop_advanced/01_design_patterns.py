"""
🏗️ OOP ADVANCED - Design Patterns
=================================

Design patterns are reusable solutions to common problems in software design.
Learn these patterns to write better, more maintainable code! 🎯
"""

print("=== WHAT ARE DESIGN PATTERNS? ===")

# Design patterns are proven solutions to common design problems
# They provide a common vocabulary and best practices

print("""
Design Pattern Categories:
- Creational: Object creation patterns
- Structural: Object composition patterns
- Behavioral: Object interaction patterns

Benefits:
- Reusable solutions
- Common vocabulary
- Best practices
- Improved code quality
- Easier maintenance
""")

print("\n=== SINGLETON PATTERN ===")

# Singleton ensures only one instance of a class exists
class Singleton:
    """Singleton pattern implementation"""
    
    _instance = None
    _initialized = False
    
    def __new__(cls):
        """Create new instance only if none exists"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Initialize only once"""
        if not self._initialized:
            self.data = {}
            self._initialized = True
    
    def set_data(self, key, value):
        """Set data in singleton"""
        self.data[key] = value
        return f"Set {key} = {value}"
    
    def get_data(self, key):
        """Get data from singleton"""
        return self.data.get(key, "Key not found")
    
    def get_all_data(self):
        """Get all data from singleton"""
        return self.data.copy()

# Test singleton pattern
print("=== Singleton Pattern Example ===")
singleton1 = Singleton()
singleton2 = Singleton()

print(f"Same instance: {singleton1 is singleton2}")
print(singleton1.set_data("name", "Alice"))
print(singleton2.set_data("age", 25))
print(f"Data from singleton1: {singleton1.get_all_data()}")
print(f"Data from singleton2: {singleton2.get_all_data()}")

print("\n=== FACTORY PATTERN ===")

# Factory pattern creates objects without specifying their exact class
class Animal:
    """Base class for animals"""
    
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        """Animal makes a sound"""
        return f"{self.name} makes a sound"

class Dog(Animal):
    """Dog class"""
    
    def make_sound(self):
        """Dog barks"""
        return f"{self.name} barks: Woof! Woof!"

class Cat(Animal):
    """Cat class"""
    
    def make_sound(self):
        """Cat meows"""
        return f"{self.name} meows: Meow! Meow!"

class Bird(Animal):
    """Bird class"""
    
    def make_sound(self):
        """Bird chirps"""
        return f"{self.name} chirps: Tweet! Tweet!"

class AnimalFactory:
    """Factory for creating animals"""
    
    @staticmethod
    def create_animal(animal_type, name):
        """Create animal based on type"""
        if animal_type.lower() == "dog":
            return Dog(name)
        elif animal_type.lower() == "cat":
            return Cat(name)
        elif animal_type.lower() == "bird":
            return Bird(name)
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")
    
    @staticmethod
    def get_available_types():
        """Get available animal types"""
        return ["dog", "cat", "bird"]

# Test factory pattern
print("=== Factory Pattern Example ===")
factory = AnimalFactory()
print(f"Available types: {factory.get_available_types()}")

animals = [
    factory.create_animal("dog", "Buddy"),
    factory.create_animal("cat", "Whiskers"),
    factory.create_animal("bird", "Tweety")
]

for animal in animals:
    print(f"{animal.name}: {animal.make_sound()}")

print("\n=== OBSERVER PATTERN ===")

# Observer pattern defines a one-to-many dependency between objects
class Subject:
    """Subject class for observer pattern"""
    
    def __init__(self):
        self._observers = []
        self._state = None
    
    def attach(self, observer):
        """Attach an observer"""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        """Detach an observer"""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self):
        """Notify all observers"""
        for observer in self._observers:
            observer.update(self)
    
    def set_state(self, state):
        """Set state and notify observers"""
        self._state = state
        self.notify()
    
    def get_state(self):
        """Get current state"""
        return self._state

class Observer:
    """Observer interface"""
    
    def update(self, subject):
        """Update observer"""
        pass

class ConcreteObserver(Observer):
    """Concrete observer implementation"""
    
    def __init__(self, name):
        self.name = name
    
    def update(self, subject):
        """Update observer with subject state"""
        print(f"{self.name} received update: {subject.get_state()}")

# Test observer pattern
print("=== Observer Pattern Example ===")
subject = Subject()

observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")
observer3 = ConcreteObserver("Observer 3")

subject.attach(observer1)
subject.attach(observer2)
subject.attach(observer3)

subject.set_state("State 1")
subject.set_state("State 2")

subject.detach(observer2)
subject.set_state("State 3")

print("\n=== STRATEGY PATTERN ===")

# Strategy pattern defines a family of algorithms and makes them interchangeable
class PaymentStrategy:
    """Base class for payment strategies"""
    
    def pay(self, amount):
        """Process payment"""
        pass

class CreditCardPayment(PaymentStrategy):
    """Credit card payment strategy"""
    
    def __init__(self, card_number):
        self.card_number = card_number
    
    def pay(self, amount):
        """Process credit card payment"""
        return f"Paid ${amount} with credit card ending in {self.card_number[-4:]}"

class PayPalPayment(PaymentStrategy):
    """PayPal payment strategy"""
    
    def __init__(self, email):
        self.email = email
    
    def pay(self, amount):
        """Process PayPal payment"""
        return f"Paid ${amount} with PayPal account {self.email}"

class BankTransferPayment(PaymentStrategy):
    """Bank transfer payment strategy"""
    
    def __init__(self, account_number):
        self.account_number = account_number
    
    def pay(self, amount):
        """Process bank transfer payment"""
        return f"Paid ${amount} with bank transfer to account {self.account_number}"

class PaymentProcessor:
    """Payment processor using strategy pattern"""
    
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy
    
    def set_payment_strategy(self, payment_strategy):
        """Set payment strategy"""
        self.payment_strategy = payment_strategy
    
    def process_payment(self, amount):
        """Process payment using current strategy"""
        return self.payment_strategy.pay(amount)

# Test strategy pattern
print("=== Strategy Pattern Example ===")
processor = PaymentProcessor(CreditCardPayment("1234567890123456"))
print(processor.process_payment(100))

processor.set_payment_strategy(PayPalPayment("user@example.com"))
print(processor.process_payment(200))

processor.set_payment_strategy(BankTransferPayment("987654321"))
print(processor.process_payment(300))

print("\n=== DECORATOR PATTERN ===")

# Decorator pattern adds behavior to objects dynamically
class Coffee:
    """Base coffee class"""
    
    def __init__(self):
        self.description = "Simple Coffee"
        self.cost = 2.00
    
    def get_description(self):
        """Get coffee description"""
        return self.description
    
    def get_cost(self):
        """Get coffee cost"""
        return self.cost

class CoffeeDecorator(Coffee):
    """Base decorator class"""
    
    def __init__(self, coffee):
        self.coffee = coffee
    
    def get_description(self):
        """Get decorated description"""
        return self.coffee.get_description()
    
    def get_cost(self):
        """Get decorated cost"""
        return self.coffee.get_cost()

class Milk(CoffeeDecorator):
    """Milk decorator"""
    
    def get_description(self):
        """Add milk to description"""
        return self.coffee.get_description() + ", Milk"
    
    def get_cost(self):
        """Add milk cost"""
        return self.coffee.get_cost() + 0.50

class Sugar(CoffeeDecorator):
    """Sugar decorator"""
    
    def get_description(self):
        """Add sugar to description"""
        return self.coffee.get_description() + ", Sugar"
    
    def get_cost(self):
        """Add sugar cost"""
        return self.coffee.get_cost() + 0.25

class WhippedCream(CoffeeDecorator):
    """Whipped cream decorator"""
    
    def get_description(self):
        """Add whipped cream to description"""
        return self.coffee.get_description() + ", Whipped Cream"
    
    def get_cost(self):
        """Add whipped cream cost"""
        return self.coffee.get_cost() + 0.75

# Test decorator pattern
print("=== Decorator Pattern Example ===")
coffee = Coffee()
print(f"Base coffee: {coffee.get_description()} - ${coffee.get_cost()}")

coffee_with_milk = Milk(coffee)
print(f"With milk: {coffee_with_milk.get_description()} - ${coffee_with_milk.get_cost()}")

coffee_with_sugar = Sugar(coffee)
print(f"With sugar: {coffee_with_sugar.get_description()} - ${coffee_with_sugar.get_cost()}")

coffee_with_all = WhippedCream(Milk(Sugar(coffee)))
print(f"With all: {coffee_with_all.get_description()} - ${coffee_with_all.get_cost()}")

print("\n=== ADAPTER PATTERN ===")

# Adapter pattern allows incompatible interfaces to work together
class OldPrinter:
    """Old printer with incompatible interface"""
    
    def print_document(self, text):
        """Print document using old interface"""
        return f"Old printer: {text}"

class NewPrinter:
    """New printer with different interface"""
    
    def print_text(self, content):
        """Print text using new interface"""
        return f"New printer: {content}"

class PrinterAdapter:
    """Adapter to make old printer compatible with new interface"""
    
    def __init__(self, old_printer):
        self.old_printer = old_printer
    
    def print_text(self, content):
        """Adapt old printer to new interface"""
        return self.old_printer.print_document(content)

# Test adapter pattern
print("=== Adapter Pattern Example ===")
old_printer = OldPrinter()
new_printer = NewPrinter()
adapter = PrinterAdapter(old_printer)

print(old_printer.print_document("Hello World"))
print(new_printer.print_text("Hello World"))
print(adapter.print_text("Hello World"))

print("\n=== FACADE PATTERN ===")

# Facade pattern provides a simplified interface to a complex subsystem
class CPU:
    """CPU subsystem"""
    
    def start(self):
        """Start CPU"""
        return "CPU started"
    
    def execute(self, program):
        """Execute program"""
        return f"CPU executing: {program}"

class Memory:
    """Memory subsystem"""
    
    def load(self, data):
        """Load data into memory"""
        return f"Memory loaded: {data}"
    
    def read(self, address):
        """Read from memory"""
        return f"Memory read from address: {address}"

class HardDrive:
    """Hard drive subsystem"""
    
    def read(self, sector):
        """Read from hard drive"""
        return f"Hard drive read sector: {sector}"
    
    def write(self, data, sector):
        """Write to hard drive"""
        return f"Hard drive wrote to sector {sector}: {data}"

class ComputerFacade:
    """Facade for computer subsystem"""
    
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()
    
    def start_computer(self):
        """Start computer using facade"""
        results = []
        results.append(self.cpu.start())
        results.append(self.memory.load("OS"))
        results.append(self.hard_drive.read("boot_sector"))
        return results
    
    def run_program(self, program):
        """Run program using facade"""
        results = []
        results.append(self.memory.load(program))
        results.append(self.cpu.execute(program))
        return results

# Test facade pattern
print("=== Facade Pattern Example ===")
computer = ComputerFacade()

print("Starting computer:")
for result in computer.start_computer():
    print(f"  {result}")

print("\nRunning program:")
for result in computer.run_program("Python"):
    print(f"  {result}")

print("\n=== DESIGN PATTERNS BEST PRACTICES ===")

print("""
Design Patterns Best Practices:
1. Use patterns to solve real problems, not just for the sake of it
2. Understand the problem before applying a pattern
3. Start with simple solutions and refactor to patterns when needed
4. Document why you're using a pattern
5. Test patterns thoroughly
6. Consider the trade-offs of each pattern
7. Use patterns consistently across your codebase
8. Learn from existing implementations
9. Practice with real-world examples
10. Keep patterns simple and focused
""")

# Example of good pattern usage
class Logger:
    """Logger using singleton pattern"""
    
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.logs = []
            self._initialized = True
    
    def log(self, message, level="INFO"):
        """Log a message"""
        log_entry = f"[{level}] {message}"
        self.logs.append(log_entry)
        print(log_entry)
    
    def get_logs(self):
        """Get all logs"""
        return self.logs.copy()
    
    def clear_logs(self):
        """Clear all logs"""
        self.logs.clear()

# Test logger singleton
print("=== Logger Singleton Example ===")
logger1 = Logger()
logger2 = Logger()

print(f"Same logger instance: {logger1 is logger2}")

logger1.log("Application started")
logger2.log("User logged in", "INFO")
logger1.log("Database connection established", "DEBUG")
logger2.log("Error occurred", "ERROR")

print(f"Total logs: {len(logger1.get_logs())}")

"""
Key Points to Remember:
1. Design patterns solve common design problems
2. Use patterns to improve code quality and maintainability
3. Understand the problem before applying a pattern
4. Start simple and refactor to patterns when needed
5. Test patterns thoroughly
6. Document why you're using a pattern
7. Practice with real-world examples
8. Keep patterns simple and focused
9. Learn from existing implementations
10. Use patterns consistently
"""
