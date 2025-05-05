#!/usr/bin/python3

def print_board(board):
    """Print the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if a player has won the game."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    board = [[" "]*3 for _ in range(3)]  # Initialize a 3x3 board
    player = "X"

    while not check_winner(board):
        print_board(board)
        
        # Input validation for row and column
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

                # Check if the input is within bounds
                if 0 <= row < 3 and 0 <= col < 3:
                    if board[row][col] == " ":
                        break  # Exit the loop if the spot is valid
                    else:
                        print("That spot is already taken! Try again.")
                else:
                    print("Invalid input! Row and column must be between 0 and 2. Try again.")
            except ValueError:
                print("Invalid input! Please enter numeric values for row and column.")

        # Update the board with the player's move
        board[row][col] = player

        # Switch player
        player = "O" if player == "X" else "X"

    print_board(board)
    print(f"Player {player} wins!")

tic_tac_toe()
