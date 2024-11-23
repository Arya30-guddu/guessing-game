import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is? You have 10 attempts!")

    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        try:
            # Get the user's guess
            guess = int(input(f"You have {attempts} attempts left. Enter your guess: "))
            
            # Check the user's guess
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {target_number} correctly.")
                break  # Exit the loop since the user won
        except ValueError:
            print("Invalid input! Please enter a number.")

        # Decrease the attempt count
        attempts -= 1

    # If the user runs out of attempts
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The number was {target_number}.")

# Run the game
number_guessing_game()
