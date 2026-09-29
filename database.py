import sqlite3
connection = sqlite3.connect('expenses.db') #establishing a database connection 

#creating the database table
create_table = """
            CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL)
"""
connection.execute(create_table)  #executing the data table created
connection.commit()

#inserting expense items automatically into the database
def add_expense_to_database(type, amount, date):
  insert_expense = """
            INSERT INTO expenses(type, amount, date)
            VALUES (?, ?, ?) 
  """
  connection.execute(insert_expense, (type, amount, date)) 
  connection.commit()

#retriving expenses from the table
def get_expenses():
  view_expenses = """
              SELECT * FROM expenses
  """
  result = connection.execute(view_expenses)  
  expenses = result.fetchall()
  return expenses


#updating the data
def update_expense(type, amount, id):
  update_expense = """
          UPDATE expenses
          SET type = ? , amount = ?
          WHERE id = ?

          """
  connection.execute(update_expense, (type, amount, id))
  connection.commit()

#deleting an expense
def delete_expense(id):
  delete_expense = """
          DELETE FROM expenses
          WHERE id = ?
  """
  connection.execute(delete_expense, (id,))
  connection.commit()

