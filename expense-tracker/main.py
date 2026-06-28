import expense_tracker_ui as ui
import expense_tracker_logic as logic
import expense_tracker_database as db
import sys

def main_menu():
    page = ui.main_menu()
    main_interface[page]()

def category_menu():
    page = ui.category_menu()
    category_interface[page]()
    category_menu()

def expenses_menu():
    page = ui.expenses_menu()
    expenses_interface[page]()
    expenses_menu()

def view_menu():
    page = ui.view_menu()
    view_interface[page]()
    view_menu()

main_interface = {
    1: category_menu,
    2: expenses_menu,
    3: view_menu,
    4: sys.exit
}

category_interface = {
    1: logic.add_category,
    2: logic.rename_category,
    3: logic.delete_category,
    4: main_menu
}

expenses_interface = {
    1: logic.add_expense,
    2: logic.delete_expense,
    3: main_menu
}

view_interface = {
    1: logic.view_expenses,
    2: main_menu
}

if __name__ == '__main__':
    db.create_table()
    main_menu()
