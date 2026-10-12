import sqlite3

connection = sqlite3.connect('expenses.db')
connection.execute("PRAGMA foreign_keys = ON")  # makes SQLite enforce the category link

connection.execute("""
    CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE COLLATE NOCASE  
    )
""")
#the collate nocase makes Food == food
connection.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        amount REAL NOT NULL,
        description TEXT,
        date TEXT NOT NULL,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
""")
connection.commit()


def insert_category(name):
    cursor = connection.execute("INSERT INTO categories(name) VALUES (?)", (name,))
    connection.commit()
    return cursor.lastrowid


def get_all_categories():
    return connection.execute("SELECT id, name FROM categories ORDER BY name").fetchall()


def add_expense_to_database(category_id, name, amount, description, date):
    connection.execute(
        "INSERT INTO expenses(category_id,name, amount, description, date) VALUES (?, ?, ?, ?,?)",
        (category_id,name, amount, description, date),
    )
    connection.commit()


def get_expenses_by_category(category_id):
    query = """
        SELECT id, name, amount, description, date
        FROM expenses
        WHERE category_id = ?
        ORDER BY date DESC
    """
    return connection.execute(query, (category_id,)).fetchall()


def get_total_expenses():
    result = connection.execute("SELECT SUM(amount) FROM expenses").fetchone()
    return result[0] or 0

def get_expenses():
    query = """
        SELECT e.id, e.name, c.name, e.amount, e.description, e.date
        FROM expenses e
        JOIN categories c ON c.id = e.category_id
        ORDER BY e.date DESC
    """
    return connection.execute(query).fetchall()


def get_expense_by_id(expense_id):
    query = """
        SELECT id, category_id, name, amount, description, date
        FROM expenses
        WHERE id = ?
    """
    return connection.execute(query, (expense_id,)).fetchone()


def update_expense(expense_id, category_id, name,  amount, description):
    connection.execute(
        "UPDATE expenses SET category_id = ?,name = ?, amount = ?, description = ? WHERE id = ?",
        (category_id, name, amount, description, expense_id),
    )
    connection.commit()


def delete_expense(expense_id):
    connection.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    connection.commit()