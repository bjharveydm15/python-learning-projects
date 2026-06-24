from textwrap import dedent

def system_message(key):
    messages = {
        'EMPTY': 'No existing category to rename.',
        'NOT_FOUND': 'Chosen category does not exist.',
        'SUCCESS': 'Category successfully modified.',
        'DUPLICATE': 'Category already exists.',
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
    run_menu(menu, 4)

def category_menu():
    print(f'{'-' * 40}')

    menu = dedent('''
        1. Create a new category
        2. Rename an existing category
        3. Delete an existing category
        4. Back to main menu
    ''')

    run_menu(menu, 4)

def expenses_menu():

    menu = dedent('''
        1. Add an expense
        2. Delete an expense
        3. Back to main menu
    ''')

    run_menu(menu, 3)

def view_menu():

    menu = dedent('''
        1. View expenses by category
        2. View all expenses
        3. Back to main menu
    ''')

    run_menu(menu, 3)

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

def enter_amount(self):
    print(f'{'-' * 40}')

    while True:
        try:
            expense = float(input('Enter amount: ').strip())

            if expense <= 0:
                print('Amount must be greater than 0.')

            return expense

        except ValueError:
            print('Please enter a valid number.')
