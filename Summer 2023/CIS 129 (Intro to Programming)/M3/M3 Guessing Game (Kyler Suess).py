# import random

# def guess_number():
#     secret_number = random.randint(1, 100)
#     attempts = 0

    
#     while True:
#         print("Welcome to the Number Guessing Game!")
#         start = input("Press Enter to start or 'q' to quit: ")

#         if start.lower() == 'q':
#             print("Goodbye!")
#             break # Exit the loop
#         else start.lower() == 'Enter':
#             print("I'm thinking of a number between 1 and 100.")
#             continue
        

#         # if guess.lower() == 'q':
#         #      print("Thanks for playing. Goodbye!")
#         #      return  # Exit the function
        
#         try:
#             guess = int(guess)
#             attempts += 1

#             if guess < secret_number:
#                 print("Too low!")
#             elif guess > secret_number:
#                 print("Too high!")
#             else:
#                 print(f"Congratulations! You guessed it in {attempts} attempts.")
#                 break  # Exit the loop

#         except ValueError:
#             print("Invalid input. Please enter a number or 'q' to quit.")

#  input("Press Enter to start the guessing game or 'q' to quit: ")
# guess_number()

import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("Please enter a number 1-100 for a surprise.")

    while True:
        user_guess = input("Take a guess: ")
        
        if user_guess.lower() == 'q':
            print("Thanks for playing. Goodbye!")
            return  # Exit the function if 'q' is pressed

        elif user_guess.isdigit():
            user_guess = int(user_guess)
            attempts += 1

            if user_guess < secret_number:
                print("Too low!")
            elif user_guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                return  # Exit the function if the number is guessed correctly
        else:
            print("Invalid input. Please enter a number or 'q' to quit.")

start_game = input("Press Enter to start the guessing game or 'q' to quit: ")

if start_game == 'q':
    print("Goodbye!")
elif start_game != '':
    print("Invalid input. Please press Enter or 'q' to quit.")
else:
    guessing_game()
