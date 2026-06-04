def load_tasks():
    opened_file = input('Enter the file name to open or create: ')

    try:
        with open(opened_file, 'r') as f:
            print(f'{opened_file} found. Opening existing file.')
            old_content = f.read()
    except FileNotFoundError:
        with open(opened_file, 'w') as f:
            print(f'{opened_file} not found. Creating a new file.')
            old_content = ''

    return opened_file, old_content

def save_tasks(opened_file, old_content, new_content):
    if not old_content:
        with open(opened_file, 'w') as f:
            f.write(new_content)
    if old_content:
        while True:
            write_or_append = input('Overwrite existing file (Press 1)\n'
                                    + 'Append new text to the end of the file (Press 2): ')

            if write_or_append not in ('1','2'):
                print('Please choose 1 or 2 only')
                continue

            break

        if write_or_append == '1':
            with open(opened_file, 'w') as f:
                f.write(new_content)

        if write_or_append == '2':
            with open(opened_file, 'w') as f:
                f.write(old_content + '\n' + new_content)

def edit_content(old_content):
    print("Enter your text (type 'SAVE' on a new line to save and exit): ")
    print(old_content)

    new_content = ''

    while True:
        user_input = input()

        if user_input.lower() == 'save':
            return new_content

        if new_content:
            new_content += '\n' + user_input
        else:
            new_content = user_input

def search_and_replace(old_content):
    search = input('Enter text to search: ')
    replace = input('Enter replacement text:  ')

    old_content = old_content.replace(search, replace)

    return old_content

def main():
    opened_file, old_content = load_tasks()

    while True:
        will_search = input('Do you want to look for a specific key ' +
                            'word or phrase and replace them? (y/n): ').lower()

        if will_search not in ('y','n'):
            print('Please choose either y or n only')
            continue

        if will_search == 'y':
            old_content = search_and_replace(old_content)

        break

    new_content = edit_content(old_content)
    save_tasks(opened_file, old_content, new_content)

if __name__ == "__main__":
        main()
