import random

def generate_numbers(state):
    s = state
    secret_number = []

    for i in range(s['secret_length']):
        secret = random.randint(0,9)
        secret_number.append(secret)

    print(f'\nI have generated a {s['secret_length']}-digit number with unique digits.'
        ' Try to guess it!')

    return secret_number

def guess_secret(state):
    s = state

    while True:
        user_guess = input('Guess: ')

        if not user_guess.isdigit():
            print("Please enter a number.")
            continue

        guess_count = len(list(user_guess))

        if guess_count != s['secret_length']:
            print(f'Please enter a {s['secret_length']}-digit number.')
            continue

        return user_guess

def check_guess(state):
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

def ask_difficulty():
    while True:
        try:
            secret_length = int(input('Choose how many numbers do you want to guess? '))
        except ValueError:
            print('Please enter a number.')
            continue

        if secret_length <= 3:
            print('Please enter a number greater than 3.')
            continue

        break

    while True:
        difficulty = input(
            'Choose guess difficulty (forgiving, balanced, flawless): '
        ).lower()

        if difficulty not in ('forgiving', 'balanced', 'flawless'):
            print('Please choose only between forgiving, balanced, and flawless')
            continue

        return secret_length, difficulty

def set_allowed_attempts(state):
    s = state

    if s['difficulty'] == 'forgiving':
        allowed_attempts = s['secret_length'] * 2 + 6
    elif s['difficulty'] == 'balanced':
        allowed_attempts = s['secret_length'] * 2 + 3
    elif s['difficulty'] == 'flawless':
        allowed_attempts = s['secret_length'] * 2

    return allowed_attempts

def should_add_hint(state):
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

def offer_hint(is_consecutive):
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

def reveal_hint(state):
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

def reveal_secret(state):
    s = state

    secret_number = s['secret_number']

    return ''.join(str(x) for x in secret_number)

def main():
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

    s['secret_length'], s['difficulty'] = ask_difficulty()

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
