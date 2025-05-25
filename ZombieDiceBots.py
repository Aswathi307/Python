print("name:T P Aswathi\nsec:o\nusn:1AY24AI109")
dice_pool = [
    ('green', ['brain', 'brain', 'brain', 'footprint', 'footprint', 'shotgun']),
    ('yellow', ['brain', 'brain', 'footprint', 'footprint', 'shotgun', 'shotgun']),
    ('red', ['brain', 'footprint', 'footprint', 'shotgun', 'shotgun', 'shotgun'])
] * 2  # 13 dice total (3 green, 4 yellow, 3 red)

# Strategy bots
def random_bot(score, brains, shotguns):
    return random.choice([True, False])

def cautious_bot(score, brains, shotguns):
    return shotguns < 2

def greedy_bot(score, brains, shotguns):
    return brains < 4 and shotguns < 3

def play_turn(bot_func):
    brains = 0
    shotguns = 0
    footprints = []

    cup = list(dice_pool)
    random.shuffle(cup)

    while True:
        # Get 3 dice (reuse footprints if available)
        dice_to_roll = footprints
        while len(dice_to_roll) < 3 and cup:
            die = random.choice(cup)
            cup.remove(die)
            dice_to_roll.append(die)

        if not dice_to_roll:
            break  # no more dice

        new_footprints = []
        for color, faces in dice_to_roll:
            roll = random.choice(faces)
            if roll == 'brain':
                brains += 1
            elif roll == 'shotgun':
                shotguns += 1
            else:
                new_footprints.append((color, faces))

        print(f"Rolled: {[random.choice(d[1]) for d in dice_to_roll]} | Total Brains: {brains}, Shotguns: {shotguns}")

        if shotguns >= 3:
            print("💥 Too many shotguns! Turn over.\n")
            return 0

        if not bot_func(0, brains, shotguns):
            break

        dice_to_roll = new_footprints

    print(f"🧠 Scored {brains} brains this turn!\n")
    return brains


# Simulate a game round with different bots
bots = {
    'RandomBot': random_bot,
    'CautiousBot': cautious_bot,
    'GreedyBot': greedy_bot
}

scores = {name: 0 for name in bots}

print("🎲 Starting Zombie Dice Simulation!\n")

for name, bot in bots.items():
    print(f"🧟 {name}'s turn:")
    score = play_turn(bot)
    scores[name] += score

print("🏁 Final Scores:")
for name, score in scores.items():
    print(f"{name}: {score} brains")
