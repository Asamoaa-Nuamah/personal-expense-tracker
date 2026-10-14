# Personal Expense Tracker

A Python command-line application for tracking personal spending, organizing expenses by category, and reviewing totals over time.

This project uses SQLite to persist data locally and provides a simple menu-driven interface for adding, viewing, summarizing, editing, and deleting expense records.

## Overview

The expense tracker allows users to:

- Add expenses with a category, name, amount, and optional description
- View expenses by category or date
- Review overall spending totals
- View spending summaries by category
- Edit existing entries
- Delete records when needed
- Keep data saved between sessions in a local SQLite database

## Current Features

- Add new expenses with validation
- Create and reuse categories
- View expenses by category
- View expenses for today or a specific date
- View summaries by category and total spend
- Edit an existing expense
- Delete an existing expense
- Persistent SQLite storage using `expenses.db`

## Project Structure

```text
Expense_Tracker/
├── main.py
├── add_expense.py
├── view_expense.py
├── summary_expense.py
├── delete_expense.py
├── edit_expense.py
├── database.py
├── expenses.db
├── README.md
└── .gitignore
```

## Application Flow

The app is structured around a small menu system in `main.py`:

- `main.py` controls the main menu and program flow
- `add_expense.py` handles category selection and adding expense records
- `view_expense.py` displays stored expenses using category/date filters
- `summary_expense.py` calculates overall and per-category spending summaries
- `delete_expense.py` removes selected records
- `edit_expense.py` updates selected records
- `database.py` handles the SQLite database schema and queries

## Requirements

- Python 3.8+
- SQLite support (included with Python)

## Run the App

From the project folder, run:

```bash
python3 main.py
```

## Main Menu

The current menu in the project is:

```text
===== PERSONAL EXPENSE TRACKER =====
1. Add expense
2. View expenses
3. Spending summary
4. Delete expense
5. Edit expense
6. Exit
```

### Menu Options

1. Add expense
   - Select an existing category or create a new one
   - Enter the expense name and amount
   - Optionally include a description

2. View expenses
   - View expenses by category
   - View today’s expenses
   - View expenses for a specific date

3. Spending summary
   - Shows totals for categories and overall spend

4. Delete expense
   - Choose an expense ID to remove from the database

5. Edit expense
   - Update a selected expense’s details

6. Exit
   - Close the application

## Data Storage

The application stores all data in a local SQLite database file named `expenses.db`.

The database currently contains:

- `categories` table
- `expenses` table

Each expense record includes:

- ID
- category ID
- name
- amount
- description
- date

## Data Validation

The app includes basic validation to improve reliability:

- Rejects negative amounts
- Rejects invalid numeric input
- Prevents empty expense names
- Validates category selection
- Confirms deletion before removing records

## Example Workflow

1. Run `python3 main.py`
2. Select option 1 to add an expense
3. Choose a category or create a new one
4. Enter the expense name and amount
5. Use option 2 to view records or option 3 for summary totals
6. Use option 4 or 5 to remove or update records as needed

## Use Cases

This app is suitable for:

- Daily personal budgeting
- Tracking recurring expenses
- Monitoring spending by category
- Simple local financial record keeping

## Notes

This is a lightweight local CLI budgeting tool intended for personal use. It does not include a web dashboard, authentication, cloud sync, or backup system in its current version.
