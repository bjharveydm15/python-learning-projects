from textwrap import dedent
from dataclasses import dataclass


@dataclass
class Player:
    symbol: str
    score: int = 0


def print_board(board, board_size):
    slots = board_size - 3
    print('---+---+---' + '+---' * slots)

    for r in range(board_size):
        print(" | ".join(board[r]))
        print('---+---+---' + '+---' * slots)


def check_row(board, player, board_size):
    for r in range(board_size):
        if all(board[r][c] == player for c in range(board_size)):
            return True

    return False


def check_columns(board, player, board_size):
    for c in range(board_size):
        if all(board[r][c] == player for r in range(board_size)):
            return True

    return False


def check_main_diagonal(board, player, board_size):
    if all(board[i][i] == player for i in range(board_size)):
        return True

    return False


def check_anti_diagonal(board, player, board_size):
    if all(board[i][board_size - 1 - i] == player for i in range(board_size)):
        return True

    return False


def check_win(board, player, board_size):
    return any([
        check_row(board, player, board_size),
        check_columns(board, player, board_size),
        check_main_diagonal(board, player, board_size),
        check_anti_diagonal(board, player, board_size)
    ])


def get_move_input(board_size):
    while True:
        try:
            row = int(input(f"Enter row (1-{board_size}): ")) - 1
            col = int(input(f"Enter col (1-{board_size}): ")) - 1
        except ValueError:
            print('Invalid input.')
            continue

        return row, col


def is_move_in_range(board_size, row, col):
    return row in range(board_size) and col in range(board_size)


def is_cell_occupied(board, row, col):
    return board[row][col] != ' '


def get_move(board, board_size):
    while True:
        row, col = get_move_input(board_size)

        if not is_move_in_range(board_size, row, col):
            print("Invalid input.")
            continue

        if is_cell_occupied(board, row, col):
            print("Cell already taken.")
            continue

        return row, col


def will_reset_game_scores():
    while True:
        restart = input('Do you want to reset game scores? (y/n): ').lower()

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


def board_size_input():
    while True:
        board_size = input(
            dedent(
                '''\
                Please choose a board size.  
                3 for 3X3
                4 for 4X4
                5 for 5X5\
                '''
            )
        )

        try:
            return int(board_size)
        except ValueError:
            print('Invalid input.')
            continue


def is_board_size_in_range(board_size):
    return board_size in (3, 4, 5)


def ask_board_size():
    while True:
        board_size = board_size_input()

        if not is_board_size_in_range(board_size):
            print('Invalid input.')
            continue

        return board_size


def create_board(board_size):
    return [[' ' for _ in range(board_size)] for _ in range(board_size)]


def show_player_roles(player_1, player_2):
    print(
        dedent(
            f'''\
            Player 1 plays as {player_1.symbol}
            Player 2 plays as {player_2.symbol}\
             '''
        )
    )


def show_player_turn(player_mark, player_1):
    if player_mark == player_1.symbol:
        print("Player 1's turn")
    else:
        print("Player 2's turn")


def declare_winner(player_mark, player_1, player_2):
    if player_mark == player_1.symbol:
        player_1.score += 1
        winner = 'Player 1'
    else:
        player_2.score += 1
        winner = 'Player 2'

    print(
        dedent(
            f"""
            {winner} wins!

            Scoreboard:
            Player 1: {player_1.score}
            Player 2: {player_2.score}
            """
        )
    )


def declare_draw(player_1, player_2):
    print(
        dedent(
            f"""
            It's a draw!

            Scoreboard:
            Player 1: {player_1.score}
            Player 2: {player_2.score}
            """
        )
    )


def main():
# --------------------------- Game setup -------------------------------
    player_1 = Player('X')
    player_2 = Player('O')

    board_size = ask_board_size()

    while True:
        show_player_roles(player_1, player_2)
        board = create_board(board_size)

        player_mark = 'X'
        moves = 0

# -----------------------------------------------------------------------
# --------------------------- Game round -------------------------------
# -----------------------------------------------------------------------

# --------------------------- Player turn -------------------------------
        while True:
            print_board(board, board_size)
            show_player_turn(player_mark, player_1)

            r, c = get_move(board, board_size)

            board[r][c] = player_mark
            moves += 1

# --------------------------- Check for winner or draw -------------------------------
            if check_win(board, player_mark, board_size):
                print_board(board, board_size)
                declare_winner(player_mark, player_1, player_2)
                break

            if moves == board_size * board_size:
                print_board(board, board_size)
                declare_draw(player_1, player_2)
                break

# --------------------------- Change player turn -------------------------------
            player_mark = 'O' if player_mark == 'X' else 'X'

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
        another_game = continue_playing()

        if another_game == 'y':
            reset = will_reset_game_scores()

            if reset == 'y':
                player_1.score = 0
                player_2.score = 0
                board_size = ask_board_size()

        else:
            break

# --------------------------- Change player mark -------------------------------
        player_1.symbol, player_2.symbol = player_2.symbol, player_1.symbol


if __name__ == "__main__":
    main()
