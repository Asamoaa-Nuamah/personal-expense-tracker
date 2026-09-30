# Personal Expense Tracker

A command line personal expense tracker built with Python. The project allows users to record, view, categorize, calculate, edit, and delete expenses while maintaining data between program sessions using SQLite database storage.

The project was developed incrementally, with each version introducing new functionality and concepts.

---

## Features

### Version 1.0

* Add expenses
* Add multiple expenses in one session
* Validate expense amounts
* Prevent negative expense amounts
* Reject invalid non-numeric amounts
* View recorded expenses
* Calculate total expenses
* Interactive Git/GitHub project setup

### Version 2.0

* Filter expenses by category
* Calculate spending for a specific category
* Delete expenses
* Edit expense categories
* Edit expense amounts
* Edit both category and amount
* Improved input validation
* Case-insensitive category matching
* Formatted currency output

### Version 3.0

* Interactive main menu
* Improved program flow
* Persistent JSON storage
* Automatically load previously saved expenses
* Automatically save expenses when exiting
* Multiple expense entry integrated into the main menu
* Data remains available after restarting the program

### Version 4.0

* Automatically record the date when an expense is created
* Store expense category, amount, and date
* Use Python's `datetime` module for automatic date capture

### Version 5.0

* Introduced SQLite database storage
* Created an `expenses` database table
* Added unique database IDs for expenses
* Added expenses directly to the SQLite database
* Retrieve expenses from SQLite
* Update expenses directly in SQLite
* Delete expenses directly from SQLite
* Complete CRUD functionality using SQLite
* Use parameterized SQL queries
* Removed the previous JSON storage system

---

# Version 1.0

The first version focused on building the core functionality of the expense tracker.

### Adding Expenses

Users can enter:

* Expense category/type
* Expense amount

The program validates the amount and prevents negative values or non-numeric input.

### Viewing Expenses

Users can view all recorded expenses, including the expense category and amount.

### Calculating Total Expenses

The program calculates the total amount spent across all recorded expenses.

### Multiple Expense Entry

Users can add multiple expenses during a single run of the program.

---

# Version 2.0

Version 2.0 expanded the application from a basic expense tracker into a more functional expense management system.

### Categorizing Expenses

Users can enter a category and view only expenses belonging to that category.

Category matching is case-insensitive, meaning inputs such as `Food`, `food`, and `FOOD` can refer to the same category.

### Category Spending

Users can calculate the total amount spent within a particular category.

For example:

```text
Enter expense category you want to calculate: Food

Total spent on Food: GHC1,250.00
```

### Delete Expenses

Expenses are displayed with numbers, allowing users to select and delete a specific expense.

The program validates the selected number before deleting the expense.

### Edit Expenses

Users can select an existing expense and choose to:

1. Edit the category
2. Edit the amount
3. Edit both

Input validation is applied when entering new categories and amounts.

---

# Version 3.0

Version 3.0 focused on improving the overall application flow and introducing persistent data storage.

## Interactive Main Menu

Instead of automatically executing every function sequentially, the program now presents an interactive menu:

```text
===== PERSONAL EXPENSE TRACKER =====

1. Add expense
2. View expenses
3. Calculate total expenses
4. Categorize expenses
5. Calculate spending by category
6. Delete expense
7. Edit expense
8. Exit
```

The user selects an option, the corresponding function is executed, and the program returns to the main menu when the function is finished.

The program continues running until the user selects **Exit**.

## Multiple Expense Entry

The `add_expense()` function now handles multiple expense entries internally.

After adding an expense, the user is asked whether they want to add another expense.

```text
Do you want to add another expense? (Y/N):
```

Choosing `Y` allows another expense to be entered, while choosing `N` returns the user to the main menu.

## Persistent JSON Storage

Version 3.0 introduced JSON based persistent storage.

Expenses were stored in:

```text
expenses.json
```

The program automatically loaded previously saved expenses when it started.

When the user exited the program, the current expenses were automatically saved to the JSON file.

This allowed expenses to be preserved between program sessions.

### Data Flow

```text
Program starts
      ↓
Load expenses from JSON
      ↓
User adds / edits / deletes expenses
      ↓
Updated expenses remain in memory
      ↓
User chooses Exit
      ↓
Save expenses to JSON
      ↓
Program ends
```

---

# Version 4.0

Version 4.0 focused on improving the information stored for each expense by automatically recording the date.

## Automatic Expense Dates

When a new expense is created, the program automatically records the current date.

Each expense now contains:

* Expense category/type
* Expense amount
* Date

The Python `datetime` module is used to obtain the current date.

The date is converted to a string before being stored so that it can be handled by the application's persistent storage system.

Example:

```text
Food - GHC50.00 - 2026-09-29
```

This feature provides the foundation for future date-based features such as monthly and weekly spending summaries.

---

# Version 5.0

Version 5.0 introduced a major change to the application's data storage system.

Instead of storing expenses in a Python list and saving them to a JSON file, the application now uses a **SQLite database**.

## SQLite Database

The project uses Python's built-in `sqlite3` module to communicate with SQLite.

The database is stored locally in:

```text
expenses.db
```

A table named `expenses` was created with the following columns:

```text
id
type
amount
date
```

The `id` column is the primary key and is automatically generated by SQLite.

## Database CRUD Operations

Version 5.0 implements the four basic CRUD operations directly with SQLite.

### Create

New expenses are inserted into the database using an SQL `INSERT` statement.

```text
User enters expense
        ↓
Python
        ↓
INSERT into expenses
        ↓
SQLite database
```

### Read

Expenses are retrieved from the database using an SQL `SELECT` statement.

The application retrieves the latest database records whenever expenses need to be displayed or calculated.

### Update

Existing expenses can be edited using an SQL `UPDATE` statement.

The database ID is used to identify the specific expense that should be changed.

### Delete

Expenses can be removed using an SQL `DELETE` statement.

The database ID is used to identify the expense that should be deleted.

## Parameterized Queries

The project uses parameterized SQL queries with `?` placeholders.

For example:

```python
INSERT INTO expenses(type, amount, date)
VALUES (?, ?, ?)
```

The values are supplied separately when the query is executed.

This separates SQL statements from the data being inserted or updated.

## Database IDs

Each expense now has a unique database ID.

Example:

```text
3. Food - GHC50.89
8. Transport - GHC25.00
```

The ID allows the application to identify a specific database record when editing or deleting an expense.

This replaces the previous list-index-based approach.

## Migration from JSON to SQLite

The project initially used JSON storage in Version 3.0.

In Version 5.0, the storage system was migrated to SQLite.

The old JSON storage system was removed after the SQLite implementation was tested and confirmed to support the application's main features.

The current data flow is:

```text
Program starts
      ↓
Python application
      ↓
database.py
      ↓
SQLite
      ↓
expenses.db
```

---

# Project Structure

```text
personal-expense-tracker/

├── .gitignore
├── README.md
├── main.py
├── add_expense.py
├── view_expense.py
├── total_expense.py
├── categorizing_expense.py
├── category_total.py
├── delete_expense.py
├── edit_expense.py
├── database.py
└── expenses.db
```

## File Descriptions

| File                      | Purpose                                      |
| ------------------------- | -------------------------------------------- |
| `main.py`                 | Controls the main program flow and menu      |
| `add_expense.py`          | Handles adding one or multiple expenses      |
| `view_expense.py`         | Retrieves and displays recorded expenses     |
| `total_expense.py`        | Calculates total expenses                    |
| `categorizing_expense.py` | Filters expenses by category                 |
| `category_total.py`       | Calculates spending for a selected category  |
| `delete_expense.py`       | Deletes a selected expense from the database |
| `edit_expense.py`         | Edits an existing expense                    |
| `database.py`             | Handles SQLite database operations           |
| `expenses.db`             | Stores expense data in the SQLite database   |
| `README.md`               | Project documentation                        |

---

# Data Structure

In the earlier versions of the project, expenses were stored as a list of dictionaries.

Example:

```python
expenses = [
    {
        "type": "Food",
        "amount": 50.00
    },
    {
        "type": "Transport",
        "amount": 20.00
    }
]
```

Starting from Version 5.0, expenses are stored as rows in a SQLite database.

Each database row contains:

```text
ID
Category/Type
Amount
Date
```

When retrieved from SQLite using `fetchall()`, each expense is represented as a tuple:

```text
expense[0] → ID
expense[1] → Type
expense[2] → Amount
expense[3] → Date
```

This structure allows the application to work directly with persistent database records.

---

# Concepts Practiced

Throughout the development of this project, the following Python and software development concepts were practiced:

* Variables
* Lists
* Dictionaries
* Tuples
* Functions
* Function imports
* Modules
* `if` / `elif` / `else`
* `while` loops
* Nested loops
* `for` loops
* `break`
* User input
* Input validation
* `try` / `except`
* `ValueError`
* String methods
* Formatted strings (f-strings)
* Dictionary access and modification
* List operations
* JSON serialization and deserialization
* File handling
* Persistent data storage
* `datetime`
* SQLite
* SQL
* Tables
* Rows and columns
* Primary keys
* Database IDs
* `SELECT`
* `INSERT`
* `UPDATE`
* `DELETE`
* Parameterized SQL queries
* CRUD operations
* Modular program design
* Git and GitHub

---

# How to Run

Clone the repository and navigate into the project directory.

Then run:

```bash
python main.py
```

The application will display the main menu and allow the user to select the desired operation.

The SQLite database file is created and managed locally by the application.

---

# Current Limitations

The current version is a command line application and stores data locally in a SQLite database.

It does not currently include:

* A graphical user interface
* A web interface
* User accounts or authentication
* Advanced reporting or data visualization
* Budget management
* Monthly or weekly spending summaries
* Income tracking
* REST API functionality
* Multiple user support

---

# Future Improvements

Possible future improvements include:

* Add monthly and weekly spending summaries
* Add budget tracking
* Add income tracking
* Add spending reports
* Add data visualization
* Build a REST API
* Build a graphical or web interface
* Add search functionality
* Improve error handling and user experience
* Introduce a JavaScript frontend
* Connect the application to a more advanced database such as PostgreSQL

---

# Project Goal

The goal of this project is to build a practical Python application while progressively developing software engineering skills.

The project began as a simple command line expense tracker and has evolved through multiple stages:

```text
Python Lists
      ↓
JSON Storage
      ↓
Improved Expense Data
      ↓
SQLite Database
      ↓
CRUD Application
```

Each version introduces new concepts while building on the previous version.

Future versions will continue to expand the application's functionality while applying more advanced software development concepts, eventually moving toward a full stack expense management application.
