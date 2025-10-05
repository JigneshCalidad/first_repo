"""
 PROJECT 2 - Guess the Number Game
==================================

Build a number guessing game where the player tries to guess a random number.
This project will help you practice loops, random numbers, and user interaction.
"""

import random

def easy_game():
    """Easy mode: numbers 1-10, 5 attempts"""
    print("=== Easy Mode ===")
    print("Guess a number between 1 and 10")
    print("You have 5 attempts")
    
    secret_number = random.randint(1, 10)
    attempts = 0
    max_attempts = 5
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                return True
            elif guess < secret_number:
                print("Too low! 📉")
            else:
                print("Too high! 📈")
                
        except ValueError:
            print("Please enter a valid number!")
            attempts -= 1  # Don't count invalid attempts
    
    print(f"Game over! The number was {secret_number}")
    return False

def medium_game():
    """Medium mode: numbers 1-50, 7 attempts"""
    print("=== Medium Mode ===")
    print("Guess a number between 1 and 50")
    print("You have 7 attempts")
    
    secret_number = random.randint(1, 50)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                return True
            elif guess < secret_number:
                print("Too low! 📉")
            else:
                print("Too high! 📈")
                
        except ValueError:
            print("Please enter a valid number!")
            attempts -= 1
    
    print(f"Game over! The number was {secret_number}")
    return False

def hard_game():
    """Hard mode: numbers 1-100, 10 attempts"""
    print("=== Hard Mode ===")
    print("Guess a number between 1 and 100")
    print("You have 10 attempts")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                return True
            elif guess < secret_number:
                print("Too low! 📉")
            else:
                print("Too high! 📈")
                
        except ValueError:
            print("Please enter a valid number!")
            attempts -= 1
    
    print(f"Game over! The number was {secret_number}")
    return False

def custom_game():
    """Custom mode: user chooses range and attempts"""
    print("=== Custom Mode ===")
    
    try:
        min_num = int(input("Enter minimum number: "))
        max_num = int(input("Enter maximum number: "))
        max_attempts = int(input("Enter number of attempts: "))
        
        if min_num >= max_num:
            print("Minimum must be less than maximum!")
            return False
        
        print(f"Guess a number between {min_num} and {max_num}")
        print(f"You have {max_attempts} attempts")
        
        secret_number = random.randint(min_num, max_num)
        attempts = 0
        
        while attempts < max_attempts:
            try:
                guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
                attempts += 1
                
                if guess == secret_number:
                    print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                    return True
                elif guess < secret_number:
                    print("Too low! 📉")
                else:
                    print("Too high! 📈")
                    
            except ValueError:
                print("Please enter a valid number!")
                attempts -= 1
        
        print(f"Game over! The number was {secret_number}")
        return False
        
    except ValueError:
        print("Please enter valid numbers!")
        return False

def two_player_game():
    """Two player mode: one player sets the number, other guesses"""
    print("=== Two Player Mode ===")
    print("Player 1: Set a number")
    print("Player 2: Guess the number")
    
    try:
        secret_number = int(input("Player 1, enter a number: "))
        max_attempts = int(input("How many attempts should Player 2 have? "))
        
        print(f"Player 2, you have {max_attempts} attempts to guess the number!")
        
        attempts = 0
        while attempts < max_attempts:
            try:
                guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
                attempts += 1
                
                if guess == secret_number:
                    print(f"🎉 Player 2 wins! You guessed it in {attempts} attempts!")
                    return True
                elif guess < secret_number:
                    print("Too low! 📉")
                else:
                    print("Too high! 📈")
                    
            except ValueError:
                print("Please enter a valid number!")
                attempts -= 1
        
        print(f"Player 1 wins! The number was {secret_number}")
        return False
        
    except ValueError:
        print("Please enter valid numbers!")
        return False

def statistics_mode():
    """Statistics mode: track performance over multiple games"""
    print("=== Statistics Mode ===")
    print("Play multiple games and see your statistics!")
    
    games_played = 0
    games_won = 0
    total_attempts = 0
    
    while True:
        print(f"\nGames played: {games_played}")
        print(f"Games won: {games_won}")
        if games_played > 0:
            win_rate = (games_won / games_played) * 100
            avg_attempts = total_attempts / games_played
            print(f"Win rate: {win_rate:.1f}%")
            print(f"Average attempts: {avg_attempts:.1f}")
        
        print("\n1. Easy (1-10, 5 attempts)")
        print("2. Medium (1-50, 7 attempts)")
        print("3. Hard (1-100, 10 attempts)")
        print("4. Exit")
        
        choice = input("Choose mode (1-4): ")
        
        if choice == '4':
            break
        elif choice == '1':
            won = easy_game()
            games_played += 1
            if won:
                games_won += 1
                total_attempts += 5  # Assume max attempts for simplicity
        elif choice == '2':
            won = medium_game()
            games_played += 1
            if won:
                games_won += 1
                total_attempts += 7
        elif choice == '3':
            won = hard_game()
            games_played += 1
            if won:
                games_won += 1
                total_attempts += 10
        else:
            print("Invalid choice!")
    
    print(f"\nFinal Statistics:")
    print(f"Games played: {games_played}")
    print(f"Games won: {games_won}")
    if games_played > 0:
        win_rate = (games_won / games_played) * 100
        avg_attempts = total_attempts / games_played
        print(f"Win rate: {win_rate:.1f}%")
        print(f"Average attempts: {avg_attempts:.1f}")

def main():
    """Main function to choose game mode"""
    print("🎯 Welcome to Guess the Number Game! 🎯")
    print("Choose your game mode:")
    print("1. Easy (1-10, 5 attempts)")
    print("2. Medium (1-50, 7 attempts)")
    print("3. Hard (1-100, 10 attempts)")
    print("4. Custom (you choose range and attempts)")
    print("5. Two Player (one sets, other guesses)")
    print("6. Statistics Mode (track performance)")
    print("7. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            easy_game()
        elif choice == '2':
            medium_game()
        elif choice == '3':
            hard_game()
        elif choice == '4':
            custom_game()
        elif choice == '5':
            two_player_game()
        elif choice == '6':
            statistics_mode()
        elif choice == '7':
            print("Thanks for playing! 👋")
            break
        else:
            print("Invalid choice! Please enter 1-7.")
        
        # Ask if player wants to play again
        if choice in ['1', '2', '3', '4', '5']:
            play_again = input("\nDo you want to play again? (y/n): ")
            if play_again.lower() != 'y':
                print("Thanks for playing! 👋")
                break

if __name__ == "__main__":
    main()

"""
Project Features:
1. Multiple difficulty levels
2. Custom game settings
3. Two-player mode
4. Statistics tracking
5. Error handling for invalid input
6. User-friendly interface
7. Game replay functionality

Learning Objectives:
- Practice with random numbers
- Implement different game modes
- Handle user input and validation
- Create interactive programs
- Practice loops and conditionals
- Work with functions and parameters
- Implement game statistics

Extensions:
- Add hints system
- Implement difficulty scaling
- Add sound effects
- Create a GUI version
- Add multiplayer networking
- Implement save/load functionality
- Add achievements system
"""
