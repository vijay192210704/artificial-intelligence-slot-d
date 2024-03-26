def print_board(board):
    """
    Print the Tic Tac Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """
    Check if there is a winner.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col] 

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def is_board_full(board):
    """
    Check if the board is full.
    """
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_player_move(player):
    """
    Get the player's move.
    """
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0, 1, 2): "))
            col = int(input(f"Player {player}, enter column (0, 1, 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid input. Please enter row and column numbers between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter integers.")

def play_tic_tac_toe():
    """
    Play the Tic Tac Toe game.
    """
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row, col = get_player_move(players[current_player])
        if board[row][col] != ' ':
            print("That position is already taken. Try again.")
            continue

        board[row][col] = players[current_player]
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    play_tic_tac_toe()
