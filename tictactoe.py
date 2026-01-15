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
    idx = idx + 1 % len(players)

