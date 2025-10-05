"""
📁 INPUT/OUTPUT - File Operations
================================

Files are essential for storing and retrieving data permanently.
Learn how to read from and write to files in Python! 💾
"""

import os  # For file system operations

print("=== FILE WRITING ===")

# Writing to a file
def write_to_file():
    """Write content to a file"""
    filename = "sample.txt"
    
    # Method 1: Using with statement (recommended)
    with open(filename, 'w') as file:
        file.write("Hello, World!\n")
        file.write("This is a sample file.\n")
        file.write("Python is awesome!\n")
    
    print(f"Content written to {filename}")

# Write some content
write_to_file()

print("\n=== FILE READING ===")

# Reading from a file
def read_from_file():
    """Read content from a file"""
    filename = "sample.txt"
    
    try:
        # Method 1: Read entire file
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
            
        # Method 2: Read line by line
        print("\nReading line by line:")
        with open(filename, 'r') as file:
            for i, line in enumerate(file, 1):
                print(f"Line {i}: {line.strip()}")
                
    except FileNotFoundError:
        print(f"File {filename} not found!")

# Read the file
read_from_file()

print("\n=== APPENDING TO FILES ===")

# Appending to a file
def append_to_file():
    """Append content to existing file"""
    filename = "sample.txt"
    
    with open(filename, 'a') as file:  # 'a' for append mode
        file.write("This line was appended!\n")
        file.write("More content added.\n")
    
    print(f"Content appended to {filename}")

# Append some content
append_to_file()

# Read the updated file
print("\nUpdated file content:")
read_from_file()

print("\n=== FILE MODES ===")

# Different file modes
print("""
File Modes:
- 'r': Read mode (default)
- 'w': Write mode (overwrites existing file)
- 'a': Append mode (adds to end of file)
- 'x': Create mode (fails if file exists)
- 'b': Binary mode (for images, videos, etc.)
- 't': Text mode (default)
- '+': Read and write mode
""")

# Example with different modes
def demonstrate_modes():
    """Demonstrate different file modes"""
    
    # Write mode - creates new file or overwrites
    with open("demo.txt", 'w') as file:
        file.write("Line 1\n")
        file.write("Line 2\n")
    print("File created with write mode")
    
    # Append mode - adds to existing file
    with open("demo.txt", 'a') as file:
        file.write("Line 3 (appended)\n")
    print("Content appended")
    
    # Read mode - read the file
    with open("demo.txt", 'r') as file:
        content = file.read()
        print("File content:")
        print(content)

demonstrate_modes()

print("\n=== FILE INFORMATION ===")

# Get file information
def file_info(filename):
    """Display file information"""
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        print(f"File: {filename}")
        print(f"Size: {size} bytes")
        print(f"Exists: {os.path.exists(filename)}")
    else:
        print(f"File {filename} does not exist!")

# Check file info
file_info("sample.txt")
file_info("demo.txt")

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Simple note-taking app
def note_taking_app():
    """Simple note-taking application"""
    notes_file = "notes.txt"
    
    print("=== Note Taking App ===")
    print("1. Add note")
    print("2. View notes")
    print("3. Clear notes")
    
    choice = input("Choose option (1-3): ")
    
    if choice == "1":
        note = input("Enter your note: ")
        with open(notes_file, 'a') as file:
            file.write(f"{note}\n")
        print("Note saved!")
        
    elif choice == "2":
        try:
            with open(notes_file, 'r') as file:
                notes = file.readlines()
                if notes:
                    print("\nYour notes:")
                    for i, note in enumerate(notes, 1):
                        print(f"{i}. {note.strip()}")
                else:
                    print("No notes found!")
        except FileNotFoundError:
            print("No notes file found!")
            
    elif choice == "3":
        if os.path.exists(notes_file):
            os.remove(notes_file)
            print("All notes cleared!")
        else:
            print("No notes file found!")

# Uncomment to run note-taking app
# note_taking_app()

# Example 2: Student grade tracker
def grade_tracker():
    """Track student grades in a file"""
    grades_file = "grades.txt"
    
    print("=== Grade Tracker ===")
    student_name = input("Enter student name: ")
    subject = input("Enter subject: ")
    grade = input("Enter grade: ")
    
    # Append grade to file
    with open(grades_file, 'a') as file:
        file.write(f"{student_name},{subject},{grade}\n")
    
    print("Grade recorded!")
    
    # Display all grades
    print("\nAll grades:")
    try:
        with open(grades_file, 'r') as file:
            for line in file:
                name, subj, grd = line.strip().split(',')
                print(f"{name}: {subj} - {grd}")
    except FileNotFoundError:
        print("No grades recorded yet!")

# Uncomment to run grade tracker
# grade_tracker()

# Example 3: File backup utility
def backup_file(source, backup):
    """Create a backup of a file"""
    try:
        with open(source, 'r') as original:
            content = original.read()
        
        with open(backup, 'w') as backup_file:
            backup_file.write(content)
        
        print(f"Backup created: {backup}")
        return True
    except FileNotFoundError:
        print(f"Source file {source} not found!")
        return False

# Create a backup
backup_file("sample.txt", "sample_backup.txt")

print("\n=== ERROR HANDLING ===")

# Safe file operations
def safe_file_operations():
    """Demonstrate safe file operations"""
    
    filename = "test_file.txt"
    
    # Safe reading
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File content: {content}")
    except FileNotFoundError:
        print(f"File {filename} not found!")
    except PermissionError:
        print(f"No permission to read {filename}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    # Safe writing
    try:
        with open(filename, 'w') as file:
            file.write("This is a test file.")
        print(f"Successfully wrote to {filename}")
    except PermissionError:
        print(f"No permission to write to {filename}")
    except Exception as e:
        print(f"Error writing file: {e}")

safe_file_operations()

print("\n=== FILE CLEANUP ===")

# Clean up demo files
def cleanup_files():
    """Remove demo files"""
    files_to_remove = ["sample.txt", "demo.txt", "test_file.txt", "sample_backup.txt"]
    
    for filename in files_to_remove:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Removed {filename}")

# Uncomment to clean up files
# cleanup_files()

print("\n=== FILE OPERATIONS TIPS ===")

print("""
File Operations Tips:
1. Always use 'with' statement for file operations
2. Handle FileNotFoundError exceptions
3. Close files properly (with statement does this automatically)
4. Use appropriate file modes (r, w, a, x)
5. Check if file exists before operations
6. Use try/except for error handling
7. Consider file permissions
8. Backup important files
9. Use meaningful file names
10. Organize files in directories
""")

"""
Key Points to Remember:
1. Use open() to work with files
2. Always use 'with' statement for automatic file closing
3. File modes: 'r' (read), 'w' (write), 'a' (append)
4. Handle FileNotFoundError exceptions
5. Use os.path.exists() to check if file exists
6. Files are stored permanently on disk
7. Use try/except for safe file operations
8. Consider file permissions and access rights
9. Backup important data
10. Use meaningful file names and organize files
"""
