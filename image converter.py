def display_board(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()

def check_win(board, player):
    # Check rows for a win
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns for a win
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals for a win
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    # No win found
    return False

def make_move(board, player, position):
    if board[position[0]][position[1]] != '-':
        return False
    board[position[0]][position[1]] = player
    return True

def switch_player(current_player):
    if current_player == 'X':
        return 'O'
    else:
        return 'X'

def play_game():
    board = [['-', '-', '-'],
              ['-', '-', '-'],
              ['-', '-', '-']]

    current_player = 'X'

    while True:
        display_board(board)

        # Get player's move
        position = input(f"{current_player}'s turn. Enter a position (row, column): ")
        position = [int(i) for i in position.split(',')]

        # Make the move
        if make_move(board, current_player, position):
            # Check for a win
            if check_win(board, current_player):
                display_board(board)
                print(f"{current_player} wins!")
                break

            # Switch players
            current_player = switch_player(current_player)

        # Check for a tie
        if all('-' not in row for row in board):
            display_board(board)
            print("It's a tie!")
            break

if "_name_" == "_main_":
    play_game()