print("name:aswathi\nsec:o\nusn:1AY24AI109")
def is_valid_chess_board(board):
    valid_positions = [f"{row}{col}" for row in range(1, 9) for col in 'abcdefgh']
    valid_pieces = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}

    white_count = 0
    black_count = 0
    white_pawns = 0
    black_pawns = 0
    white_kings = 0
    black_kings = 0

    for position, piece in board.items():
        # Validate position
        if position not in valid_positions:
            print(f"Invalid board position: {position}")
            return False

        # Validate piece format
        if len(piece) < 2 or piece[0] not in 'wb' or piece[1:] not in valid_pieces:
            print(f"Invalid piece: {piece}")
            return False

        # Count pieces
        if piece[0] == 'w':
            white_count += 1
            if piece == 'wpawn':
                white_pawns += 1
            if piece == 'wking':
                white_kings += 1
        else:
            black_count += 1
            if piece == 'bpawn':
                black_pawns += 1
            if piece == 'bking':
                black_kings += 1

    if white_count > 16:
        print("Too many white pieces.")
        return False
    if black_count > 16:
        print("Too many black pieces.")
        return False
    if white_pawns > 8:
        print("Too many white pawns.")
        return False
    if black_pawns > 8:
        print("Too many black pawns.")
        return False
    if white_kings != 1:
        print("Invalid number of white kings.")
        return False
    if black_kings != 1:
        print("Invalid number of black kings.")
        return False

    print("Board is valid.")
    return True
