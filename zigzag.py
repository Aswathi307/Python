print("Name:T P Aswathi\nsec:O\nusn :1AY24AI109")
def zigzag_pattern(n):
    for row in range(3):  # Fixed 3 rows for basic zigzag
        for col in range(n):
            if (row + col) % 4 == 0 or (row == 1 and col % 4 == 0):
                print("*", end="")
            else:
                print(" ", end="")
        print()
zigzag_pattern(20)
