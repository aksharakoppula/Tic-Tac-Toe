board = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            [" ", " ", " "]
        ]

def print_board():
    print()
    for row in board:
        print(f"{row[0]}|{row[1]}|{row[2]}")
    print()

players = ["x", "o"]
idx = 0
player = players[idx]

def prompt_user():
    row = input("Please enter your chosen row: ")
    while not row.isdigit() or int(row) < 1 or int(row) > 3:
        row = input("Please enter an integer from 1 to 3: ")
    column = input("Please enter your chosen column: ")
    while not column.isdigit() or int(column) < 1 or int(column) > 3:
        column = input("Please enter an integer from 1 to 3: ")
    return int(row), int(column)

def check_winner():
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "_" and board[i][0] != " ":
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] and board[0][i] != "_" and board[0][i] != " ":
            return board[0][i]
        else:
            return False
    if board[0][0] == board[1][1] == board[2][2] and board [0][0] != "_" and board[0][0] != " ":
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[1][1] != "_" and board[1][1] != " ":
        return board[1][1]
    else:
        return "Tie!"

running = True
while running:
    print_board()
    print(f"Player {player}'s turn")
    row, column = prompt_user()
    while board[row-1][column-1] != "_" and board[row-1][column-1] != " ":
        print("Position Already Taken")
        row, column = prompt_user()
    board[row-1][column-1] = player
    print_board()
    idx = (idx + 1) % len(players)
    player = players[idx]
