import tic_tac_toe
import pytest


@pytest.mark.parametrize(
    "board, player, boolean",
    [
        (
            [
                ['x', '', 'o'],
                ['x', 'o', ''],
                ['x', '', 'o'],
            ],
            'x',
            True,
        ),
        (
            [
                ['o', '', 'x'],
                ['x', 'o', ''],
                ['x', '', 'o'],
            ],
            'o',
            True,
        ),
        (
            [
                ['x', 'x', 'o'],
                ['o', 'o', 'x'],
                ['x', 'o', 'o'],
            ],
            'o',
            False,
        ),
(
            [
                ['', '', 'o'],
                ['x', 'o', ''],
                ['x', '', 'o'],
            ],
            'o',
            False,
        ),
    ]
)
def test_check_win(board, player, boolean):
    assert tic_tac_toe.check_win(board, player, len(board)) == boolean


@pytest.mark.parametrize("board, move", [
    (
        [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ],
        ['2', '3'],
    ),
    (
        [
            ['x', ' ', ' '],
            [' ', ' ', ' '],
            [' ', 'o ', ' '],
        ],
        ['1', '3'],
    ),
    (
        [
            ['x', 'o', 'x'],
            [' ', ' ', ' '],
            [' ', 'o ', ' '],
        ],
        ['2', '2'],
    ),
])
def test_get_move(monkeypatch, board, move):
    inputs = iter(move)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    expected_row = int(move[0]) - 1
    expected_col = int(move[1]) - 1

    result = tic_tac_toe.get_move(board, 3)
    assert result == (expected_row, expected_col)


@pytest.mark.parametrize("user_input, expected", [
    (['2', '3', '1', '2'], (0, 1)),
    (['3', '1', '3', '2', '2', '1', '4'], (1, 0)),
    (['1', '4', '2', '2', '2'], (1, 1)),
    (['0', '2', '3', '3', '1', '1'], (2, 2)),
    (['q', '2', 'a', '2', '1'], (1, 0)),
    (['z', '2', 'b', '3', '3'], (2, 2)),
    (['2', 'a', '2', '2'], (1, 1)),
    (['w', '4', 'x', '3', '3', '7', 'b'], (2, 2)),
    (['l', '2', '5', '1', '3'], (0, 2)),
    (['5', '2', 'm', '3', '7', '4', '2', '3', '3', 'a'], (2, 2)),

])
def test_get_move_recurring_inputs(
        monkeypatch, capsys, user_input, expected
):
    board = [
        ['x', ' ', ' '],
        [' ', ' ', 'o'],
        ['o', 'x', ' '],
    ]
    inputs = iter(user_input)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert tic_tac_toe.get_move(board, 3) == expected

    captured = capsys.readouterr()
    assert (
        "Cell already taken" in captured.out
        or "Invalid input." in captured.out
    )


@pytest.mark.parametrize("user_input, expected", [
    ('y', 'y'), ('n', 'n')
])
def test_y_or_n_functions(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)

    assert tic_tac_toe.will_reset_game_scores() == expected
    assert tic_tac_toe.continue_playing() == expected


@pytest.mark.parametrize("func", [
    tic_tac_toe.will_reset_game_scores,
    tic_tac_toe.continue_playing,
])
@pytest.mark.parametrize("user_input, expected", [
    (['a', '2', '3e23e', 'y', '2'], 'y'),
    (['0', 'n', '2'], 'n'),
])
def test_y_or_n_functions_bad_inputs(
    capsys, monkeypatch, func, user_input, expected
):
    inputs = iter(user_input)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    assert func() == expected

    captured = capsys.readouterr()
    assert "Invalid input." in captured.out


@pytest.mark.parametrize("user_input, expected", [
    ('3', 3), ('4', 4), ('5', 5)
])
def test_ask_board_size(monkeypatch, user_input, expected):
    monkeypatch.setattr('builtins.input', lambda _: user_input)

    assert tic_tac_toe.ask_board_size() == expected


@pytest.mark.parametrize("user_input, expected", [
    (['g', 'erq', '32', '0', '3', 'o'], 3),
    (['g', 'erq', '32', '0', '4', 'o'], 4),
    (['g', 'erq', '2', '5', '4', 'o'], 5),
])
def test_ask_board_size_bad_inputs(
    capsys, monkeypatch, user_input, expected
):
    inputs = iter(user_input)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert tic_tac_toe.ask_board_size() == expected

    captured = capsys.readouterr()
    assert "Invalid input." in captured.out


def test_player_1_wins(monkeypatch, capsys):
    inputs = iter([
        '3', # board size
        '1', '1',
        '1', '2',
        '2', '2',
        '1', '3',
        '3', '2',
        '2', '1',
        '3', '3',
        'y', # another game
        'n', # restart game
        '2', '1',
        '1', '1',
        '3', '2',
        '1', '2',
        '2', '3',
        '1', '3',
        'y', # another game
        'n', # restart game
        '1', '1',
        '1', '2',
        '1', '3',
        '3', '1',
        '3', '2',
        '3', '3',
        '2', '1',
        '2', '2',
        '2', '3',
        'n' # another game
    ])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    tic_tac_toe.main()

    captured = capsys.readouterr()
    print(captured.out)
    assert all([
        "Player 1 wins!" in captured.out,
        "It's a draw!" in captured.out,
        "Player 1: 1" in captured.out,
        "Player 1: 2" in captured.out,
    ])
