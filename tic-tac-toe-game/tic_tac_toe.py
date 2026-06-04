def print_board(board, board_size):
    slots = board_size - 3
    print('---+---+---' + '+---' * slots)

    for r in range(board_size):
        print(" | ".join(board[r]))
        print('---+---+---' + '+---' * slots)

def check_win(board, player, board_size):
    # rows
    for r in range(board_size):
        if all(board[r][c] == player for c in range(board_size)):
            return True

    # columns
    for c in range(board_size):
        if all(board[r][c] == player for r in range(board_size)):
            return True

    # main diagonal
    if all(board[i][i] == player for i in range(board_size)):
        return True

    # anti-diagonal
    if all(board[i][board_size - 1 - i] == player for i in range(board_size)):
        return True

    return False

def get_move(board, board_size):
    while True:

        try:
            row = int(input(f"Enter row (1-{board_size}): ")) - 1
            col = int(input(f"Enter col (1-{board_size}): ")) - 1
        except ValueError:
            print('Invalid input.')
            continue

        if row not in range(board_size) or col not in range(board_size):
            print("Invalid input.")
            continue

        if board[row][col] != ' ':
            print("Cell already taken.")
            continue

        return row, col

def restart_game():
    while True:
        restart = input('Do you want to restart the match? (y/n): ').lower()

        if restart not in ('y', 'n'):
            print("Invalid input.")
            continue

        return restart

def continue_playing():
    while True:
        another_game = input('Do you want to continue playing? (y/n): ').lower()

        if another_game not in ('y', 'n'):
            print("Invalid input.")
            continue

        return another_game

def ask_board_size():
    while True:
        try:
            board_size = int(input('''Please choose a board size.  
3 for 3X3
4 for 4X4
5 for 5X5
'''))
        except ValueError:
            print('Invalid input.')
            continue

        if board_size not in (3, 4, 5):
            print("Invalid input.")
            continue

        return board_size


def main():
    player1_score = 0
    player2_score = 0

    player_1 = 'X'
    player_2 = 'O'

    board_size = ask_board_size()

    while True:
        print(f'''
Player 1 plays as {player_1}
Player 2 plays as {player_2}
''')
        board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        player = 'X'
        moves = 0

        while True:
            print_board(board, board_size)

            if player == player_1:
                print("Player 1's turn")
            else:
                print("Player 2's turn")

            r, c = get_move(board, board_size)

            board[r][c] = player
            moves += 1

            if check_win(board, player, board_size):
                print_board(board, board_size)

                if player == player_1:
                    player1_score += 1
                    winner = 'Player 1'
                else:
                    player2_score += 1
                    winner = 'Player 2'

                print(f"""
{winner} wins!

Scoreboard:
Player 1: {player1_score}
Player 2: {player2_score}
""")

                break

            if moves == board_size * board_size:
                print_board(board, board_size)
                print(f"""
It's a draw!

Scoreboard:
Player 1: {player1_score}
Player 2: {player2_score}
""")

                break

            player = 'O' if player == 'X' else 'X'

        another_game = continue_playing()

        if another_game == 'y':
            restart = restart_game()

            if restart == 'y':
                player1_score = 0
                player2_score = 0
                board_size = ask_board_size()

        else:
            break


        player_1, player_2 = player_2, player_1


if __name__ == "__main__":
    main()
