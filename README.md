# Personal Expense Tracker

A simple Python command-line app for tracking personal expenses, organizing them by category, and reviewing spending over time.

The project stores data in a local SQLite database, supports editing and deleting entries, and creates automatic backups so your records remain available between sessions.

## Features

- Add expenses with a category, name, amount, and optional description
- View expenses by category, week, month, year, or specific date
- Calculate total spending across all recorded expenses
- See category-based spending summaries with percentages
- Edit existing expenses and update category or amount
- Delete expenses safely by selecting their record ID
- Create and reuse categories for consistent tracking
- Keep persistent data in SQLite instead of temporary in-memory storage
- Back up the database automatically to the backups folder

## Project structure

```text
Expense_Tracker/
├── main.py
├── add_expense.py
├── view_expense.py
├── total_expense.py
├── summary_expense.py
├── delete_expense.py
├── edit_expense.py
├── database.py
├── expenses.db
├── backups/
├── README.md
└── .gitignore
```

## How it works

The app uses a menu-driven interface in `main.py` to route the user to the relevant action. Expenses are stored in `expenses.db`, and category and budget logic are handled in `database.py`.

## Run the app

Make sure Python 3 is installed, then start the program:

```bash
python3 main.py
```

If you prefer a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python main.py
```

## Main menu

```text
===== PERSONAL EXPENSE TRACKER =====
1. Add expense
2. View expenses
3. Calculate total expenses
4. Spending summary
5. Delete expense
6. Edit expense
7. Backup database
8. Exit
```

### Menu options

1. Add expense
   - Choose or create a category
   - Enter the expense name and amount
   - Optionally add a short description

2. View expenses
   - View all entries or filter by category, week, month, year, or date

3. Calculate total expenses
   - Shows the total amount spent across all records

4. Spending summary
   - Summarizes spending by category for all time or a selected time range

5. Delete expense
   - Select the expense ID to remove a record

6. Edit expense
   - Update the category, name, amount, or description of an existing entry

7. Backup database
   - Creates a timestamped copy in the backups directory

8. Exit
   - Saves a final backup automatically before closing

## Data storage

- Database file: `expenses.db`
- Backup folder: `backups/`
- Backup format: `expenses_YYYY-MM-DD_HH-MM-SS.db`

## Example workflow

1. Start the app with `python3 main.py`
2. Choose option 1 to add an expense
3. Select a category or create a new one
4. Enter the expense name and amount
5. Review totals and summaries in the menu
6. Use backups if you want a safe restore point

## Notes

This project is intended for personal budgeting and lightweight expense tracking. It is designed as a local command-line utility and does not include a web interface or cloud syncing.
