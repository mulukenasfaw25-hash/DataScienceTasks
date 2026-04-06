def print_board(board):
   for row in [board[i:i+3] for i in range(0, 9, 3)]:
       print("| " + " | ".join(row) + " |")

def check_win(b, p):
   vic = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
   return any(all(b[i] == p for i in v) for v in vic)

def tic_tac_toe():
   board = [str(i+1) for i in range(9)]
   curr = "X"
   for _ in range(9):
       print_board(board)
       move = int(input(f"Player {curr}, choose (1-9): ")) - 1
       if board[move] not in "XO":
           board[move] = curr
           if check_win(board, curr):
               print_board(board)
               return print(f"Player {curr} wins!")
           curr = "O" if curr == "X" else "X"
   print("It's a draw!")

tic_tac_toe()


