import random

def generate_numbers(secret_number_length):
    secret_number = []

    for i in range(secret_number_length):
        secret = random.randint(0,9)
        secret_number.append(secret)

    print(f'\nI have generated a {secret_number_length}-digit number with unique digits.'
        ' Try to guess it!')

    return secret_number

def guess_secret(secret_number_length):
    while True:
        user_guess = input('Guess: ')

        try:
             int_guess = int(user_guess)
        except ValueError:
            print('Please enter a number.')
            continue

        guess_count = len(list(user_guess))

        if guess_count != secret_number_length:
            print(f'Please enter a {secret_number_length}-digit number.')
            continue

        return user_guess

def check_guess(secret_number, user_guess, secret_number_length):
    bulls = 0
    cows = 0

    guess_number = [int(x) for x in user_guess]

    dummy_secret = secret_number.copy()
    dummy_guess = guess_number.copy()

    for guess, secret in zip(guess_number, secret_number):
        if guess == secret:
            bulls += 1
            dummy_secret.remove(secret)
            dummy_guess.remove(guess)

    for guess in dummy_guess:
        if guess in dummy_secret:
            cows += 1
            dummy_secret.remove(guess)

    if bulls == secret_number_length:
        return True

    print(f'Bulls: {bulls} Cows: {cows}')
    return False

def difficulty_level():
    while True:
        try:
            secret_number_length = int(input('Choose how many numbers do you want to guess? '))
        except ValueError:
            print('Please enter a number.')
            continue

        if secret_number_length <= 3:
            print('Please enter a number greater than 3.')
            continue

        break

    while True:
        guessing_difficulty = input(
            'Choose guess difficulty (forgiving, balanced, flawless): '
        ).lower()

        if guessing_difficulty not in ('forgiving', 'balanced', 'flawless'):
            print('Please choose only between forgiving, balanced, and flawless')
            continue

        break

    if guessing_difficulty == 'forgiving':
        allowed_attempts = secret_number_length * 2 + 6
    elif guessing_difficulty == 'balanced':
        allowed_attempts = secret_number_length * 2 + 3
    elif guessing_difficulty == 'flawless':
        allowed_attempts = secret_number_length * 2

    return secret_number_length, allowed_attempts, guessing_difficulty

def check_hint(attempts, allowed_attempts, guessing_difficulty):
    add_hint = 0

    if guessing_difficulty == 'forgiving':
        hint_signal = round(allowed_attempts / 3)

        if attempts in (hint_signal, hint_signal * 2):
            add_hint = 1

    elif guessing_difficulty == 'balanced':
        if attempts == round(allowed_attempts / 2):
            add_hint = 1

    return add_hint

def offer_hints(prompt, active, guessing_difficulty, secret_number):
    deduct_hint = 0

    while True:
        offer_hint = input(prompt).lower()

        if offer_hint not in ('y', 'n'):
            print('Please enter either y or n only.')
            continue

        break

    if offer_hint == 'n':
        return False, deduct_hint, active
    else:
        if guessing_difficulty != 'flawless' and active:
            first_hint = sum(secret_number)
            print(f'Hint: The sum of the digits is {first_hint}')
            deduct_hint = 1
            active = False

        elif guessing_difficulty == 'forgiving':
            second_hint = sum(1 for x in secret_number if x % 2 == 0)
            print(f'Hint: The secret number contains {second_hint} even digits.')
            deduct_hint = 1
            active = False

    return True, deduct_hint, active

def main():
    attempts = 1
    hint = 0
    active = True

    secret_number_length, allowed_attempts, guessing_difficulty = difficulty_level()
    secret_number = generate_numbers(secret_number_length)

    print(f'Your maximum allowed attempts is {allowed_attempts}')

    while attempts <= allowed_attempts:
        print(f'\nattempt: {attempts}')
        user_guess = guess_secret(secret_number_length)
        correct_guess = check_guess(secret_number, user_guess, secret_number_length)

        if correct_guess:
            print(f'\nYou guessed the secret number in {attempts} attempts!')
            break

        attempts += 1

        add_hint = check_hint(attempts, allowed_attempts, guessing_difficulty)
        hint += add_hint

        if hint > 0:
            if active:
                another_hint, deduct_hint, active = offer_hints(
                    '\nDo you want a hint (y/n): ',
                        active, guessing_difficulty, secret_number)

                hint -= deduct_hint
                if another_hint:
                    active = False
            else:
                another_hint = True

            if hint > 0 and another_hint:
                another_hint, deduct_hint, active = offer_hints(
                    '\nDo you want another hint (y/n): ',
                    active, guessing_difficulty, secret_number)
                hint -= deduct_hint

    if attempts > allowed_attempts:
        reveal = ''.join(str(x) for x in secret_number)

        print('\nYou have reached maximum number of attempts!')
        print(f'The secret number is {reveal}')

if __name__ == '__main__':
    main()
