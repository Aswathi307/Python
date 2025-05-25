print("Name:T P Aswathi\nsec:O\nusn :1AY24AI109")
def print_zigzag(rows, cols):
    for row in range(rows):
        for col in range(cols):
            if (row + col) % 2 == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print_zigzag(5, 10)
