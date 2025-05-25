print("Name:T P Aswathi,usn:1AY24AI109,sec:O")
import time
import os
import copy

def print_board(board):
    for row in board:
        print(''.join(['█' if cell else ' ' for cell in row]))
    print()
def count_neighbors(board, x, y):
    rows = len(board)
    cols = len(board[0])
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            ni, nj = x + i, y + j
            if 0 <= ni < rows and 0 <= nj < cols:
                count += board[ni][nj]
    return count


def next_generation(board):
    rows = len(board)
    cols = len(board[0])
    new_board = copy.deepcopy(board)

    for i in range(rows):
        for j in range(cols):
            neighbors = count_neighbors(board, i, j)
            if board[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_board[i][j] = 0
            else:
                if neighbors == 3:
                    new_board[i][j] = 1
    return new_board


def main():
    board = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]

    generations = 20
    delay = 0.5
    for _ in range(generations):
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board(board)
        board = next_generation(board)
        time.sleep(delay)


if __name__ == "__main__":
    main()
