import sqlite3

def create_table():
    with sqlite3.connect('expenses_tracker.db') as connection:
        connection.execute("PRAGMA foreign_keys = ON")

        connection.execute(
            '''
            Create Table IF NOT EXISTS Categories(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
            '''
        )

        connection.execute('''
            Create Table IF NOT EXISTS Expenses(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                FOREIGN KEY (category_id) 
                REFERENCES Categories(id)
                ON DELETE CASCADE
            )
        ''')

def insert_category(new_name):
    with sqlite3.connect('expenses_tracker.db') as connection:
        connection.execute("PRAGMA foreign_keys = ON")

        connection.execute(
            '''
            INSERT INTO Categories (name)
            VALUES (?)
            ''',
            (new_name,)
        )

def insert_amount(category, new_amount):
    with sqlite3.connect('expenses_tracker.db') as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        category_id = query_id(connection, category)

        if category_id is None:
            return

        connection.execute(
            '''
            INSERT INTO Expenses (category_id, amount)
            VALUES (?, ?)
            ''',
            (category_id, new_amount)
        )

def query_category(name):
    with sqlite3.connect('expenses_tracker.db') as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()

        result = cursor.execute(
            '''
            SELECT name FROM Categories
            WHERE name = ?
            ''',
            (name,)
        ).fetchone()

        return result[0] if result else None

def query_records():
    with sqlite3.connect('expenses_tracker.db') as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()

        cursor.execute(
            '''
            SELECT * FROM Expenses
            '''
        )
        return cursor.fetchall()

def query_id(connection, name):
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()

    cursor.execute(
        '''
        SELECT id FROM Categories
        WHERE name = ?
        ''', (name,)
    )
    data = cursor.fetchone()

    return data[0] if data else None

def update_category(new_name, old_name):
    with sqlite3.connect('expenses_tracker.db') as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        category_id = query_id(connection, old_name)

        if category_id is None:
            return

        connection.execute(
            '''
            UPDATE Categories 
            SET name = ? 
            WHERE id = ?
            ''',
            (new_name, category_id)
        )

def delete_category(name):
    with sqlite3.connect('expenses_tracker.db') as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        category_id = query_id(connection, name)

        if category_id is None:
            return

        connection.execute(
            '''
            Delete FROM Expenses
            WHERE category_id = ?
            ''',
            (category_id,)
        )

        connection.execute(
            '''
            Delete FROM Categories
            WHERE id = ?
            ''',
            (category_id,)
        )

def delete_expenses(name):
    with sqlite3.connect('expenses_tracker.db') as connection:
        connection.execute("PRAGMA foreign_keys = ON")

        connection.execute('''
            Delete FROM Expenses
            WHERE id = (
                SELECT MAX(id)
                FROM Expenses
            )
        ''')
