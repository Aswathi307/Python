print("name:T P Aswathi\nsec:O\nusn :1AY24AI109") 

import random

secret_number = random.randint(1, 100)

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        break
