print("name:T P Aswathi\nsec:O\nusn :1AY24AI109") 

import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    while True:
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if guess < lower_bound or guess > upper_bound:
            print("Out of bounds! Try again.")
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()
