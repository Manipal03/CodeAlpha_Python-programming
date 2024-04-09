import time
import random

# Welcoming the user
name = input("What is your name? ")
print("Hello, " + name + ", Time to play hangman!")

# Wait for 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

# List of words to choose from
words = ['python', 'hangman', 'programming', 'game', 'computer', 'player']

# Selecting a random word
word = random.choice(words)

# Create a variable with an empty value for guesses
guesses = ''

# Maximum number of incorrect guesses allowed
max_attempts = 10

# Create a while loop
while max_attempts > 0:
    # Make a counter that starts with zero
    failed = 0

    # For every character in the secret word
    for char in word:
        # See if the character is in the player's guess
        if char in guesses:
            # Print the character
            print(char, end=" ")
        else:
            # If not found, print a dash
            print("_", end=" ")

            # Increase the failed counter with one
            failed += 1

    # If failed is equal to zero, the player won
    if failed == 0:
        print("\nYou won!")
        break

    # Ask the user to guess a character
    guess = input("\nGuess a character: ")

    # Validate the input (single character)
    if len(guess) != 1:
        print("Please enter a single character.")
        continue

    # Set the player's guess to guesses
    guesses += guess

    # If the guess is not found in the secret word
    if guess not in word:
        # Decrease the max_attempts counter
        max_attempts -= 1
        # Print wrong guess and remaining attempts
        print("Wrong guess. You have", max_attempts, "more attempts.")

        # If the max_attempts are equal to zero, the player loses
        if max_attempts == 0:
            print("You Lose!")
            break

