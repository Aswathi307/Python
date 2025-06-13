print("name:T P Aswathi\nsec:o\nusn:1AY24AI109")
def is_valid_square(square):
        if len(square) != 2:
        return False
    file, rank = square[0], square[1]
    return file in 'abcdefgh' and rank in '12345678'

def is_valid_piece(piece):
    
    valid_pieces = {'p', 'r', 'n', 'b', 'q', 'k'}
    if piece == '':  
        return True
    if len(piece) != 2:
        return False
    color, p = piece[0], piece[1].lower()
    return color in ('w', 'b') and p in valid_pieces

def validate_chess_dict(chess_dict):
   
    for square, piece in chess_dict.items():
        if not is_valid_square(square):
            print(f"Invalid square: {square}")
            return False
        if not is_valid_piece(piece):
            print(f"Invalid piece: {piece} at {square}")
            return False
    return True

if __name__ == "__main__":

    chess_board = {
                'a1': 'wr', 'b1': 'wn', 'c1': 'wb', 'd1': 'wq', 'e1': 'wk', 'f1': 'wb', 'g1': 'wn', 'h1': 'wr',
        'a2': 'wp', 'b2': 'wp', 'c2': 'wp', 'd2': 'wp', 'e2': 'wp', 'f2': 'wp', 'g2': 'wp', 'h2': 'wp',
        'a3': '', 'b3': '', 'c3': '', 'd3': '', 'e3': '', 'f3': '', 'g3': '', 'h3': '',
        'a8': 'br', 'b8': 'bn', 'c8': 'bb', 'd8': 'bq', 'e8': 'bk', 'f8': 'bb', 'g8': 'bn', 'h8': 'br',
        'h9': 'wp', 
    }

    if validate_chess_dict(chess_board):
        print("Chess dictionary is valid!")
    else:
        print("Chess dictionary is invalid.")
