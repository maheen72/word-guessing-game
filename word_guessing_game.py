#     ------------------------ WORD GUESSING GAME ------------------------

import random

Easy = ["eat" , "sleep" , "drink" , "dance"]
Medium = ["eating" , "drinking" , "dancing" , "sleeping"]
Hard = ["ate" , "drank" , "danced" , "slept"]

def main_function():
    print("---- Welcome to word guessing game ----")
    print("What you want to guess : Easy, Medium and Hard or Exit")

    Attempt = 0
    user_choice = input("Enter your difficuilty_level:").lower()

    if user_choice == "easy":
     secret = random.choice(Easy)
     maximum_attempts = 3

    elif user_choice == "medium":
     secret = random.choice(Medium)
     maximum_attempts = 4
    
    elif user_choice == "hard":
     secret = random.choice(Hard)
     maximum_attempts = 5

    elif user_choice == "Exit":
     print("---Thanks for using---")
     exit()

    else:
     print("invalid choice enter right one")
     return

    def save_password():
     with open("password.txt" , "w") as file:
      file.write(secret)
    
    while Attempt < maximum_attempts :
      user_input = input("Enter the word:").lower()
      Attempt += 1

      if user_input == secret :
       print("congrats! you guess right")
       print(f"you guess right in {Attempt} Attempts")
       break
        
      else:
        print("OHH... you guess wrong")
        print(f"you have {maximum_attempts - Attempt} attempts left")
        print("try again")

    if Attempt == maximum_attempts:
     print("--- GAME OVER ---")
     print(f"the secret word is '{secret}'")

    
    choice = input("Do you want to save the secret word? (yes/no): ").lower()
    if choice == "yes":
       save_password()
       print("Secret word saved.")
main_function()

while True:
 user_input = input("Do you want to play again? (yes/no): ").lower()
 if user_input == "yes":
    print("Restarting the game...")
    main_function()
 else:
    print("Thanks for playing! Goodbye.")
    exit()