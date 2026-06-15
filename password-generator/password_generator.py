import string
import random
import json
from pathlib import Path

class PasswordGenerator:
    def __init__(self):
        self.criteria = {
            'has_upper': {
                'bool': False,
                'prompt': "Include uppercase letters? (y/n): ",
                'implementation': string.ascii_uppercase
            },
            'has_number': {
                'bool': False,
                'prompt': "Include numbers? (y/n): ",
                'implementation': string.digits
            },
            'has_symbol': {
                'bool': False,
                'prompt': "Include special characters? (y/n): ",
                'implementation': string.punctuation
            }
        }
        self.pass_count = 1
        self.length = 1
        self.new_passwords = []
        self.stored_passwords = []

    def get_criteria(self, asked):
        get_values = []

        for key in self.criteria.keys():
            get_values.append(self.criteria[key][asked])

        return get_values

    def ask_criteria(self):
        self.ask_password_count('How many passwords would you like to generate? ')

        prompts = self.get_criteria('prompt')

        for prompt, key in zip(prompts, self.criteria.keys()):
            self.ask_y_or_n(prompt, key)

        self.ask_length("Enter password length: ")

    def ask_password_count(self, prompt):
        while True:
            try:
                generation_count = int(input(prompt))

                if generation_count < 1:
                    print('Password length must at least 1.')
                    continue

                self.pass_count = generation_count
                return

            except ValueError:
                print('Please enter a valid number.')

    def ask_y_or_n(self, prompt, key):
        while True:
            y_or_n = input(prompt).strip()

            if y_or_n.lower() == 'y':
                self.criteria[key]['bool'] = True
                return
            elif y_or_n.lower() == 'n':
                return

            print('Please enter y or n only.')

    def ask_length(self, prompt):
        required = 1 + sum(criterion['bool'] for criterion in self.criteria.values())

        while True:
            try:
                self.length = int(input(prompt).strip())

                if self.length < required:
                    print(f'Password length must be at least {required} characters long.')
                    continue

                return
            except ValueError:
                print('Please enter a valid password length.')

    def generate_password(self):
        while len(self.new_passwords) < self.pass_count:
            char_pool = string.ascii_lowercase
            password = [random.choice(string.ascii_lowercase)]

            implementations = self.get_criteria('implementation')
            bools = self.get_criteria('bool')

            for implementation, implemented in zip(implementations, bools):
                if implemented:
                    char_pool += implementation
                    password.append(random.choice(implementation))

            while len(password) < self.length:
                password.append(random.choice(char_pool))
            random.shuffle(password)

            unique_pass = ''.join(password)

            if unique_pass not in self.new_passwords:
                self.new_passwords.append(unique_pass)

    def show_password(self):
        print('\nGenerated passwords:')

        for password in self.new_passwords:
            print(f'\t{password}')
        print('\n')

    def save(self):
        while True:
            y_or_n = input('Do you want to save the passwords generated? (y/n): ').strip()

            if y_or_n.lower() == 'y':
                if not Path('saved_passwords.json').exists():
                    with open('saved_passwords.json', 'w') as file:
                        json.dump(self.new_passwords, file, indent=4)
                        return
                while True:
                    y_or_n = input('Overwrite existing file? (y/n): ').strip()

                    if y_or_n.lower() == 'y':
                        with open('saved_passwords.json', 'w') as file:
                            json.dump(self.new_passwords, file, indent=4)
                            return
                    if y_or_n.lower() == 'n':
                        self.stored_passwords.extend(self.new_passwords)

                        with open('saved_passwords.json', 'w') as file:
                            json.dump(self.stored_passwords, file, indent=4)
                            return
                    else:
                        print('Please enter y or n only.')
            elif y_or_n.lower() == 'n':
                return
            else:
                print('Please enter y or n only.')

    def load(self):
        try:
            with open('saved_passwords.json', 'r') as file:
                self.stored_passwords = json.load(file)
        except FileNotFoundError:
            return

        while True:
            y_or_n = input('Do you want to see previous saved passwords? (y/n): ').strip()

            if y_or_n.lower() == 'y':
                print('\nStored Passwords:')
                for password in self.stored_passwords:
                    print(f'\t{password}')
                print('\n')
                return
            elif y_or_n.lower() == 'n':
                return
            else:
                print('Please enter y or n only.')


if __name__ == '__main__':
    generate_passwords = PasswordGenerator()
    generate_passwords.load()
    generate_passwords.ask_criteria()
    generate_passwords.generate_password()
    generate_passwords.show_password()
    generate_passwords.save()
