import string

def create_password():
    return input("Enter a password: ")

def validate_length(password):
    if len(password) <= 4:
        return 0, 'add more characters'
    elif len(password) <= 6:
        return 1, 'add more characters'
    elif len(password) <= 8:
        return 2, 'add more characters'
    elif len(password) <= 10:
        return 3, 'add more characters'
    else:
        return 4, None

def validate_upper_case(password):
    for char in password:
        if char.isupper():
            return 1, None

    return 0, 'include an uppercase letter'

def validate_number(password):
    for char in password:
        if char.isdigit():
            return 1, None

    return 0, 'include a number'

def validate_special_character(password):
    for char in password:
        if char in string.punctuation:
            return 1, None

    return 0, 'include a special character'

def define_strength(score):
    if score == 0:
        return 'Very Weak'
    elif score <= 2:
        return 'Weak'
    elif score <= 4:
        return 'Medium'
    elif score <= 6:
        return 'Strong'
    else:
        return 'Very Strong'

def show_strength(pass_strength):
    print(f'Password strength: {pass_strength}')

def show_suggestions(pass_strength, suggestions):
    if pass_strength == 'Very Strong':
        return

    print('\nTry adding these:')

    for suggestion in suggestions:
        if suggestion is not None:
            print(f'\t{suggestion}')

    print('\n')

def main():
    score = 0
    suggestions = []

    password = create_password()

    temp_score, suggestion = validate_length(password)
    score += temp_score
    suggestions.append(suggestion)

    temp_score, suggestion = validate_upper_case(password)
    score += temp_score
    suggestions.append(suggestion)

    temp_score, suggestion = validate_number(password)
    score += temp_score
    suggestions.append(suggestion)

    temp_score, suggestion = validate_special_character(password)
    score += temp_score
    suggestions.append(suggestion)

    pass_strength = define_strength(score)
    show_strength(pass_strength)
    show_suggestions(pass_strength, suggestions)

if __name__ == '__main__':
    main()
