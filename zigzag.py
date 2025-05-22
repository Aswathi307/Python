print("Name:T P Aswathi,usn :1AY24AI109,sec:O
def zigzag_pattern(n):
    # n: number of columns
    for row in range(3):  # Fixed 3 rows for basic zigzag
        for col in range(n):
            if (row + col) % 4 == 0 or (row == 1 and col % 4 == 0):
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Example: zigzag of length 20
zigzag_pattern(20)
