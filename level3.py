def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")
    print("\n")


def check_win(board, player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # columns
        [0,4,8],[2,4,6]           # diagonals
    ]
    return any(all(board[i] == player for i in pos) for pos in win_positions)


def get_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, choose position (1-9): "))
            if move < 1 or move > 9:
                print("⚠️ Choose a number between 1 and 9.")
            elif board[move - 1] in ["X", "O"]:
                print("⚠️ That spot is already taken.")
            else:
                return move - 1
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")


def play_game():
    board = [str(i+1) for i in range(9)]
    current_player = "X"

    for turn in range(9):
        print_board(board)
        move = get_move(board, current_player)
        board[move] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("🤝 It's a draw!")


def tic_tac_toe():
    while True:
        play_game()
        again = input("Play again? (yes/no): ").lower()
        if again != 'y':
            print("Thanks for playing! 👋")
            break


# Run the game
tic_tac_toe()