import random

# Display the board
def display_board(board):
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print('--+---+--')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print('--+---+--')
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print('-' * 10)

# Let the human choose X or O
def player_input():
    while True:
        marker = input("Enter X or O: ").upper()
        if marker == "X":
            return "X", "O"
        elif marker == "O":
            return "O", "X"
        else:
            print("Invalid Input. Please choose X or O.")

# Place a marker
def place_marker(board, marker, position):
    board[position] = marker

# Check win
def win_check(board, marker):
    return (
        (board[1] == board[2] == board[3] == marker) or
        (board[4] == board[5] == board[6] == marker) or
        (board[7] == board[8] == board[9] == marker) or
        (board[1] == board[4] == board[7] == marker) or
        (board[2] == board[5] == board[8] == marker) or
        (board[3] == board[6] == board[9] == marker) or
        (board[1] == board[5] == board[9] == marker) or
        (board[3] == board[5] == board[7] == marker)
    )

# Check space
def space_available(board, position):
    return board[position] == ' '

# Human move
def human_move(board, human):
    while True:
        pos = input("Enter the position (1-9): ")
        if not pos.isdigit():
            print("Please enter a number between 1 and 9.")
            continue
        pos = int(pos)
        if pos in range(1, 10) and space_available(board, pos):
            place_marker(board, human, pos)
            break
        else:
            print("Invalid Input or position already taken. Try again.")

# Computer move
def computer_move(board, computer):
    while True:
        pos = random.randint(1, 9)
        if space_available(board, pos):
            place_marker(board, computer, pos)
            break

# Board full?
def board_full(board):
    return ' ' not in board[1:]

# Main game loop with replay
def play_game():
    while True:  # Loop for replay
        board = [' '] * 10
        human, computer = player_input()
        turn = random.choice(['Human', 'Computer'])
        print(f"{turn} will go first!\n")

        while True:
            display_board(board)
            if turn == 'Human':
                human_move(board, human)
                if win_check(board, human):
                    display_board(board)
                    print("🎉 Human Wins!")
                    break
                turn = 'Computer'
            else:
                computer_move(board, computer)
                if win_check(board, computer):
                    display_board(board)
                    print("💻 Computer Wins!")
                    break
                turn = 'Human'

            if board_full(board):
                display_board(board)
                print("It's a Tie!")
                break

        replay = input("Do you want to play again? (Y/N): ").upper()
        if replay != 'Y':
            print("Thanks for playing!")
            break

# Run the game
play_game()
