"""
🎭 OOP PRINCIPLES - Abstraction
===============================

Abstraction is the process of hiding complex implementation details
and showing only the essential features to the user! 🎯
"""

print("=== WHAT IS ABSTRACTION? ===")

# Abstraction focuses on what an object does, not how it does it
# It provides a simplified interface to complex systems

print("""
Abstraction Principles:
- Hide complex implementation details
- Show only essential features
- Provide simple interfaces
- Focus on what, not how
- Reduce complexity for users
""")

print("\n=== BASIC ABSTRACTION ===")

# Basic abstraction example
class Car:
    """A car class demonstrating basic abstraction"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._engine_running = False
        self._fuel_level = 100
        self._speed = 0
    
    # Public interface (what the user needs to know)
    def start(self):
        """Start the car"""
        if not self._engine_running:
            self._engine_running = True
            return f"The {self.year} {self.make} {self.model} is now running!"
        else:
            return "The car is already running!"
    
    def stop(self):
        """Stop the car"""
        if self._engine_running:
            self._engine_running = False
            self._speed = 0
            return "The car has been stopped."
        else:
            return "The car is already stopped!"
    
    def accelerate(self, speed_increase):
        """Accelerate the car"""
        if self._engine_running:
            self._speed += speed_increase
            self._fuel_level -= speed_increase * 0.1  # Fuel consumption
            return f"Accelerated to {self._speed} mph"
        else:
            return "Cannot accelerate - engine is not running!"
    
    def brake(self, speed_decrease):
        """Brake the car"""
        if self._speed > 0:
            self._speed = max(0, self._speed - speed_decrease)
            return f"Braked to {self._speed} mph"
        else:
            return "The car is already stopped!"
    
    def get_status(self):
        """Get car status"""
        status = f"Car: {self.year} {self.make} {self.model}\n"
        status += f"Engine: {'Running' if self._engine_running else 'Stopped'}\n"
        status += f"Speed: {self._speed} mph\n"
        status += f"Fuel: {self._fuel_level:.1f}%"
        return status
    
    # Private methods (implementation details hidden from user)
    def _check_fuel(self):
        """Check fuel level"""
        return self._fuel_level > 0
    
    def _check_engine_health(self):
        """Check engine health"""
        return True  # Simplified for example
    
    def _update_fuel_consumption(self):
        """Update fuel consumption"""
        if self._engine_running:
            self._fuel_level -= 0.1

# Test basic abstraction
print("=== Basic Abstraction Example ===")
car = Car("Toyota", "Camry", 2020)
print(car.start())
print(car.accelerate(30))
print(car.brake(10))
print(f"\n{car.get_status()}")
print(car.stop())

print("\n=== ABSTRACTION WITH INTERFACES ===")

# Abstraction using interfaces (abstract base classes)
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes"""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        """Calculate area of the shape"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter of the shape"""
        pass
    
    def get_info(self):
        """Get shape information"""
        return f"{self.name}: Area = {self.area():.2f}, Perimeter = {self.perimeter():.2f}"

class Rectangle(Shape):
    """Rectangle implementation"""
    
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
    """Circle implementation"""
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        """Calculate circle area"""
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculate circle perimeter (circumference)"""
        import math
        return 2 * math.pi * self.radius

# Test abstraction with interfaces
print("=== Abstraction with Interfaces ===")
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Rectangle(10, 7)
]

for shape in shapes:
    print(shape.get_info())

print("\n=== ABSTRACTION IN REAL-WORLD APPLICATIONS ===")

# Abstraction in a real-world application
class DatabaseConnection:
    """Abstract database connection class"""
    
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self._connection = None
        self._is_connected = False
    
    def connect(self):
        """Connect to database"""
        if not self._is_connected:
            self._connection = self._establish_connection()
            self._is_connected = True
            return "Connected to database"
        else:
            return "Already connected to database"
    
    def disconnect(self):
        """Disconnect from database"""
        if self._is_connected:
            self._close_connection()
            self._is_connected = False
            return "Disconnected from database"
        else:
            return "Not connected to database"
    
    def execute_query(self, query):
        """Execute a database query"""
        if not self._is_connected:
            return "Not connected to database"
        
        return self._run_query(query)
    
    def get_connection_status(self):
        """Get connection status"""
        return f"Database connection: {'Connected' if self._is_connected else 'Disconnected'}"
    
    # Private methods (implementation details)
    def _establish_connection(self):
        """Establish database connection"""
        # Simulate connection establishment
        print("Establishing database connection...")
        return f"Connection to {self.connection_string}"
    
    def _close_connection(self):
        """Close database connection"""
        print("Closing database connection...")
        self._connection = None
    
    def _run_query(self, query):
        """Run database query"""
        # Simulate query execution
        print(f"Executing query: {query}")
        return f"Query result for: {query}"

# Test database abstraction
print("=== Database Abstraction Example ===")
db = DatabaseConnection("localhost:5432/mydb")
print(db.get_connection_status())
print(db.connect())
print(db.execute_query("SELECT * FROM users"))
print(db.disconnect())

print("\n=== ABSTRACTION WITH COMPLEX SYSTEMS ===")

# Abstraction with complex systems
class MediaPlayer:
    """A media player with abstraction"""
    
    def __init__(self, name):
        self.name = name
        self._current_track = None
        self._is_playing = False
        self._volume = 50
        self._playlist = []
    
    # Public interface
    def play(self, track=None):
        """Play a track"""
        if track:
            self._current_track = track
            self._playlist.append(track)
        
        if self._current_track:
            self._is_playing = True
            return f"Playing: {self._current_track}"
        else:
            return "No track selected"
    
    def pause(self):
        """Pause playback"""
        if self._is_playing:
            self._is_playing = False
            return "Playback paused"
        else:
            return "Not currently playing"
    
    def stop(self):
        """Stop playback"""
        self._is_playing = False
        self._current_track = None
        return "Playback stopped"
    
    def set_volume(self, volume):
        """Set volume level"""
        if 0 <= volume <= 100:
            self._volume = volume
            return f"Volume set to {volume}%"
        else:
            return "Volume must be between 0 and 100"
    
    def get_playlist(self):
        """Get current playlist"""
        return self._playlist.copy()
    
    def get_status(self):
        """Get player status"""
        status = f"Media Player: {self.name}\n"
        status += f"Current track: {self._current_track or 'None'}\n"
        status += f"Status: {'Playing' if self._is_playing else 'Stopped'}\n"
        status += f"Volume: {self._volume}%"
        return status
    
    # Private methods (implementation details)
    def _load_track(self, track):
        """Load track for playback"""
        print(f"Loading track: {track}")
        return True
    
    def _initialize_audio_system(self):
        """Initialize audio system"""
        print("Initializing audio system...")
        return True
    
    def _cleanup_resources(self):
        """Clean up resources"""
        print("Cleaning up resources...")

# Test media player abstraction
print("=== Media Player Abstraction ===")
player = MediaPlayer("My Music Player")
print(player.play("Song 1"))
print(player.set_volume(75))
print(player.pause())
print(player.play())
print(f"\n{player.get_status()}")
print(f"Playlist: {player.get_playlist()}")

print("\n=== ABSTRACTION PATTERNS ===")

# Different abstraction patterns
class FileManager:
    """A file manager with abstraction patterns"""
    
    def __init__(self):
        self._files = {}
        self._current_directory = "/"
    
    # High-level operations (what user needs)
    def create_file(self, filename, content=""):
        """Create a new file"""
        if self._validate_filename(filename):
            self._files[filename] = content
            return f"Created file: {filename}"
        else:
            return "Invalid filename"
    
    def read_file(self, filename):
        """Read file content"""
        if filename in self._files:
            return self._files[filename]
        else:
            return "File not found"
    
    def write_file(self, filename, content):
        """Write content to file"""
        if filename in self._files:
            self._files[filename] = content
            return f"Updated file: {filename}"
        else:
            return "File not found"
    
    def delete_file(self, filename):
        """Delete a file"""
        if filename in self._files:
            del self._files[filename]
            return f"Deleted file: {filename}"
        else:
            return "File not found"
    
    def list_files(self):
        """List all files"""
        return list(self._files.keys())
    
    def get_file_info(self, filename):
        """Get file information"""
        if filename in self._files:
            content = self._files[filename]
            return f"File: {filename}, Size: {len(content)} characters"
        else:
            return "File not found"
    
    # Private methods (implementation details)
    def _validate_filename(self, filename):
        """Validate filename"""
        return isinstance(filename, str) and len(filename) > 0 and "/" not in filename
    
    def _check_permissions(self, filename):
        """Check file permissions"""
        return True  # Simplified for example
    
    def _update_metadata(self, filename):
        """Update file metadata"""
        pass  # Simplified for example

# Test file manager abstraction
print("=== File Manager Abstraction ===")
fm = FileManager()
print(fm.create_file("document.txt", "Hello, World!"))
print(fm.create_file("readme.md", "# My Project"))
print(f"Files: {fm.list_files()}")
print(fm.write_file("document.txt", "Updated content"))
print(f"Content: {fm.read_file('document.txt')}")
print(fm.get_file_info("document.txt"))

print("\n=== ABSTRACTION BEST PRACTICES ===")

print("""
Abstraction Best Practices:
1. Hide complex implementation details
2. Provide simple, intuitive interfaces
3. Focus on what the object does, not how
4. Use abstract base classes for common interfaces
5. Keep public interfaces stable
6. Document your abstractions clearly
7. Test abstractions thoroughly
8. Use meaningful method names
9. Avoid exposing internal state
10. Follow the principle of least surprise
""")

# Example of good abstraction design
class Calculator:
    """A calculator with good abstraction"""
    
    def __init__(self):
        self._history = []
        self._memory = 0
    
    # Public interface
    def add(self, a, b):
        """Add two numbers"""
        result = a + b
        self._history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract two numbers"""
        result = a - b
        self._history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        result = a * b
        self._history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        """Get calculation history"""
        return self._history.copy()
    
    def clear_history(self):
        """Clear calculation history"""
        self._history.clear()
        return "History cleared"
    
    def memory_store(self, value):
        """Store value in memory"""
        self._memory = value
        return f"Stored {value} in memory"
    
    def memory_recall(self):
        """Recall value from memory"""
        return self._memory
    
    def memory_clear(self):
        """Clear memory"""
        self._memory = 0
        return "Memory cleared"

# Test calculator abstraction
print("=== Calculator Abstraction ===")
calc = Calculator()
print(f"5 + 3 = {calc.add(5, 3)}")
print(f"10 - 4 = {calc.subtract(10, 4)}")
print(f"6 * 7 = {calc.multiply(6, 7)}")
print(f"15 / 3 = {calc.divide(15, 3)}")
print(f"History: {calc.get_history()}")
print(calc.memory_store(42))
print(f"Memory: {calc.memory_recall()}")

"""
Key Points to Remember:
1. Abstraction hides complex implementation details
2. Focus on what an object does, not how it does it
3. Provide simple, intuitive interfaces
4. Use abstract base classes for common interfaces
5. Keep public interfaces stable
6. Document your abstractions clearly
7. Test abstractions thoroughly
8. Follow the principle of least surprise
9. Practice with real-world examples
10. Balance simplicity with functionality
"""
