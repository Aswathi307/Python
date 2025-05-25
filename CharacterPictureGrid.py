print("name:T P Aswathi\nsec:o\nusn:1AY24AI109")
grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]

# Print rotated picture (90 degrees clockwise)
for x in range(len(grid[0])):  
    for y in range(len(grid)): 
        print(grid[y][x], end='')
    print() 
