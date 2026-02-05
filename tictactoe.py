board = [
            ["_","_","_"],
            ["_","_","_"],
            [" "," "," "]
         ]

def print_board():
     print()
     for row in board:
          print(f"{row[0]}|{row[1]}|{row[2]}")
     print()

players = ["x","o"]
index=0
player=players[index]

def prompt_user():
     row = input("Please enter your chosen row: ") 
     while not row.isdigit() or int(row) < 1 or int(row) > 3:
          row = input("Please give me an integer between 1 and 3: ")
     column = input("Please enter your chosen column: ")
     while not column.isdigit() or int(column) < 1 or int(column) > 3:
          column = input("Please give me an integer between 1 and 3: ")
     return int(row), int(column)

def check_winner():
     #Check for winning horizontally or winning vertically
     for i in range(len(board)):
          if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "_" and board[i][0] != " ":
               return board[i][0]
          elif board[0][i] == board[1][i] == board[2][i] and board[0][i] != "_" and board[0][i] != " ":
               return board[0][i]

     #Check for winning diagonally     
     if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_" and board[0][0] != " ":
          return board[0][0]
     elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_" and board [0][2] != " ":
          return board[0][2]
     
     #Check if any empty spaces still on board     
     for row in range(3):
          for col in range(3):
               if board[row][col] == "_" or board[row][col] == " ":
                    return False
          
     #Nobody won
     return "Tie"
     
running = True
while running:
     print_board()
     print(f"Player {player}'s turn")
     row, column = prompt_user()
     while board[row-1][column-1] != "_" and board[row-1][column-1] != " ":
          print("Position already taken")
          row, column = prompt_user()
     board[row-1][column-1] = player
     print_board()
     is_winner = check_winner()
     if is_winner == False:
          index= (index+1) % len(players)
          player=players[index]
          continue
     else:
          if is_winner == "Tie":
               print("It's a tie!")
          else:
               print(f"Player {is_winner} won!")
          running = False


