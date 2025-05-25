print("name:T P Aswathi\nsec:o\nusn:1AY24AI109")
import random

def coin_flip_streaks(num_flips=10000, streak_length=6):
    flips = []
    for _ in range(num_flips):
        flips.append(random.choice(['H', 'T']))  # H for heads, T for tails

    streaks = 0
    current_streak = 1

    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            current_streak += 1
            if current_streak == streak_length:
                streaks += 1
        else:
            current_streak = 1

    print(f'Number of streaks of {streak_length} or more: {streaks}')
    # Optional: Uncomment to see the flip results
    # print(''.join(flips))

coin_flip_streaks()
