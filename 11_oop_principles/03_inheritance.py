"""
🧬 OOP PRINCIPLES - Inheritance
==============================

Inheritance allows a class to inherit properties and methods from another class.
It promotes code reusability and establishes "is-a" relationships! 🔗
"""

print("=== WHAT IS INHERITANCE? ===")

# Inheritance allows a class to inherit from another class
# The child class gets all the attributes and methods of the parent class

print("""
Inheritance Concepts:
- Parent Class (Base Class): The class being inherited from
- Child Class (Derived Class): The class that inherits
- "is-a" relationship: Child is a type of Parent
- Code reusability: Avoid duplicating code
- Method overriding: Child can override parent methods
""")

print("\n=== BASIC INHERITANCE ===")

# Basic inheritance example
class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
    
    def eat(self):
        """Animal eats"""
        return f"{self.name} is eating"
    
    def sleep(self):
        """Animal sleeps"""
        return f"{self.name} is sleeping"
    
    def make_sound(self):
        """Animal makes a sound"""
        return f"{self.name} makes a sound"
    
    def get_info(self):
        """Get animal information"""
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    """Dog class inheriting from Animal"""
    
    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name, "Dog")
        self.breed = breed
        self.tricks = []
    
    def make_sound(self):
        """Override parent method"""
        return f"{self.name} barks: Woof! Woof!"
    
    def learn_trick(self, trick):
        """Dog-specific method"""
        self.tricks.append(trick)
        return f"{self.name} learned {trick}"
    
    def perform_trick(self, trick):
        """Dog-specific method"""
        if trick in self.tricks:
            return f"{self.name} performs {trick}"
        else:
            return f"{self.name} doesn't know {trick}"
    
    def get_info(self):
        """Override parent method"""
        return f"{self.name} is a {self.breed} {self.species}"

class Cat(Animal):
    """Cat class inheriting from Animal"""
    
    def __init__(self, name, breed):
        super().__init__(name, "Cat")
        self.breed = breed
        self.lives = 9
    
    def make_sound(self):
        """Override parent method"""
        return f"{self.name} meows: Meow! Meow!"
    
    def climb(self):
        """Cat-specific method"""
        return f"{self.name} is climbing"
    
    def get_info(self):
        """Override parent method"""
        return f"{self.name} is a {self.breed} {self.species} with {self.lives} lives"

# Test basic inheritance
print("=== Basic Inheritance Example ===")
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Persian")

print(dog.get_info())
print(dog.make_sound())
print(dog.learn_trick("sit"))
print(dog.perform_trick("sit"))

print(f"\n{cat.get_info()}")
print(cat.make_sound())
print(cat.climb())

print("\n=== MULTIPLE INHERITANCE ===")

# Multiple inheritance example
class Flyable:
    """Mixin class for flying ability"""
    
    def fly(self):
        """Fly method"""
        return f"{self.name} is flying"
    
    def land(self):
        """Land method"""
        return f"{self.name} has landed"

class Swimmable:
    """Mixin class for swimming ability"""
    
    def swim(self):
        """Swim method"""
        return f"{self.name} is swimming"
    
    def dive(self):
        """Dive method"""
        return f"{self.name} is diving"

class Duck(Animal, Flyable, Swimmable):
    """Duck class with multiple inheritance"""
    
    def __init__(self, name):
        super().__init__(name, "Duck")
        self.feathers = True
    
    def make_sound(self):
        """Override parent method"""
        return f"{self.name} quacks: Quack! Quack!"
    
    def get_info(self):
        """Override parent method"""
        return f"{self.name} is a {self.species} with feathers"

# Test multiple inheritance
print("=== Multiple Inheritance Example ===")
duck = Duck("Donald")
print(duck.get_info())
print(duck.make_sound())
print(duck.fly())
print(duck.swim())
print(duck.dive())
print(duck.land())

print("\n=== INHERITANCE HIERARCHY ===")

# Complex inheritance hierarchy
class Vehicle:
    """Base class for all vehicles"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
        self.speed = 0
    
    def start(self):
        """Start the vehicle"""
        self.is_running = True
        return f"{self.year} {self.make} {self.model} is now running"
    
    def stop(self):
        """Stop the vehicle"""
        self.is_running = False
        self.speed = 0
        return f"{self.year} {self.make} {self.model} has stopped"
    
    def accelerate(self, speed_increase):
        """Accelerate the vehicle"""
        if self.is_running:
            self.speed += speed_increase
            return f"Accelerated to {self.speed} mph"
        else:
            return "Cannot accelerate - vehicle is not running"
    
    def get_info(self):
        """Get vehicle information"""
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    """Car class inheriting from Vehicle"""
    
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors
        self.passengers = 0
    
    def open_door(self, door_number):
        """Open a specific door"""
        if 1 <= door_number <= self.doors:
            return f"Opened door {door_number}"
        else:
            return "Invalid door number"
    
    def get_info(self):
        """Override parent method"""
        return f"{super().get_info()} with {self.doors} doors"

class Truck(Vehicle):
    """Truck class inheriting from Vehicle"""
    
    def __init__(self, make, model, year, cargo_capacity):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity
        self.cargo = []
    
    def load_cargo(self, item):
        """Load cargo into truck"""
        if len(self.cargo) < self.cargo_capacity:
            self.cargo.append(item)
            return f"Loaded {item} into truck"
        else:
            return "Truck is at capacity"
    
    def unload_cargo(self, item):
        """Unload cargo from truck"""
        if item in self.cargo:
            self.cargo.remove(item)
            return f"Unloaded {item} from truck"
        else:
            return f"{item} not found in truck"
    
    def get_info(self):
        """Override parent method"""
        return f"{super().get_info()} with {self.cargo_capacity} cargo capacity"

class Motorcycle(Vehicle):
    """Motorcycle class inheriting from Vehicle"""
    
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size
        self.has_helmet = False
    
    def put_on_helmet(self):
        """Put on helmet"""
        self.has_helmet = True
        return "Helmet is on"
    
    def take_off_helmet(self):
        """Take off helmet"""
        self.has_helmet = False
        return "Helmet is off"
    
    def get_info(self):
        """Override parent method"""
        return f"{super().get_info()} with {self.engine_size}cc engine"

# Test inheritance hierarchy
print("=== Inheritance Hierarchy Example ===")
vehicles = [
    Car("Toyota", "Camry", 2020, 4),
    Truck("Ford", "F-150", 2019, 5),
    Motorcycle("Honda", "CBR", 2021, 600)
]

for vehicle in vehicles:
    print(f"\n{vehicle.get_info()}")
    print(vehicle.start())
    print(vehicle.accelerate(30))
    print(vehicle.stop())

print("\n=== METHOD OVERRIDING ===")

# Method overriding example
class Shape:
    """Base class for shapes"""
    
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """Calculate area"""
        return 0
    
    def perimeter(self):
        """Calculate perimeter"""
        return 0
    
    def get_info(self):
        """Get shape information"""
        return f"{self.name}: Area = {self.area():.2f}, Perimeter = {self.perimeter():.2f}"

class Rectangle(Shape):
    """Rectangle class inheriting from Shape"""
    
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        """Override parent method"""
        return self.width * self.height
    
    def perimeter(self):
        """Override parent method"""
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Circle class inheriting from Shape"""
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        """Override parent method"""
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Override parent method"""
        import math
        return 2 * math.pi * self.radius

# Test method overriding
print("=== Method Overriding Example ===")
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Rectangle(10, 7)
]

for shape in shapes:
    print(shape.get_info())

print("\n=== SUPER() FUNCTION ===")

# Using super() function
class Person:
    """Base class for persons"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_info(self):
        """Get person information"""
        return f"Name: {self.name}, Age: {self.age}"
    
    def work(self):
        """Person works"""
        return f"{self.name} is working"

class Employee(Person):
    """Employee class inheriting from Person"""
    
    def __init__(self, name, age, employee_id, department):
        # Call parent constructor
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department
        self.salary = 0
    
    def work(self):
        """Override parent method"""
        return f"{self.name} is working in {self.department} department"
    
    def get_salary(self):
        """Get employee salary"""
        return f"{self.name}'s salary is ${self.salary}"
    
    def get_info(self):
        """Override parent method"""
        # Call parent method and extend it
        base_info = super().get_info()
        return f"{base_info}, ID: {self.employee_id}, Department: {self.department}"

class Manager(Employee):
    """Manager class inheriting from Employee"""
    
    def __init__(self, name, age, employee_id, department, team_size):
        super().__init__(name, age, employee_id, department)
        self.team_size = team_size
        self.salary = 80000  # Manager salary
    
    def work(self):
        """Override parent method"""
        return f"{self.name} is managing a team of {self.team_size} people"
    
    def get_info(self):
        """Override parent method"""
        base_info = super().get_info()
        return f"{base_info}, Team Size: {self.team_size}"

# Test super() function
print("=== Super() Function Example ===")
person = Person("Alice", 30)
employee = Employee("Bob", 25, "E001", "Engineering")
manager = Manager("Charlie", 35, "M001", "Engineering", 10)

print(person.get_info())
print(person.work())

print(f"\n{employee.get_info()}")
print(employee.work())
print(employee.get_salary())

print(f"\n{manager.get_info()}")
print(manager.work())
print(manager.get_salary())

print("\n=== INHERITANCE BEST PRACTICES ===")

print("""
Inheritance Best Practices:
1. Use inheritance for "is-a" relationships
2. Keep inheritance hierarchies shallow
3. Use composition over inheritance when possible
4. Override methods when necessary
5. Use super() to call parent methods
6. Follow the Liskov Substitution Principle
7. Document inheritance relationships
8. Test inheritance thoroughly
9. Use abstract base classes for common interfaces
10. Avoid deep inheritance hierarchies
""")

# Example of good inheritance design
class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
    
    def eat(self):
        """Animal eats"""
        return f"{self.name} is eating"
    
    def sleep(self):
        """Animal sleeps"""
        return f"{self.name} is sleeping"
    
    def make_sound(self):
        """Animal makes a sound"""
        return f"{self.name} makes a sound"
    
    def get_info(self):
        """Get animal information"""
        return f"{self.name} is a {self.species}"

class Bird(Animal):
    """Bird class inheriting from Animal"""
    
    def __init__(self, name, species, can_fly=True):
        super().__init__(name, species)
        self.can_fly = can_fly
        self.wingspan = 0
    
    def fly(self):
        """Bird flies"""
        if self.can_fly:
            return f"{self.name} is flying"
        else:
            return f"{self.name} cannot fly"
    
    def make_sound(self):
        """Override parent method"""
        return f"{self.name} chirps: Tweet! Tweet!"
    
    def get_info(self):
        """Override parent method"""
        base_info = super().get_info()
        return f"{base_info}, Can fly: {self.can_fly}"

# Test good inheritance design
print("=== Good Inheritance Design ===")
bird1 = Bird("Tweety", "Canary", True)
bird2 = Bird("Penguin", "Emperor Penguin", False)

print(bird1.get_info())
print(bird1.make_sound())
print(bird1.fly())

print(f"\n{bird2.get_info()}")
print(bird2.make_sound())
print(bird2.fly())

"""
Key Points to Remember:
1. Inheritance promotes code reusability
2. Use inheritance for "is-a" relationships
3. Override methods when necessary
4. Use super() to call parent methods
5. Keep inheritance hierarchies shallow
6. Follow the Liskov Substitution Principle
7. Test inheritance thoroughly
8. Use composition over inheritance when possible
9. Document inheritance relationships
10. Practice with real-world examples
"""
