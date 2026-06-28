import expense_tracker_database as db
import expense_tracker_ui as ui

state = {
    'new_name': '',
    'existing_name': '',
    'amount': 0
}

# database
def insert_database(data):
    db.insert_category(data)
    validate('SUCCESS')

def update_database(old_data, new_data):
    db.update_category(old_data, new_data)
    validate('SUCCESS')

def delete_database(old_data):
    db.delete_category(old_data)
    validate('SUCCESS')

def record_expense(category, amount):
    db.insert_amount(category, amount)
    validate('SUCCESS')

def remove_expense():
    db.delete_expenses()
    validate('SUCCESS')

def in_database(data):
    is_found = db.query_category(data)

    if is_found is None:
        return False
    else:
        return True

# ui
def add_category():
    new_data = is_unique()

    if new_data:
        insert_database(state['new_name'])

def rename_category():
    old_data = is_existing()

    if old_data:
        new_data = is_unique()

        if new_data:
            update_database(state['existing_name'], state['new_name'])

def delete_category():
    old_data = is_existing()

    if old_data:
        delete_database(state['existing_name'])

def add_expense():
    category = is_existing()

    if category:
        state['amount'] = ui.enter_amount()
        record_expense(state['existing_name'], state['amount'] )

def delete_expense():
    will_delete = ui.delete_last_expense()

    if will_delete:
        remove_expense()

def view_expenses():
    category = is_existing()

    if category:
        records = db.query_records(state['existing_name'])
        ui.view_expenses(records)

def is_unique():
    state['new_name'] = ui.new_category()

    if not state['new_name']:
        validate('NOT_VALID')
        return False

    if in_database(state['new_name']):
        validate('DUPLICATE')
        return False

    return True

def is_existing():
    state['existing_name'] = ui.is_existing()

    if not in_database(state['existing_name']):
        validate('NOT_FOUND')
        return False

    return True

def validate(error_code):
    ui.system_message(error_code)
