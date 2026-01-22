board = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            [" ", " ", " "]
        ]

def print_board():
    for row in board:
        print(f"{row[0]}|{row[1]}|{row[2]}")

players = ["x", "o"]
idx = 0
player = players[idx]


running = True
while running:
    print_board()
    print(f"Player {player}'s turn")
    idx = (idx + 1) % len(players)
    player = players[idx]
    row = input("Please enter your chosen row: ")
    while not row.isdigit() or int(row) < 0 or int(row) > 4:
        row = input("Please enter an integer from 1 to 3: ")
    column = input("Please enter your chosen column: ")
    while not column.isdigit() or int(column) < 0 or int(row) > 4:
        column = input("Please enter an integer from 1 to 3: ")
    if board[row-1][column-1] != "_" or board[row-1][column-1] != " ":
        pass


