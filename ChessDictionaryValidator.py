print("name:T P Aswathi\nsec:o\nusn:1AY24AI109")

def is_valid_chess_board(board):
    valid_files = 'abcdefgh'
    valid_ranks = '12345678'
    valid_positions = {f + r for f in valid_files for r in valid_ranks}
    valid_pieces = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}

    piece_count = {
        'w': {'total': 0, 'pawn': 0},
        'b': {'total': 0, 'pawn': 0}
    }

    for position, piece in board.items():
        if position not in valid_positions:
            print(f"Invalid position: {position}")
            return False
        if len(piece) < 2 or piece[0] not in 'wb' or piece[1:] not in valid_pieces:
            print(f"Invalid piece: {piece}")
            return False

        color = piece[0]
        piece_name = piece[1:]
        
        piece_count[color]['total'] += 1
        if piece_name == 'pawn':
            piece_count[color]['pawn'] += 1

        if piece_count[color]['total'] > 16:
            print(f"Too many {color} pieces")
            return False
        if piece_count[color]['pawn'] > 8:
            print(f"Too many {color} pawns")
            return False
    return True
if __name__ == "__main__":
    test_board = {
        'a1': 'wrook', 'b1': 'wknight', 'c1': 'wbishop', 'd1': 'wqueen',
        'e1': 'wking', 'f1': 'wbishop', 'g1': 'wknight', 'h1': 'wrook',
        'a2': 'wpawn', 'b2': 'wpawn', 'c2': 'wpawn', 'd2': 'wpawn',
        'e2': 'wpawn', 'f2': 'wpawn', 'g2': 'wpawn', 'h2': 'wpawn',
        'a7': 'bpawn', 'b7': 'bpawn', 'c7': 'bpawn', 'd7': 'bpawn',
        'e7': 'bpawn', 'f7': 'bpawn', 'g7': 'bpawn', 'h7': 'bpawn',
        'a8': 'brook', 'b8': 'bknight', 'c8': 'bbishop', 'd8': 'bqueen',
        'e8': 'bking', 'f8': 'bbishop', 'g8': 'bknight', 'h8': 'brook'
    }

    if is_valid_chess_board(test_board):
        print("The chess board is valid.")
    else:
        print("The chess board is invalid.")
