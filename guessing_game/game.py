"""
Guessing Game
--------------
The program picks a random number between 1 and 100, and the
player has 10 attempts to guess it, getting a hint after each
try ("higher" or "lower"). At the end, the player can choose
to play again.
"""

import random

while True:
    number = random.randint(1, 100)
    attempts = 10
    print("""
                === Guessing Game ===
    Guess the number between 1 and 100. You have 10 attempts
    """)
    while attempts > 0:
        guess = int(input(f"Attempt {11 - attempts}/10: "))
        if guess < number:
            print("The number is higher.")
        elif guess > number:
            print("The number is lower.")
        else:
            print(f"Correct! You guessed it in {11 - attempts} attempts.")
            break
        attempts -= 1
        if attempts == 0:
            print(f"You ran out of attempts. The number was {number}.")
    
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        print("Thanks for playing. Goodbye!")
        break