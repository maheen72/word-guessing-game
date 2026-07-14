# ------------------------ WORD GUESSING GAME ------------------------

import random

easy_words = ["eat", "sleep", "drink", "dance"]
medium_words = ["eating", "drinking", "dancing", "sleeping"]
hard_words = ["ate", "drank", "danced", "slept"]

def main_function():
    print("---- Welcome to word guessing game ----")
    print("Choose difficulty: Easy, Medium, Hard or Exit")

    attempts = 0

    # Input validation
    while True:
        user_choice = input("Enter your difficulty level: ").lower()
        if user_choice in ["easy", "medium", "hard", "exit"]:
            break
        print("Invalid choice. Try again.")

    if user_choice == "exit":
        print("--- Thanks for using ---")
        exit()

    # Difficulty selection
    if user_choice == "easy":
        secret = random.choice(easy_words)
        maximum_attempts = 3
    elif user_choice == "medium":
        secret = random.choice(medium_words)
        maximum_attempts = 4
    elif user_choice == "hard":
        secret = random.choice(hard_words)
        maximum_attempts = 5

    def save_password():
        with open("password.txt", "w") as file:
            file.write(secret)

    print(f"The word has {len(secret)} letters")

    # Game loop
    while attempts < maximum_attempts:
        user_input = input("Enter the word: ").lower()
        attempts += 1

        if user_input == secret:
            print("Congrats! You guessed right")
            print(f"You guessed right in {attempts} attempts")
            break
        else:
            print("Wrong guess")
            print(f"You have {maximum_attempts - attempts} attempts left")
            print("Try again")

    # Game over
    if attempts == maximum_attempts and user_input != secret:
        print("--- GAME OVER ---")
        print(f"The secret word is '{secret}'")

    # Save option
    choice = input("Do you want to save the secret word? (yes/no): ").lower()
    if choice == "yes":
        save_password()
        print("Secret word saved.")


# First run
main_function()

# Play again loop
while True:
    user_input = input("Do you want to play again? (yes/no): ").lower()

    if user_input == "yes":
        print("Restarting the game...")
        main_function()
    elif user_input == "no":
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("Please enter yes or no.")