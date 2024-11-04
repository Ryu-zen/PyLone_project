# Tic Tac Toe Game in Python

# Function to print the game board
def print_board(board):
    print("Current board:")
    print(" %s | %s | %s " % (board[1], board[2], board[3]))
    print("---|---|---")
    print(" %s | %s | %s " % (board[4], board[5], board[6]))
    print("---|---|---")
    print(" %s | %s | %s " % (board[7], board[8], board[9]))
    print()

# Function to check for a win
def check_win(board):
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Horizontal
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Vertical
        (1, 5, 9), (3, 5, 7)               # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True
    return False

# Function to check for a draw
def check_draw(board):
    return ' ' not in board[1:]

# Main game function
def tic_tac_toe():
    board = [' '] * 10  # Create a board with 10 spaces (index 0 unused)
    current_player = 'X'
    
    while True:
        print_board(board)
        move = int(input(f"Player {current_player}, enter your move (1-9): "))
        
        if board[move] == ' ':
            board[move] = current_player
            if check_win(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move! Try again.")

# Start the game
if __name__ == "__main__":
    tic_tac_toe()
