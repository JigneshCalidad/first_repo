"""
🔄 FLOW CONTROL - Switch Alternatives
====================================

Python doesn't have a traditional switch statement, but we have several
elegant alternatives that are often more readable and powerful! 🎯
"""

print("=== DICTIONARY-BASED SWITCH ===")

# Dictionary mapping for switch-like behavior
def get_day_type(day):
    """Get type of day using dictionary mapping"""
    day_types = {
        "monday": "weekday",
        "tuesday": "weekday", 
        "wednesday": "weekday",
        "thursday": "weekday",
        "friday": "weekday",
        "saturday": "weekend",
        "sunday": "weekend"
    }
    
    return day_types.get(day.lower(), "unknown")

# Test dictionary switch
days = ["monday", "saturday", "friday", "invalid"]
for day in days:
    day_type = get_day_type(day)
    print(f"{day.capitalize()} is a {day_type}")

print("\n=== FUNCTION-BASED SWITCH ===")

# Using functions as switch cases
def handle_add(x, y):
    return x + y

def handle_subtract(x, y):
    return x - y

def handle_multiply(x, y):
    return x * y

def handle_divide(x, y):
    return x / y if y != 0 else "Error: Division by zero"

def handle_default(x, y):
    return "Invalid operation"

# Function-based switch
def calculator(operation, x, y):
    """Calculator using function-based switch"""
    operations = {
        "+": handle_add,
        "-": handle_subtract,
        "*": handle_multiply,
        "/": handle_divide
    }
    
    handler = operations.get(operation, handle_default)
    return handler(x, y)

# Test calculator
operations = ["+", "-", "*", "/", "%"]
x, y = 10, 3

for op in operations:
    result = calculator(op, x, y)
    print(f"{x} {op} {y} = {result}")

print("\n=== LAMBDA-BASED SWITCH ===")

# Using lambda functions for simple operations
def get_grade_emoji(grade):
    """Get emoji for grade using lambda switch"""
    grade_emojis = {
        "A": lambda: "🌟",
        "B": lambda: "👍", 
        "C": lambda: "✅",
        "D": lambda: "📈",
        "F": lambda: "❌"
    }
    
    emoji_func = grade_emojis.get(grade.upper(), lambda: "❓")
    return emoji_func()

# Test grade emojis
grades = ["A", "B", "C", "D", "F", "X"]
for grade in grades:
    emoji = get_grade_emoji(grade)
    print(f"Grade {grade}: {emoji}")

print("\n=== CLASS-BASED SWITCH ===")

# Using classes for complex switch-like behavior
class WeatherHandler:
    """Handle different weather conditions"""
    
    def handle_sunny(self):
        return "Perfect for outdoor activities! ☀️"
    
    def handle_rainy(self):
        return "Stay indoors or bring an umbrella! ☔"
    
    def handle_snowy(self):
        return "Bundle up and be careful! ❄️"
    
    def handle_cloudy(self):
        return "Decent weather for most activities! ☁️"
    
    def handle_default(self):
        return "Check the weather forecast! 🌤️"

def get_weather_advice(weather):
    """Get weather advice using class-based switch"""
    handler = WeatherHandler()
    weather_methods = {
        "sunny": handler.handle_sunny,
        "rainy": handler.handle_rainy,
        "snowy": handler.handle_snowy,
        "cloudy": handler.handle_cloudy
    }
    
    method = weather_methods.get(weather.lower(), handler.handle_default)
    return method()

# Test weather advice
weather_conditions = ["sunny", "rainy", "snowy", "cloudy", "foggy"]
for weather in weather_conditions:
    advice = get_weather_advice(weather)
    print(f"{weather.capitalize()}: {advice}")

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Menu system
def handle_menu_choice(choice):
    """Handle menu choices using dictionary switch"""
    menu_actions = {
        "1": lambda: "Opening file...",
        "2": lambda: "Saving file...",
        "3": lambda: "Printing document...",
        "4": lambda: "Exiting application...",
        "5": lambda: "Showing help..."
    }
    
    action = menu_actions.get(choice, lambda: "Invalid choice!")
    return action()

# Test menu system
menu_choices = ["1", "2", "3", "4", "5", "6"]
for choice in menu_choices:
    result = handle_menu_choice(choice)
    print(f"Choice {choice}: {result}")

# Example 2: HTTP status code handler
def handle_http_status(status_code):
    """Handle HTTP status codes"""
    status_handlers = {
        200: lambda: "OK - Request successful! ✅",
        201: lambda: "Created - Resource created! 🆕",
        400: lambda: "Bad Request - Invalid input! ❌",
        401: lambda: "Unauthorized - Login required! 🔐",
        403: lambda: "Forbidden - Access denied! 🚫",
        404: lambda: "Not Found - Resource missing! 🔍",
        500: lambda: "Server Error - Try again later! 🔧"
    }
    
    handler = status_handlers.get(status_code, lambda: f"Unknown status: {status_code}")
    return handler()

# Test HTTP status handling
status_codes = [200, 201, 400, 401, 403, 404, 500, 999]
for code in status_codes:
    message = handle_http_status(code)
    print(f"Status {code}: {message}")

# Example 3: User role permissions
def check_permissions(role, action):
    """Check user permissions based on role"""
    role_permissions = {
        "admin": {
            "read": "Full access granted! 👑",
            "write": "Full access granted! 👑",
            "delete": "Full access granted! 👑",
            "manage": "Full access granted! 👑"
        },
        "user": {
            "read": "Access granted! 👤",
            "write": "Access granted! 👤",
            "delete": "Access denied! 🚫",
            "manage": "Access denied! 🚫"
        },
        "guest": {
            "read": "Limited access granted! 👥",
            "write": "Access denied! 🚫",
            "delete": "Access denied! 🚫",
            "manage": "Access denied! 🚫"
        }
    }
    
    role_data = role_permissions.get(role, {})
    permission = role_data.get(action, "Unknown role or action!")
    return permission

# Test permission system
roles = ["admin", "user", "guest", "moderator"]
actions = ["read", "write", "delete", "manage"]

for role in roles:
    print(f"\n{role.capitalize()} role:")
    for action in actions:
        permission = check_permissions(role, action)
        print(f"  {action}: {permission}")

print("\n=== ADVANCED SWITCH PATTERNS ===")

# Pattern 1: Range-based switching
def get_temperature_category(temp):
    """Categorize temperature using range-based switch"""
    if temp < 0:
        return "Freezing! 🥶"
    elif temp < 10:
        return "Very cold! ❄️"
    elif temp < 20:
        return "Cool! 🌤️"
    elif temp < 30:
        return "Warm! ☀️"
    elif temp < 40:
        return "Hot! 🔥"
    else:
        return "Extremely hot! 🌡️"

# Test temperature categories
temperatures = [-5, 5, 15, 25, 35, 45]
for temp in temperatures:
    category = get_temperature_category(temp)
    print(f"{temp}°C: {category}")

# Pattern 2: Multiple condition switching
def process_user_input(user_input, user_type, is_premium):
    """Process user input with multiple conditions"""
    # Create a key based on multiple conditions
    key = f"{user_type}_{is_premium}_{user_input.lower()}"
    
    handlers = {
        "admin_true_help": lambda: "Admin help: Full system access! 👑",
        "admin_false_help": lambda: "Admin help: Full system access! 👑",
        "user_true_help": lambda: "Premium user help: Enhanced support! ⭐",
        "user_false_help": lambda: "Basic user help: Standard support! 👤",
        "guest_true_help": lambda: "Guest help: Limited support! 👥",
        "guest_false_help": lambda: "Guest help: Limited support! 👥"
    }
    
    handler = handlers.get(key, lambda: "Unknown request!")
    return handler()

# Test multi-condition switching
test_cases = [
    ("admin", True, "help"),
    ("user", True, "help"),
    ("user", False, "help"),
    ("guest", False, "help"),
    ("admin", True, "unknown")
]

for user_type, is_premium, command in test_cases:
    result = process_user_input(command, user_type, is_premium)
    print(f"{user_type} (premium: {is_premium}) - {command}: {result}")

print("\n=== SWITCH ALTERNATIVES SUMMARY ===")

print("""
Switch Alternatives in Python:
1. Dictionary mapping - Simple key-value lookups
2. Function-based - Complex logic in separate functions
3. Lambda-based - Simple operations inline
4. Class-based - Object-oriented approach
5. Range-based - For numeric ranges
6. Multi-condition - Complex decision trees

Best Practices:
1. Use dictionaries for simple mappings
2. Use functions for complex logic
3. Keep switch logic readable
4. Handle default cases
5. Use meaningful names
6. Test all possible cases
7. Consider performance for large switches
8. Document complex switch logic
""")

"""
Key Points to Remember:
1. Python doesn't have traditional switch statements
2. Dictionary mapping is the most common alternative
3. Use functions for complex switch logic
4. Lambda functions work well for simple cases
5. Classes provide object-oriented switch behavior
6. Always handle default/unknown cases
7. Keep switch logic readable and maintainable
8. Test all possible switch cases
9. Consider performance for large switch statements
10. Choose the right pattern for your use case
"""
