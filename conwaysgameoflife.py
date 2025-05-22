print("Name:T P Aswathi,usn:1AY24AI109,sec:O")
import time
import os
import copy

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_grid(grid):
    for row in grid:
        print(''.join([' ' if cell else ' ' for cell in row]))
    print()

def count_neighbors(grid, x, y):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            ni, nj = x + i, y + j
            if 0 <= ni < rows and 0 <= nj < cols:
                count += grid[ni][nj]
    return count

def update_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = copy.deepcopy(grid)

    for i in range(rows):
        for j in range(cols):
            neighbors = count_neighbors(grid, i, j)
            if grid[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j] = 0
            else:
