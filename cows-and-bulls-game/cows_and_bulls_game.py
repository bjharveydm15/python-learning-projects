"""
Cows and Bulls Game

A command-line implementation of the classic Cows and Bulls guessing game.

This module provides:
    - Secret number generation
    - Difficulty selection
    - Hint management
    - Input validation
    - Gameplay logic

Workflow:
    1. Prompt the player to select the secret number length
       and a difficulty level.
    2. Set the allowed attempts and available hints.
    3. Generate a random secret number.
    4. Award a hint after a specified number of attempts,
       depending on the selected difficulty.
    5. Offer the player the option to use an available hint.
    6. Reveal the hint if the player chooses to use it.
    7. Prompt the player to enter a guess.
    8. Compare the guess with the secret number.
    9. Display the number of cows and bulls.
   10. End the game when the player guesses the secret number or
       the player runs out of attempts, then reveal the secret number.
"""

import random

# --------------------------------------------------------------------
# Initialization Functions:
# These functions adjusts game setup according to the player's choice.
# --------------------------------------------------------------------

def ask_secret_length() -> int:
    """
    Prompt the player for the secret number length.

    Repeatedly prompts until the player enters a valid integer greater
    than 3.

    Returns
    -------
    int
        The validated secret number length.
    """

    while True:
        try:
            secret_length = int(input('Choose how many numbers do you want to guess? '))
        except ValueError:
            print('Please enter a number.')
            continue

        if secret_length <= 3:
            print('Please enter a number greater than 3.')
            continue

        return secret_length


def ask_difficulty() -> str:
    """
    Prompt the player to choose a difficulty level.

    The selected difficulty determines the maximum number of allowed
    attempts and the number of hints available during the game.

    Returns
    -------
    str
        The selected difficulty level: "forgiving", "balanced", or
        "flawless".
    """

    while True:
        difficulty = input(
            'Choose guess difficulty (forgiving, balanced, flawless): '
        ).lower()

        if difficulty not in ('forgiving', 'balanced', 'flawless'):
            print('Please choose only between forgiving, balanced, and flawless')
            continue

        return difficulty


def set_allowed_attempts(state: dict) -> int:
    """
    Calculates the maximum allowed attempts for the game.

    The calculation is based on the selected difficulty level and
    secret number length.

    Parameters
    ----------
    state : dict
        The current game state.

        Expected keys are:

            difficulty : str
                The current game difficulty. Valid values are "forgiving",
                "balanced", and "flawless".
            secret_length : int
                The number of digits in the secret number.

    Returns
    -------
    int
        The maximum number of attempts allowed for the entire game.
    """

    s = state

    if s['difficulty'] == 'forgiving':
        allowed_attempts = s['secret_length'] * 2 + 6
    elif s['difficulty'] == 'balanced':
        allowed_attempts = s['secret_length'] * 2 + 3
    elif s['difficulty'] == 'flawless':
        allowed_attempts = s['secret_length'] * 2

    return allowed_attempts


def generate_numbers(state: dict) -> list[int]:
    """
    Generates a random secret number.

    Parameters
    ----------
    state : dict
        The current game state.

        Expected keys are:

            secret_length : int
                The number of digits in the secret number.

    Returns
    -------
    list[int]
        The generated secret number.
    """

    length = state['secret_length']
    secret_number = []

    for i in range(length):
        secret = random.randint(0,9)
        secret_number.append(secret)

    print(f'\nI have generated a {length}-digit number with unique digits.'
        ' Try to guess it!')

    return secret_number


# ------------------------------------------------------------------
# Hint Functions:
# ------------------------------------------------------------------

def should_add_hint(state: dict) -> int:
    """
    Determine whether an additional hint should be awarded.

    A hint should be awarded based on the selected difficulty
    level after a specified number of attempts.

    Parameters
    ----------
    state : dict
        The current game state.

        Expected keys are:

            difficulty : str
                The current game difficulty. Valid values are "forgiving",
                "balanced", and "flawless".
            allowed_attempts : int
                The maximum number of attempts allowed in the game.
            attempts : int
                The current attempt count in the game.

    Returns
    -------
    int
        1 if a hint should be awarded; otherwise, 0.
    """

    s = state

    add_hint = 0

    if s['difficulty'] == 'forgiving':
        hint_signal = round(s['allowed_attempts'] / 3)

        if s['attempts'] in (hint_signal, hint_signal * 2):
            add_hint = 1

    elif s['difficulty'] == 'balanced':
        if s['attempts'] == round(s['allowed_attempts'] / 2):
            add_hint = 1

    return add_hint


def offer_hint(is_consecutive: bool) -> bool:
    """
    Offer a hint to the player.

    A hint is offered only when there is at least one hint available.

    Parameters
    ----------
    is_consecutive : bool
        Determines if a hint has already been offered during the
        current attempt.

    Returns
    -------
    bool
        True if the player chooses to reveal a hint; otherwise, False.
    """

    while True:
        if not is_consecutive:
            is_yes = input('\nDo you want a hint (y/n): ').lower()
        else:
            is_yes = input('\nDo you want another hint (y/n): ').lower()

        if is_yes not in ('y', 'n'):
            print('Please enter either y or n only.')
            continue

        if is_yes == 'y':
            return True
        else:
            return False


def reveal_hint(state: dict) -> int:
    """
    Reveal the hint to the player.

    The hint revealed depends on the current game difficulty. For the
    forgiving difficulty, multiple hints are revealed sequentially.

    Parameters
    ----------
    state : dict
        The current game state.

        Expected keys are:

            difficulty : str
                The current game difficulty. Valid values are "forgiving",
                "balanced", and "flawless".
            secret_number : list[int]
                The digits of the randomly generated secret number.
            hint_1_used : bool
                Whether the first hint has already been revealed.

    Returns
    -------
    int
        The number of hints to deduct from the player's remaining hints.
        Returns 1 when a hint is revealed; otherwise, 0.

    Notes
    -----
    For the forgiving difficulty, the game state is updated after the
    first hint is revealed so that subsequent calls reveal the second hint.
    """

    s = state

    deduct_hint = 0

    if s['difficulty'] == 'balanced':
        hint = sum(s['secret_number'])
        print(f'Hint: The sum of the digits is {hint}')
        deduct_hint = 1

    if s['difficulty'] == 'forgiving':
        if not s['hint_1_used']:
            first_hint = sum(s['secret_number'])
            print(f'Hint: The sum of the digits is {first_hint}')
            deduct_hint = 1
            s['hint_1_used'] = True
        else:
            second_hint = sum(1 for x in s['secret_number'] if x % 2 == 0)
            print(f'Hint: The secret number contains {second_hint} even digits.')
            deduct_hint = 1

    return deduct_hint


# ------------------------------------------------------------------
# Logical Functions:
# The modules required functions to carry out game logic.
# ------------------------------------------------------------------

def guess_secret(state: dict) -> str:
    """
    Prompt the player to enter a guess.

    The player's input is validated to ensure it is numeric and contains
    the expected number of digits before being accepted.

    Parameters
    ----------
    state : dict
        The current game state.

        Expected keys are:

            secret_length : int
                The number of digits in the secret number.

    Returns
    -------
    str
        The validated guess entered by the player.
    """

    s = state

    while True:
        user_guess = input('Guess: ')

        if not user_guess.isdigit():
            print("Please enter a number.")
            continue

        guess_count = len(list(user_guess))

        if guess_count != s['secret_length']:
            print(f"Please enter a {s['secret_length']}-digit number.")
            continue

        return user_guess


def check_guess(state: dict) -> bool:
    """
    Compare the player's guess to the secret number.

    If a digit in the player's guess matches a digit in the
    secret number in the exact position, it is marked as a bull.
    If it matches the number but the position is wrong, it is
    marked as a cow.

    Parameters
    ----------
    state : dict
        The current game state.

        Expected keys are:

            user_guess : str
                The player's guess.
            secret_number : list[int]
                The secret number to be guessed by the player.
            secret_length : int
                The number of digits in the secret number.

    Returns
    -------
    bool
        True if the number of bulls matches the secret_length;
        otherwise, False.
    """

    s = state

    bulls = 0
    cows = 0

    guess_number = [int(x) for x in s['user_guess']]

    dummy_secret = s['secret_number'].copy()
    dummy_guess = guess_number.copy()

    for guess, secret in zip(guess_number, s['secret_number']):
        if guess == secret:
            bulls += 1
            dummy_secret.remove(secret)
            dummy_guess.remove(guess)

    for guess in dummy_guess:
        if guess in dummy_secret:
            cows += 1
            dummy_secret.remove(guess)

    if bulls == s['secret_length']:
        return True

    print(f'Bulls: {bulls} Cows: {cows}')

    return False


def reveal_secret(state: dict) -> str:
    """
    Convert the secret number to a string.

    Parameters
    ----------
    state : dict
        The current game state.

        Expected keys are:

            secret_number : list[int]
                The digits of the randomly generated secret number.

    Returns
    -------
    str
        The secret number represented as a string.
    """

    s = state

    secret_number = s['secret_number']

    return ''.join(str(x) for x in secret_number)


def main():
    """
    Run the game.

    Initializes the game state dictionary, configures the game based on
    player input, executes the main gameplay loop, manages hints and
    attempts, and displays either the winning message or the secret
    number when the game ends.
    """

    state = {
        'attempts': 1,
        'hints': 0,
        'hint_1_used': False,
        'user_guess': None,
        'correct_guess': None,
        'secret_number': None,
        'secret_length': None,
        'allowed_attempts': None,
        'difficulty': None
    }

    s = state

    s['difficulty'] = ask_difficulty()
    s['secret_length'] = ask_secret_length()
    s['allowed_attempts'] = set_allowed_attempts(state)

    s['secret_number'] = generate_numbers(state)

    print(f"Your maximum allowed attempts is {s['allowed_attempts']}")

    while s['attempts'] <= s['allowed_attempts']:
        print(f"\nattempt: {s['attempts']}")

        s['user_guess'] = guess_secret(state)

        is_game_solved = check_guess(state)

        if is_game_solved:
            print(f"\nYou guessed the secret number in {s['attempts']} attempts!")
            break

        s['attempts'] += 1

        add_hint = should_add_hint(state)
        s['hints'] += add_hint

        is_consecutive = False

        while True:
            if s['hints'] == 0:
                break
            else:
                is_yes = offer_hint(is_consecutive)

                if is_yes:
                    deduct_hint = reveal_hint(state)

                    s['hints'] -= deduct_hint

                    is_consecutive = True

                else:
                    break

    if s['attempts'] > s['allowed_attempts']:
        revealed = reveal_secret(state)
        print('\nYou have reached maximum number of attempts!')
        print(f'The secret number is {revealed}')


if __name__ == '__main__':
    main()
