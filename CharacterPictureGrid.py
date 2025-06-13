print("name:T P Aswathi\nsec:o\nusn:1AY24AI109")
def create_character_grid(rows, cols, char):
    
    grid = []
    for _ in range(rows):
        row = [char] * cols
        grid.append(row)
    return grid

def print_character_grid(grid):
    """Print the character grid to the console."""
    for row in grid:
        print(' '.join(row))

def main():
    rows = 5
    cols = 10
    char = '*'

    grid = create_character_grid(rows, cols, char)
    print_character_grid(grid)

if __name__ == "__main__":
    main()
