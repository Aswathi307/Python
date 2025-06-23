print("name:T P Aswathi\n","sec:o\n","usn:1AY24AI109")
import random

def get_toss():
    return 'heads' if random.randint(0, 1) == 1 else 'tails'
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower()

toss = get_toss()

if guess == toss:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input().lower()
    if guess == toss:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
