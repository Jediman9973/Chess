def white_pawn_legal(figure, pos):


    """calculate row and col for internal state """
    row = 8 - int(pos[1])  # 1 -> 7, 2 -> 6, ... 8->0
    col = ord(pos[0]) - ord("A")  # letter, A = 0, B = 1, ..., H = 7

    """moving forward, so row is changing, column staying the same"""
    if figure[0] == pos[0] and int(figure[1])+1 == int(pos[1]):         #going up by 1
        print("Moving to " +pos[0] + pos[1])
        return True

    if int(figure[1]) == 2:                                             #if at base rank, we can go two up
        if figure[0] == pos[0] and int(figure[1]) + 2 == int(pos[1]):  # going up by 1
            print("Moving to " + pos[0] + pos[1])
            return True

    """moving diagonally to take a piece"""
    if abs(ord(figure[0])-ord(pos[0])) == 1 and int(figure[1])+1 == int(pos[1]):
        if board[row][col].islower():
            print("Taking!")
            return True
        else:
            print("Nothing to take")
            return False

    print("You cannot go there")
    return False

def black_pawn_legal(figure, pos):


    """calculate row and col for internal state """
    row = 8 - int(pos[1])  # 1 -> 7, 2 -> 6, ... 8->0
    col = ord(pos[0]) - ord("A")  # letter, A = 0, B = 1, ..., H = 7

    """moving forward, so row is changing, column staying the same"""
    if figure[0] == pos[0] and int(figure[1])-1 == int(pos[1]):         #going down by 1
        print("Moving to " +pos[0] + pos[1])
        return True

    if int(figure[1]) == 7:                                             #if at base rank, we can go two down
        if figure[0] == pos[0] and int(figure[1]) - 2 == int(pos[1]):
            print("Moving to " + pos[0] + pos[1])
            return True

    """moving diagonally to take a piece"""
    if abs(ord(figure[0])-ord(pos[0])) == 1 and int(figure[1])-1 == int(pos[1]):
        if board[row][col].isupper():
            print("Taking!")
            return True
        else:
            print("Nothing to take")
            return False

    print("You cannot go there")
    return False

def legal_position(figure):
    """check if the position is valid in chess """
    if len(figure) != 2 or not figure[0].isalpha() or not figure[1].isdigit():
        print("Invalid input format. Please enter a valid square (e.g., E2).")
        return False

    """calculate row and col for internal state"""
    row = 8 - int(figure[1])  # 1 -> 7, 2 -> 6, ... 8->0
    col = ord(figure[0]) - ord("A")  # letter, A = 0, B = 1, ..., H = 7

    """if out bound, let player choose again"""
    if row < 0 or row >= 8 or col < 0 or col >= 8:
        print("Choose a valid position.")
        return False

    return True


def white_piece(figure):
    """calculate row and col for internal state"""
    row = 8 - int(figure[1])  # 1 -> 7, 2 -> 6, ... 8->0
    col = ord(figure[0]) - ord("A")  # letter, A = 0, B = 1, ..., H = 7

    """if not white piece chosen, let player choose again"""
    piece = board[row][col]
    if piece == "." or piece.islower():
        print("Not a valid white figure.")
        return False

    return piece

def black_piece(figure):
    """calculate row and col for internal state"""
    row = 8 - int(figure[1])  # 1 -> 7, 2 -> 6, ... 8->0
    col = ord(figure[0]) - ord("A")  # letter, A = 0, B = 1, ..., H = 7

    """if not white piece chosen, let player choose again"""
    piece = board[row][col]
    if piece == "." or piece.isupper():
        print("Not a valid black figure.")
        return False

    return piece

def update_board(figure, pos, piece):
    global board
    row = 8 - int(figure[1])  # 1 -> 7, 2 -> 6, ... 8->0
    col = ord(figure[0]) - ord("A")  # letter, A = 0, B = 1, ..., H = 7

    board[row][col] = "."

    row = 8 - int(pos[1])  # 1 -> 7, 2 -> 6, ... 8->0
    col = ord(pos[0]) - ord("A")  # letter, A = 0, B = 1, ..., H = 7

    board[row][col] = piece



board = [["."]*8 for _ in range(8)]

#white pieces
board[7] = ["R", "N", "B", "Q", "K", "B", "N", "R"]
board[6] = ["P"]*8#print(board[7])

#black pieces
board[0] = ["r", "n", "b", "q", "k", "b", "n", "r"]
board[1] = ["p"]*8

for row in board:
    print(" ".join(row))


white = True

while True:

    """white's move"""

    if white:
        figure = input("Enter your piece as white: ").upper()

        while not legal_position(figure):
            figure = input().upper()

        if not white_piece(figure):
            continue

        piece = white_piece(figure)

        print(f"White chose {piece} at {figure}")


        if piece == "P":
            to_pos = input(f"Where to go with pawn from {figure}? ")

            while not legal_position(to_pos):
                to_pos = input(f"Where to go with pawn from {figure}? ")

            while not white_pawn_legal(figure, to_pos):
                to_pos = input(f"Where to go with pawn from {figure}? ")


        update_board(figure, to_pos, piece)

        for row in board:
            print(" ".join(row))

        white = False


    else:

        figure = input("Enter your piece as black: ").upper()

        while not legal_position(figure):
            figure = input().upper()

        if not black_piece(figure):
            continue

        piece = black_piece(figure)

        print(f"Black chose {piece} at {figure}")

        if piece == "p":
            to_pos = input(f"Where to go with pawn from {figure}? ")

            while not legal_position(to_pos):
                to_pos = input(f"Where to go with pawn from {figure}? ")

            while not black_pawn_legal(figure, to_pos):
                to_pos = input(f"Where to go with pawn from {figure}? ")


        update_board(figure, to_pos, piece)

        for row in board:
            print(" ".join(row))


        white = True



