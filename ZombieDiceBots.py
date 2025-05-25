print("name:T P Aswathi\nsec:o\nusn:1AY24AI109")
import zombiedice
class SimpleBot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        rolls = 0
        result = zombiedice.roll()
        rolls += 1

        while result is not None and rolls < 2:
            result = zombiedice.roll()
            rolls += 1
zombies = (
    SimpleBot("SimpleBot"),
    zombiedice.examples.RandomCoinFlipZombie(name="RandomBot"),
)

zombiedice.runWebGui(zombies=zombies, numGames=5)
