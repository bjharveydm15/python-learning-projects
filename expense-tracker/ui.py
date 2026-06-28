from textwrap import dedent

def system_message(key):
    messages = {
        'EMPTY': 'Field empty.',
        'NOT_FOUND': 'Chosen input does not exist.',
        'SUCCESS': 'Successfully updated.',
        'DUPLICATE': 'Input already exists.',
        'NOT_VALID': 'Input not valid.'
    }

    print(messages[key])

def main_menu():
    print(f'{'-' * 40}')
    print('EXPENSE TRACKER'.center(40, '-'))

    menu = dedent('''
        1. MODIFY CATEGORIES
        2. MANAGE EXPENSES
        3. VIEW EXPENSES HISTORY
        4. EXIT
    ''')
    return run_menu(menu, 4)

def category_menu():
    print(f'{'-' * 40}')

    menu = dedent('''
        1. Create a new category
        2. Rename an existing category
        3. Delete an existing category
        4. Back to main menu
    ''')

    return run_menu(menu, 4)

def expenses_menu():

    menu = dedent('''
        1. Add an expense
        2. Delete an expense
        3. Back to main menu
    ''')

    return run_menu(menu, 3)

def view_menu():

    menu = dedent('''
        1. View expenses by category
        2. Back to main menu
    ''')

    return run_menu(menu, 3)

def run_menu(menu, options):
    while True:
        print(menu)

        try:
            choice = int(input('Please press a number: ').strip())

            if choice in range(1, options + 1):
                return choice
            else:
                print(f'Please choose a number from 1 to {options} only')

        except ValueError:
            print('Please enter a valid number.')

def new_category():
    print(f'{'-' * 40}')

    return input('Please enter a new category name: ').strip()

def is_existing():
    print(f'{'-' * 40}')

    return input('Please enter an existing category name: ').strip()

def enter_amount():
    print(f'{'-' * 40}')

    while True:
        try:
            expense = float(input('Enter amount: ').strip())

            if expense <= 0:
                print('Amount must be greater than 0.')
                continue

            return expense

        except ValueError:
            print('Please enter a valid number.')

def delete_last_expense():
    print(f'{'-' * 40}')

    while True:
        y_or_n = input(
            'Do you want to delete the latest recorded expense? (y/n): '
        ).strip().lower()

        if y_or_n == 'y':
            return True
        elif y_or_n == 'n':
            return False
        else:
            print('Please enter y or n only.')

def view_expenses(records):
    print(f'{'-' * 40}')

    for record in records:
        print(record[0])
