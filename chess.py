def calculate_row_col(pos):
    row = 8 - int(pos[1])  # 1 -> 7, 2 -> 6, ... 8 -> 0
    col = ord(pos[0]) - ord('A')  # A -> 0, B -> 1, ..., H -> 7
    return row, col

def legal_position(figure):
    if len(figure) != 2 or not figure[0].isalpha() or not figure[1].isdigit():
        print("Invalid format")
        return False

    row, col = calculate_row_col(figure)
    if row < 0 or row >= 8 or col < 0 or col >= 8:
        print("Invalid position")
        return False

    return True

def white_pawn_legal(figure, pos):
    row_now, col_now = calculate_row_col(figure)
    row, col = calculate_row_col(pos)

    if figure[0] == pos[0] and int(figure[1])+1 == int(pos[1]) and board[row_now-1][col_now] == ".":
        return True

    if int(figure[1]) == 2:
        if figure[0] == pos[0] and int(figure[1]) + 2 == int(pos[1]) and board[row_now-1][col_now] == board[row_now-2][col_now] == ".":
            return True

    if abs(ord(figure[0])-ord(pos[0])) == 1 and int(figure[1])+1 == int(pos[1]):
        if board[row][col].islower():
            return True

    return False

def black_pawn_legal(figure, pos):
    row_now, col_now = calculate_row_col(figure)
    row, col = calculate_row_col(pos)

    if figure[0] == pos[0] and int(figure[1])-1 == int(pos[1]) and board[row_now+1][col_now] == ".":
        return True

    if int(figure[1]) == 7:
        if figure[0] == pos[0] and int(figure[1]) - 2 == int(pos[1]) and board[row_now+1][col_now] == board[row_now+2][col_now] == ".":
            return True

    if abs(ord(figure[0])-ord(pos[0])) == 1 and int(figure[1])-1 == int(pos[1]):
        if board[row][col].isupper():
            return True

    return False

def knight_legal(figure, pos, color):
    row, col = calculate_row_col(pos)

    if abs(ord(figure[0]) - ord(pos[0])) == 1:
        if abs(int(figure[1]) - int(pos[1])) != 2:
            return False

    if abs(int(figure[1]) - int(pos[1])) == 2:
        if abs(ord(figure[0]) - ord(pos[0])) != 1:
            return False

    return True

def rook_legal(figure, pos, color):
    row_now, col_now = calculate_row_col(figure)
    row, col = calculate_row_col(pos)

    if figure[0] != pos[0] and figure[1] != pos[1]:
        return False

    if figure[0] == pos[0]:
        for i in range(min(row_now, row) + 1, max(row_now, row)):
            if board[i][col_now] != ".":
                return False
    else:
        for i in range(min(col_now, col) + 1, max(col_now, col)):
            if board[row_now][i] != ".":
                return False

    return True

def bishop_legal(figure, pos, color):
    row_now, col_now = calculate_row_col(figure)
    row, col = calculate_row_col(pos)

    if abs(row_now - row) != abs(col_now - col):
        return False

    step_row = 1 if row > row_now else -1
    step_col = 1 if col > col_now else -1

    r, c = row_now + step_row, col_now + step_col
    while r != row and c != col:
        if board[r][c] != ".":
            return False
        r += step_row
        c += step_col

    return True

def queen_legal(figure, pos, color):
    return rook_legal(figure, pos, color) or bishop_legal(figure, pos, color)

def king_legal(figure, pos, color):
    row_now, col_now = calculate_row_col(figure)
    row, col = calculate_row_col(pos)

    if max(abs(row_now - row), abs(col_now - col)) > 1:
        return False

    return True

def white_piece(figure):
    row, col = calculate_row_col(figure)
    piece = board[row][col]
    if piece == "." or piece.islower():
        return False
    return piece

def black_piece(figure):
    row, col = calculate_row_col(figure)
    piece = board[row][col]
    if piece == "." or piece.isupper():
        return False
    return piece

def update_board(figure, pos, piece):
    global board
    row_now, col_now = calculate_row_col(figure)
    board[row_now][col_now] = "."
    row, col = calculate_row_col(pos)
    board[row][col] = piece

def display_board():
    for row in board:
        print(" ".join(row))

board = [["."]*8 for _ in range(8)]
board[7] = ["R", "N", "B", "Q", "K", "B", "N", "R"]
board[6] = ["P"]*8
board[0] = ["r", "n", "b", "q", "k", "b", "n", "r"]
board[1] = ["p"]*8
display_board()

white = True


while True:
    if white:
        figure = input("Enter your piece as white: ").upper()

        while not legal_position(figure):
            figure = input("Enter your piece as white: ").upper()

        if not white_piece(figure):
            continue

        piece = white_piece(figure)
        print(f"White chose {piece} at {figure}")

        to_pos = input(f"Where to go with {piece} from {figure}? ").upper()
        while not legal_position(to_pos) or not (white_pawn_legal(figure, to_pos) if piece == "P" else
                                                 knight_legal(figure, to_pos, "white") if piece == "N" else
                                                 rook_legal(figure, to_pos, "white") if piece == "R" else
                                                 bishop_legal(figure, to_pos, "white") if piece == "B" else
                                                 queen_legal(figure, to_pos, "white") if piece == "Q" else
                                                 king_legal(figure, to_pos, "white")):
            to_pos = input(f"Where to go with {piece} from {figure}? ").upper()

    else:
        figure = input("Enter your piece as black: ").upper()

        while not legal_position(figure):
            figure = input("Enter your piece as black: ").upper()

        if not black_piece(figure):
            continue

        piece = black_piece(figure)
        print(f"Black chose {piece} at {figure}")

        to_pos = input(f"Where to go with {piece} from {figure}? ")
        while not legal_position(to_pos) or not (black_pawn_legal(figure, to_pos) if piece == "p" else
                                                 knight_legal(figure, to_pos, "black") if piece == "n" else
                                                 rook_legal(figure, to_pos, "black") if piece == "r" else
                                                 bishop_legal(figure, to_pos, "black") if piece == "b" else
                                                 queen_legal(figure, to_pos, "black") if piece == "q" else
                                                 king_legal(figure, to_pos, "black")):
            to_pos = input(f"Where to go with {piece} from {figure}? ")

    update_board(figure, to_pos, piece)
    display_board()
    white = not white



