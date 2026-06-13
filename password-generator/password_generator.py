import string
import random

class PasswordGenerator:
    def __init__(self):
        self.length = 1
        self.has_upper = False
        self.has_digit = False
        self.has_special_char = False
        self.password = ''

    def ask_length(self):
            while True:
                try:
                    self.length =  int(input("Enter password length: ").strip())

                    if self.length < 4:
                        print('Password length must be at least 4.')
                        continue

                    return
                except ValueError:
                    print('Please enter a valid password length.')

    def ask_uppercase(self):
            while True:
                y_or_n = input("Include uppercase letters? (y/n): ").strip()

                if y_or_n.lower() == 'y':
                    self.has_upper = True
                    return
                elif y_or_n.lower() == 'n':
                    return

                print('Please enter y or n only.')

    def ask_numbers(self):
            while True:
                y_or_n = input("Include numbers? (y/n): ").strip()

                if y_or_n.lower() == 'y':
                    self.has_digit = True
                    return
                elif y_or_n.lower() == 'n':
                    return

                print('Please enter y or n only.')

    def ask_special_char(self):
            while True:
                y_or_n = input("Include special characters? (y/n): ").strip()

                if y_or_n.lower() == 'y':
                    self.has_special_char = True
                    return
                elif y_or_n.lower() == 'n':
                    return

                print('Please enter y or n only.')

    #generate password
    def generate_password(self):
        char_list = string.ascii_lowercase
        password = [random.choice(string.ascii_lowercase)]

        if self.has_upper:
            char_list += string.ascii_uppercase
            password.append(random.choice(string.ascii_uppercase))
        if self.has_digit:
            char_list += string.digits
            password.append(random.choice(string.digits))
        if self.has_special_char:
            char_list += string.punctuation
            password.append(random.choice(string.punctuation))

        while len(password) < self.length:
            password.append(random.choice(char_list))
        random.shuffle(password)

        self.password = ''.join(password)

        return

    def show_password(self):
        print(f'Generated password: {self.password}')

if __name__ == '__main__':
    generate_password = PasswordGenerator()
    generate_password.ask_length()
    generate_password.ask_uppercase()
    generate_password.ask_numbers()
    generate_password.ask_special_char()
    generate_password.generate_password()
    generate_password.show_password()
